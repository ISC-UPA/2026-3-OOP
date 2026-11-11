import os
import sys
from pathlib import Path

import pandas as pd
from sqlalchemy import Null

# Add the project root so this file can also be run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from src.mvc.repositories.database_oop import DatabaseConnection
from src.mvc.models.employee import Employee

class EmployeeRepository:
    def __init__(self, database: DatabaseConnection) -> None:
        self.db = database

    def listEmployee(self) -> list[Employee]:
        self.db._asegurar_conexion()
        sql = "SELECT employeeID, last_name, first_name, birth_date, hire_date FROM employees"
        self.db.cursor.execute(sql)
        rows = self.db.cursor.fetchall()
        return [
            Employee(
                row["employeeID"],
                row["last_name"],
                row["first_name"],
                row["birth_date"],
                row["hire_date"],
            )
            for row in rows
        ]

    def pdEmployee(self) -> pd.DataFrame:
        self.db._asegurar_conexion()
        sql = "SELECT * FROM employees"
        self.db.cursor.execute(sql)
        return pd.DataFrame(self.db.cursor.fetchall())

    def pd2Employee(self) -> pd.DataFrame:
        self.db._asegurar_conexion()
        sql = "SELECT * FROM employees"
        return pd.read_sql_query(sql, self.db.connection, params=())  # Mensaje: UserWarning

    def pdContratadosMenores(self, edad) -> pd.DataFrame:
        self.db._asegurar_conexion()
        sql = '''
        select * from employees
        where year(hire_date) - year(birth_date) <= %s
        '''
        return self.db.execute_pdSQL(sql, (edad,))


    def showEmployee(self, id=0) -> Employee | None:
        self.db._asegurar_conexion()
        sql = "SELECT * FROM employees WHERE EmployeeID = %s"        
        cursor = self.db.connection.cursor()
        try:
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
        finally:
            cursor.close()
        if row:
            '''
            return Employee(
                employeeID=int(row[0]),
                last_name=str(row[1]),
                first_name=str(row[2]),
                birth_date=row[3],
                hire_date=row[4],
            )
            '''
            return Employee(int(row[0]),  str(row[1]), row[2], row[3], row[4] )
        else:
            return None


    def insertEmployee(self, employee:Employee) -> int:
        self.db._asegurar_conexion()
        sql = """
            INSERT INTO employees (last_name, first_name, birth_date, hire_date) 
            VALUES (%s, %s, %s, %s)
        """
        cursor = self.db.connection.cursor()
        try:
            cursor.execute(sql, (employee.last_name, employee.first_name, employee.birth_date, employee.hire_date,),)
            self.db.connection.commit()
            id_generado = cursor.lastrowid
            conteo = cursor.rowcount
        finally:
            cursor.close()
        return id_generado

    def deleteEmployee(self, id) -> int:
        self.db._asegurar_conexion()
        sql = "DELETE FROM employees WHERE EmployeeID = %s"
        cursor = self.db.connection.cursor()
        try:
            cursor.execute(sql, (id,))
            self.db.connection.commit()
            conteo = cursor.rowcount
        finally:
            cursor.close()        
        return conteo

    def updateEmployee(self, employee: Employee) -> int:
        self.db._asegurar_conexion()  
        sql = """
            UPDATE employees
            SET last_name = %s, first_name = %s, birth_date = %s, hire_date = %s
            WHERE EmployeeID = %s
        """
        cursor = self.db.connection.cursor()
        try:
            cursor.execute(sql, (
                employee.last_name,employee.first_name,employee.birth_date,employee.hire_date,employee.employeeID))
            self.db.connection.commit()
            conteo = cursor.rowcount
        finally:
            cursor.close()        
        return conteo
      
      
        
        
def main() -> None:
    db = None
    try:
        db = DatabaseConnection()
        repositories = EmployeeRepository(db)

        print()
        lista = repositories.listEmployee()
        print(" ID  Last_Name    first_name     Fecha_Nac    Fecha_Contratacion")
        for employee in lista:
            print(f"{employee.employeeID:>3} {employee.last_name:<20}")

        print()
        df = repositories.pdEmployee()
        print(df)

        print()
        df = repositories.pd2Employee()
        print(df)
    finally:
        if db is not None:
            db.close()


if __name__ == "__main__":
    os.system("cls")
    main()
    print("\n. . . H e c h o")