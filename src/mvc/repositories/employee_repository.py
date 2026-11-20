import os, sys
import pandas as pd
from pathlib import Path

# Add the project root so this file can also be run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from src.mvc.models.employee import Employee
from src.mvc.repositories.database_oop import DatabaseConnection

COLUMNS = "employeeID, last_name, first_name, DATE(birth_date) AS birth_date, DATE(hire_date) AS hire_date"

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

        #return self._to_employee(row) # No importa el orden 
        return Employee(
            row["employeeID"],
            row["last_name"],
            row["first_name"],
            row["birth_date"],
            row["hire_date"],
        ) # El orden en base al Model

    def listEmployee(self) -> list[Employee]:
        self.db._asegurar_conexion()
        cursor = self.db.connection.cursor(dictionary=True)
        sql = "SELECT employeeID, last_name, first_name, DATE(birth_date) AS birth_date, DATE(hire_date) AS hire_date FROM employees"
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()
        finally:
            cursor.close()
        return [self._to_employee(row) for row in rows]  # El orden no importa
        return [
            Employee(
                row["last_name"],
                row["first_name"],
                row["birth_date"],
                row["hire_date"],
                row["employeeID"],
            )
            for row in rows
        ] # El orden debe ser como este definido en el Model

    def listarEmployee(self) -> list[Employee]:   # funciona con la validacion
        sql = f"SELECT {COLUMNS} FROM employees"
        sql = f"SELECT {COLUMNS} FROM employees where year(hire_date) = %s"
        #rows = self.db.execute_select(sql)
        rows = self.db.execute_select(sql, (1992,))
        return [self._to_employee(row) for row in rows]        


    def pdContratadosMenores(self, edad: int | str) -> pd.DataFrame:
        self.db._asegurar_conexion()
        sql = f"""
SELECT {COLUMNS}
FROM employees
WHERE TIMESTAMPDIFF(YEAR, birth_date, hire_date) < %s
        """
        print(sql)
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

    def update(self, employee: Employee) -> None:
        sql = "UPDATE employees SET last_name = %s, first_name = %s, birth_date = %s, hire_date = %s WHERE employeeID = %s"
        parametros = (employee.last_name, employee.first_name, employee.birth_date, employee.hire_date, employee.employee_id ,)
        self.db.execute_abc(sql, parametros)

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
        db = DatabaseConnection()
        repositories = EmployeeRepository(db)

        employee = repositories.showEmployee(19)            
        print(employee)

        '''
        print()
        lista = repositories.listEmployee()
        print(" ID  Last_Name    first_name     Fecha_Nac    Fecha_Contratacion")
        for emp in lista:
            print(f"{emp.employeeID:>3} {emp.last_name:<20}")
        ''' 
        
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