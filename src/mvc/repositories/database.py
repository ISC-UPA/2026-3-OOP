import os, sys
from pathlib import Path

# Add the project root so this file can also be run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
# sys.path.append(os.getcwd())

from src.config import get_db_config
from src.mvc.models.employee import Employee

import pandas as pd
import mysql.connector

COLUMNS = "employeeID, last_name, first_name, birth_date, hire_date"

class Database:
    """Singleton: una sola conexión MySQL compartida por todo el programa."""
    _instance = None

    # Se ejecuta antes de crear la instancia: construye y devuelve el objeto
    def __new__(cls, config:dict):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, config:dict) -> None: 
        # Evita re-inicializar la conexión cada vez que se llama Database()
        if not hasattr(self, "connection"):
            self.connection = mysql.connector.connect(**config)

    def _asegurar_conexion(self):
        """Si la conexión se cayó, la restablece (sigue siendo la misma instancia)."""
        if not self.connection.is_connected():
            self.connection.reconnect(attempts=3, delay=1)

    def close(self) -> None:
        """Cierra la conexión y permite crear una nueva en el futuro."""
        if hasattr(self, "connection"):
            self.connection.close()
            del self.connection
        Database._instance = None


    # Metodo para ejecutar consultas con o sin parametros 
    def execute_select(self, sql: str, params: tuple = ()) -> list[dict]:  # -> list[dict] o pd.DataFrame 
        self._asegurar_conexion()
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(sql, params)
            return cursor.fetchall()                 # list[dict]
            #return pd.DataFrame(cursor.fetchall())  # pd.DataFrame
        finally:
            cursor.close()

    # Metodo para ejecutar altas, bajas y cambios
    def execute_abc(self, sql: str, params: tuple = ()) -> tuple[int, int]:  
        #id = self.execute_many([(sql, params)]) 
        #return 0, id
        self.connection.ping(reconnect=True, attempts=3, delay=1)
        cursor = self.connection.cursor()
        try:
            if params is None:
                cursor.execute(sql)
            else:
                cursor.execute(sql, params)
            self.connection.commit()
            conteo = cursor.rowcount
            id = cursor.lastrowid
            return conteo, id
        except Exception:
            self.connection.rollback()
            raise
        finally:
            cursor.close()

    #id = self.execute_many([(sql, params)]) 
    def execute_many(self, statements: list[tuple[str, tuple]]) -> int:
        """Ejecuta varias instrucciones como una sola operación (transacción).
        O se guardan todas, o si una falla no se guarda ninguna.
        Devuelve el ID generado por la última instrucción (si lo hubo).
        """
        self.connection.ping(reconnect=True, attempts=3, delay=1)
        cursor = self.connection.cursor()
        try:
            for sql, params in statements:
                cursor.execute(sql, params)
            self.connection.commit()
            return cursor.lastrowid
        except Exception:
            self.connection.rollback()
            raise
        finally:
            cursor.close()


# -->
    # Metodo para ejecutar consultas personalizadas y devolver resultados como DataFrame
    def execute_pdSQL(self, sql, params=None) -> pd.DataFrame:         # pd.DataFrame o list[dict] 
        self._asegurar_conexion()
        df = pd.read_sql_query(sql, self.connection, params=params)    # pd.DataFrame
        # lista: list[dict] = df.to_dict(orient="records")             # list[dict]
        return df


    def listarEmployee(self) -> list[Employee]:
        self._asegurar_conexion()
        cursor = self.connection.cursor(dictionary=True)
        sql = f"""
SELECT {COLUMNS} FROM employees
        """
        try:
            cursor.execute(sql) 
            rows = cursor.fetchall()
            return [self._to_employee(row) for row in rows]
            #return [Employee(row["employeeID"], row["last_name"], row["first_name"], row["birth_date"], row["hire_date"])
            #    for row in rows
            #]
        finally:
            cursor.close()

    @staticmethod
    def _to_employee(row: dict) -> Employee:
        return Employee(
            employeeID=row["employeeID"],
            last_name=row["last_name"],
            first_name=row["first_name"],
            birth_date=row["birth_date"],
            hire_date=row["hire_date"],
        )

# <--


def main():
    db = Database(get_db_config())
    try:
        '''
        print()
        sql = "delete FROM employees WHERE employeeID =  %s"
        # conteo = db.execute_abc(sql, (12,))
        conteo, id = db.execute_abc(sql, (12,))
        print("No. de registros borrados:", conteo)

        sql = "SELECT * FROM employees"
        df = db.execute_select(sql)
        print(df)
        '''
        print()
        sql = "SELECT * FROM employees WHERE year(hire_date) =  %s"
        # df = db.execute_select(sql,  (1992,))
        df = db.execute_pdSQL(sql, (1992,))  # Mensaje: UserWarning
        print(df)


        print()
        lista = db.listarEmployee()
        print(" ID  Last_Name    first_name     Fecha_Nac    Fecha_Contratacion")
        for emp in lista:
            print(f"{emp.employeeID:>3} {emp.last_name:<20}")
            #print(f"El sueldo es: {sueldo:^15,.2f}")
    finally:
        db.close()


if __name__ == "__main__":
    os.system("cls")
    main()
    print("\n. . . H e c h o")
