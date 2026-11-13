import os, sys
import pandas as pd
from pathlib import Path

# Add the project root so this file can also be run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from src.mvc.models.employee import Employee
from src.mvc.repositories.database_oop import DatabaseConnection

class EmployeeRepository:
    def __init__(self, database: DatabaseConnection) -> None:
        self.db = database

    def showEmployee(self, id: int | str = 0) -> Employee | None:
        self.db._asegurar_conexion()
        sql = """
            SELECT EmployeeID AS employeeID, last_name, first_name, birth_date, hire_date
            FROM employees
            WHERE EmployeeID = %s
        """
        cursor = self.db.connection.cursor(dictionary=True)
        try:
            cursor.execute(sql, (int(id),))
            row = cursor.fetchone()
        finally:
            cursor.close()
        if row is None:
            return None

        return Employee(
            row["employeeID"],
            row["last_name"],
            row["first_name"],
            row["birth_date"],
            row["hire_date"],
        )

    def listEmployee(self) -> list[Employee]:
        self.db._asegurar_conexion()
        sql = "SELECT employeeID, last_name, first_name, birth_date, hire_date FROM employees"
        cursor = self.db.connection.cursor(dictionary=True)
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()
        finally:
            cursor.close()
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

    def pdContratadosMenores(self, edad: int | str) -> pd.DataFrame:
        self.db._asegurar_conexion()
        sql = """
            SELECT employeeID, last_name, first_name, birth_date, hire_date
            FROM employees
            WHERE TIMESTAMPDIFF(YEAR, birth_date, hire_date) < %s
        """
        cursor = self.db.connection.cursor(dictionary=True)
        try:
            cursor.execute(sql, (int(edad),))
            return pd.DataFrame(cursor.fetchall())
        finally:
            cursor.close()

    def insertEmployee(self, employee: Employee) -> int:
        self.db._asegurar_conexion()
        sql = """
            INSERT INTO employees (last_name, first_name, birth_date, hire_date) 
            VALUES (%s, %s, %s, %s)
        """
        cursor = self.db.connection.cursor()
        try:
            cursor.execute(
                sql,
                (
                    employee.last_name,
                    employee.first_name,
                    employee.birth_date,
                    employee.hire_date,
                ),
            )
            self.db.connection.commit()
            return cursor.lastrowid
        except Exception:
            self.db.connection.rollback()
            raise
        finally:
            cursor.close()

    def deleteEmployee(self, id: int | str) -> int:
        self.db._asegurar_conexion()
        sql = "DELETE FROM employees WHERE EmployeeID = %s"
        cursor = self.db.connection.cursor()
        try:
            cursor.execute(sql, (int(id),))
            self.db.connection.commit()
            return cursor.rowcount
        except Exception:
            self.db.connection.rollback()
            raise
        finally:
            cursor.close()

    def updateEmployee(self, employee: Employee) -> int:
        self.db._asegurar_conexion()
        sql = """
            UPDATE employees
            SET last_name = %s, first_name = %s, birth_date = %s, hire_date = %s
            WHERE EmployeeID = %s
        """
        cursor = self.db.connection.cursor()
        try:
            cursor.execute(
                sql,
                (
                    employee.last_name,
                    employee.first_name,
                    employee.birth_date,
                    employee.hire_date,
                    employee.employeeID,
                ),
            )
            self.db.connection.commit()
            return cursor.rowcount
        except Exception:
            self.db.connection.rollback()
            raise
        finally:
            cursor.close()


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
        df = repositories.pdContratadosMenores(25)
        print(df)

    finally:
        if db is not None:
            db.close()


if __name__ == "__main__":
    os.system("cls")
    main()
    print("\n. . . H e c h o")