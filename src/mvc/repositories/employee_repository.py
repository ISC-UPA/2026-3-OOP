import os, sys
import pandas as pd

from pathlib import Path
# Add the project root so this file can also be run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from src.mvc.models.employee import Employee
from src.config import get_db_config
from src.mvc.repositories.database import Database

COLUMNS = "employeeID, last_name, first_name, DATE(birth_date) AS birth_date, DATE(hire_date) AS hire_date"

class EmployeeRepository:
    def __init__(self, database: Database) -> None:
        self.db = database

    #1
    def insert(self, employee: Employee) -> int:
        sql = """
            INSERT INTO employees (last_name, first_name, birth_date, hire_date) 
            VALUES (%s, %s, %s, %s)
        """
        _, new_id = self.db.execute_abc(sql, (employee.last_name, employee.first_name, employee.birth_date, employee.hire_date))
        return new_id
    
    #2
    def delete(self, id: int | str) -> int:
        sql = "DELETE FROM employees WHERE EmployeeID = %s"
        conteo, _ = self.db.execute_abc(sql, (int(id),))
        return conteo

    #3
    def update(self, employee: Employee) -> int:
        sql = """
            UPDATE employees
               SET last_name = %s, first_name = %s, birth_date = %s, hire_date = %s
            WHERE EmployeeID = %s
        """
        parametros = (employee.last_name, employee.first_name, employee.birth_date, employee.hire_date, employee.employeeID,)
        conteo, _ = self.db.execute_abc(sql, (parametros))        
        return conteo
   
    #3 largo
    def actualizar(self, employee: Employee) -> int:
        sql = """
            UPDATE employees
            SET last_name = %s, first_name = %s, birth_date = %s, hire_date = %s
            WHERE EmployeeID = %s
        """
        parametros = (employee.last_name, employee.first_name, employee.birth_date, employee.hire_date, employee.employeeID,)
        self.db._asegurar_conexion()
        cursor = self.db.connection.cursor()
        try:
            cursor.execute(sql, parametros) 
            self.db.connection.commit()
            return cursor.rowcount
        except Exception:
            self.db.connection.rollback()
            raise
        finally:
            cursor.close()

    #4 
    def show(self, id: int | str = 0) -> Employee | None:
        sql = f"""SELECT {COLUMNS} FROM employees WHERE EmployeeID = %s """
        rows = self.db.execute_select(sql, (id,))
        return self._to_employee(rows[0]) if rows else None   # No importa el orden de los atributos  

    #4 largo 
    def mostrar(self, id: int | str = 0) -> Employee | None:
        sql = f"""SELECT {COLUMNS} FROM employees WHERE EmployeeID = %s """
        self.db._asegurar_conexion()
        cursor = self.db.connection.cursor(dictionary=True)
        try:
            cursor.execute(sql, (int(id),))
            row = cursor.fetchone()    # si son varios fetchall()
        finally:
            cursor.close()
        if row is None:
            return None
        #return self._to_employee(row) # No importa el orden 
        return Employee(
            row["employeeID"],
            row["last_name"],
            row["first_name"],
            row["birth_date"],
            row["hire_date"],
        ) # El orden en base al Model

    #5
    def list_all(self) -> list[Employee]:   # funciona con la validacion
        sql = f"SELECT {COLUMNS} FROM employees"
        #sql = f"SELECT {COLUMNS} FROM employees where year(hire_date) = %s"
        rows = self.db.execute_select(sql)
        #rows = self.db.execute_select(sql, (1992,))
        return [self._to_employee(row) for row in rows]        

    #6
    def pdContratados(self, edad: int | str) -> pd.DataFrame:
        sql = f"""
SELECT {COLUMNS}
FROM employees
WHERE TIMESTAMPDIFF(YEAR, birth_date, hire_date) < %s
        """
        rows = self.db.execute_select(sql,(edad,))
        return pd.DataFrame(rows)


    @staticmethod
    def _to_employee(row: dict) -> Employee:
        return Employee(        # No importa el orden de los atributos
            employeeID=row["employeeID"],
            last_name=row["last_name"],
            first_name=row["first_name"],
            birth_date=row["birth_date"],
            hire_date=row["hire_date"],
        )


def main() -> None:
    db = None
    try:
        db = Database(get_db_config())
        repository = EmployeeRepository(db)

        employee = repository.show(9)            
        print(employee)

        '''
        print()
        lista = repository.list_all()
        print(" ID  Last_Name    first_name     Fecha_Nac    Fecha_Contratacion")
        for emp in lista:
            print(f"{emp.employeeID:>3} {emp.last_name:<20}")
        ''' 
        
        print()
        df = repository.pdContratados(25)
        print(df)

    finally:
        if db is not None:
            db.close()


if __name__ == "__main__":
    os.system("cls")
    main()
    print("\n. . . H e c h o")
