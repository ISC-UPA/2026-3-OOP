import os, sys
from pathlib import Path
from datetime import datetime

# Add the project root so this file can also be run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from src.mvc.models.employee import Employee

class EmployeeView:

    @staticmethod
    def menuEmployee() -> None:
        print('''
========== Menu de Empleados ==========
1. Altas
2. Bajas
3. Cambios
4. Consultas
5. Listado
6. Query
0. Salir
======================================='''
        )

    @staticmethod
    def showEmployee(employee: Employee) -> None:
        if employee:
            print(f'''
ID:       {employee.employeeID}
Apellido: {employee.last_name}
Nombre:   {employee.first_name}
Fecha de nacimiento:   {employee.birth_date}
Fecha de contratación: {employee.hire_date}      
         ''')
            
            #print(f"ID: {employee.employeeID}")
            #print(f"Apellido: {employee.last_name}")
            #print(f"Nombre: {employee.first_name}")
            #print(f"Fecha de nacimiento:   {employee.birth_date}")
            #print(f"Fecha de contratación: {employee.hire_date}")
        else:
            print("Empleado no encontrado.")

    @staticmethod
    def listEmployee(employees: list[Employee]) -> None:
        if employees:
            print("Listado de Empleados")
            print(" ID last_name    first_name     Fecha_Nac    Fecha_Contratacion")
            for employee in employees:
                print(f"{employee.employeeID:>3} {employee.last_name:<20}")
                #print(f"El sueldo es: {sueldo:^15,.2f}")
        else:
            print("No existen empleados")


    @staticmethod
    def insertEmployee() -> Employee:
        print("Alta de empleado")
        last_name =  input("Ingrese el apellido del empleado: ")
        first_name = input("Ingrese el nombre del empleado:   ")
        birth_date = input("Ingrese la fecha de nacimiento (YYYY-MM-DD):   ")
        hire_date =  input("Ingrese la fecha de contratación (YYYY-MM-DD): ")
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
        hire_date =  datetime.strptime(hire_date, "%Y-%m-%d").date()

        empleado = Employee(0, last_name, first_name, birth_date, hire_date)
        return empleado

    @staticmethod
    def updateEmployee(employee:Employee) -> Employee:
        if employee:
            print("Cambios en el empleado")
            print(f"ID: {employee.employeeID}")

            print(f"Apellido actual: {employee.last_name}")
            new_last_name = input("Ingrese el nuevo apellido (dejar en blanco para no cambiar): ")
            if new_last_name:
                employee.last_name = new_last_name

            print(f"Fecha de nacimiento actual: {employee.birth_date}")
            new_birth_date = input("Ingrese la nueva fecha de nacimiento (YYYY-MM-DD) (dejar en blanco para no cambiar): ")
            if new_birth_date:
                employee.birth_date=  datetime.strptime(new_birth_date, "%Y-%m-%d").date()
        else:
            print("Empleado no encontrado.")
        return employee


    @staticmethod
    def showMessage(message):
        print(message)
        
    @staticmethod
    def showError(message):
        print("***" , message, "***")
        
def main():
    # EmployeeView.menuEmployee()
    employee = EmployeeView.insertEmployee()
    print(employee)

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
    print("\n. . . H e c h o")

        
      
    

