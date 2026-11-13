import os, sys
import mysql.connector
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

# Add the project root so this file can also be run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
# sys.path.append(os.getcwd())
from src.mvc.models.employee import Employee

load_dotenv(Path(__file__).resolve().parents[3] / ".env", override=True)

class DatabaseConnection:
    """Singleton: una sola conexión MySQL compartida por todo el programa."""
    _instance = None

    # Se ejecuta antes de crear la instancia: construye y devuelve el objeto
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Evita re-inicializar la conexión cada vez que se llama DatabaseConnection()
        if not hasattr(self, "connection"):
            self.config = {
                "host": os.getenv("DB_HOST"),
                "port": int(os.getenv("DB_PORT")),
                "database": os.getenv("DB_NAME"),
                "user": os.getenv("DB_USER"),
                "password": os.getenv("DB_PASSWORD"),
            }
            self.connection = mysql.connector.connect(**self.config)
            self.cursor = self.connection.cursor(dictionary=True)  # resultados como dict

    def _asegurar_conexion(self):
        """Si la conexión se cayó, la restablece (sigue siendo la misma instancia)."""
        if not self.connection.is_connected():
            self.connection.reconnect(attempts=3, delay=1)
            self.cursor = self.connection.cursor(dictionary=True)

    def close(self):
        """Cierra la conexión y permite crear una nueva en el futuro."""
        if hasattr(self, "connection"):
            self.cursor.close()
            self.connection.close()
            del self.connection
            del self.cursor
        DatabaseConnection._instance = None

    # Metodo para ejecutar consultas personalizadas y devolver resultados como DataFrame
    def execute_pdSQL(self, sql, params=None) -> pd.DataFrame:
        self._asegurar_conexion()
        if params is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, params)
        return pd.DataFrame(self.cursor.fetchall())

    # Metodo para ejecutar consultas personalizadas y devolver resultados como DataFrame
    def execute_pd2SQL(self, sql, params=None) -> pd.DataFrame:
        self._asegurar_conexion()
        return pd.read_sql_query(sql, self.connection, params=params)

    # Metodo para ejecutar altas, bajas y cambios, y devolver el Numero de registros
    def execute_abc(self, sql, params=None) -> int:
        self._asegurar_conexion()
        if params is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, params)
        self.connection.commit()
        conteo = self.cursor.rowcount
        return conteo

# -->
    def listarEmployee(self) -> list[Employee]:
        self._asegurar_conexion()
        sql = """
            SELECT employeeID, last_name, first_name, birth_date, hire_date 
            FROM employees
        """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return [Employee(row["employeeID"], row["last_name"], row["first_name"], row["birth_date"], row["hire_date"])
            for row in rows
        ]

# <--

def main():
    db = DatabaseConnection()
    try:
        sql = "SELECT * FROM employees"
        df = db.execute_pdSQL(sql)
        print(df)

        print()
        sql = "SELECT * FROM employees WHERE year(hire_date) =  %s"
        # df = db.execute_pdSQL(sql,  (1992,))
        df = db.execute_pd2SQL(sql, (1992,))  # Mensaje: UserWarning
        print(df)
        
        print()
        sql = "delete FROM employees WHERE employeeID =  %s"
        conteo = db.execute_abc(sql, (10,))
        print("No. de registros borrados:", conteo)
        
        print()
        lista = db.listarEmployee()
        print(" ID  Last_Name    first_name     Fecha_Nac    Fecha_Contratacion")
        for employee in lista:
            print(f"{employee.employeeID:>3} {employee.last_name:<20}")
            #print(f"El sueldo es: {sueldo:^15,.2f}")
    finally:
        db.close()


if __name__ == "__main__":
    os.system("cls")
    main()
    print("\n. . . H e c h o")
