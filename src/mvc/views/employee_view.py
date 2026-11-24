import os, sys
from pathlib import Path
from datetime import datetime

# Add the project root so this file can also be run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from src.mvc.models.employee import Employee
from src.mvc.views.base_view import BaseView

class EmployeeView(BaseView):

    #@staticmethod
    def menu(self) -> str:
        print('''
======= Menu de Empleados ========
1. Altas
2. Bajas
3. Cambios
4. Consultas
5. Listado
6. Query Contratados de cierta edad
0. Regresar
======================================='''
        )
        return input("Seleccione una opción: ").strip()

    #1
    def insert(self) -> dict: #1     Employee | dict
        print("Alta de empleado")
        last_name =  input("Ingrese el apellido del empleado: ")
        first_name = input("Ingrese el nombre del empleado:   ")
        birth_date = input("Ingrese la fecha de nacimiento (YYYY-MM-DD):   ")
        hire_date =  input("Ingrese la fecha de contratación (YYYY-MM-DD): ")
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
        hire_date =  datetime.strptime(hire_date, "%Y-%m-%d").date()
   
        empleado = Employee(0, last_name, first_name, birth_date, hire_date)
        return empleado

    #3
    def update(self, employee:Employee) -> Employee:
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

    #3
    def actualizar(self, current: Employee ) -> dict:
        print("Actualizar empleado: ", current.employeeID)

        print(f"Apellido actual: {current.last_name}")
        new_last_name = input("Ingrese el nuevo apellido (dejar en blanco para no cambiar): ")        

        print(f"Nombre actual: {current.first_name}")
        new_first_name = input("Ingrese el nuevo Nombre (dejar en blanco para no cambiar): ")        

        print(f"Fecha de nacimiento actual: {current.birth_date}")
        new_birth_date = input("Ingrese la nueva fecha de nacimiento (YYYY-MM-DD) (dejar en blanco para no cambiar): ")

        print(f"Fecha de contratacion actual: {current.hire_date}")
        new_hire_date = input("Ingrese la nueva fecha  contratacion (YYYY-MM-DD) (dejar en blanco para no cambiar): ")

        return {
            "last_name": new_last_name,
            "first_name": new_first_name,
            "birth_date": new_birth_date,
            "hire_date" : new_hire_date,
        }

    #4
    def show(self, employee: Employee) -> None:
        print(f'''
ID:       {employee.employeeID}
Apellido: {employee.last_name}
Nombre:   {employee.first_name}
Fecha de nacimiento:   {employee.birth_date}
Fecha de contratación: {employee.hire_date}      
         ''')

    #5
    def list_all(self, employees: list[Employee]) -> None:
        if employees:
            print("Listado de Empleados")
            print(" ID last_name    first_name     Fecha_Nac    Fecha_Contratacion")
            for employee in employees:
                print(f"{employee.employeeID:>3} {employee.last_name:<12} {employee.first_name:<10}")
                #print(f"El sueldo es: {sueldo:^15,.2f}")
        else:
            print("No existen empleados")

        
def main():
    #EmployeeView.menuEmployee()
    view = EmployeeView()
    view.menuEmployee()
    
    
   
    employee1 = Employee(9, "Lopez", "Jennifer", "2000-01-02", "2010-11-12")
    employee2 = Employee(10, "Pitt", "Brad", "2010-01-02", "2025-09-10")
    #EmployeeView.show(employee1)
    view.showEmployee(employee1)

    lista = [employee1, employee2]
    #EmployeeView.list_all(lista)
    #view.list_all(lista)

    #employee = EmployeeView.insert()
    #print(employee)

    #employee_update = EmployeeView.update(employee2)
    #print(employee_update)
    

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
    print("\n. . . H e c h o")

        
      
    
