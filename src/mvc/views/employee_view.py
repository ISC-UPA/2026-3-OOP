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
        #return {"employeeID": 0, "last_name":last_name, "first_name":first_name, "birth_date":birth_date, "hire_date":hire_date}  # dict
    #3
    def update(self, employee:Employee) -> Employee | dict:
        print("Dejar en blanco para no cambiar")
        print(f"Cambiar empleado ID: {employee.employeeID}")

        new_last_name = input(f"Apellido {employee.last_name}: ").strip()
        new_first_name = input(f"Nombre   {employee.first_name}: ").strip()
        new_birth_date = input(f"Fecha Nacimiento   {employee.birth_date}: ").strip()
        new_hire_date = input(f"Fecha Contratacion {employee.hire_date}: ").strip()

        last_name = new_last_name or employee.last_name
        first_name = new_first_name or employee.first_name

        try:
            birth_date = (
                datetime.strptime(new_birth_date, "%Y-%m-%d").date()
                if new_birth_date
                else employee.birth_date
            )
            hire_date = (
                datetime.strptime(new_hire_date, "%Y-%m-%d").date()
                if new_hire_date
                else employee.hire_date
            )
        except ValueError as error:
            raise ValueError("Las fechas deben tener el formato YYYY-MM-DD") from error

        #return Employee(employee.employeeID, last_name, first_name, birth_date, hire_date, )
        return {"employeeID": employee.employeeID, "last_name":last_name, "first_name":first_name, "birth_date":birth_date, "hire_date":hire_date}  # dict

    def upsert(self, current: Employee | None = None) -> dict:
        """Pide los datos del empleado. En un cambio, Enter conserva el valor actual."""
        if current:
            print("Enter conserva el valor actual")        
            print(f"Cambios en empleado ID: {current.employeeID}")
            employeeID = current.employeeID
            new_last_name = input(f"Apellido {current.last_name}: ").strip()
            new_first_name = input(f"Nombre   {current.first_name}: ").strip()
            new_birth_date = input(f"Fecha Nacimiento   {current.birth_date}: ").strip() 
            new_hire_date = input(f"Fecha Contratacion {current.hire_date}: ").strip()
        else:
            employeeID = 0
            new_last_name =  input(f"Apellido: ").strip()
            new_first_name = input(f"Nombre :  ").strip()
            new_birth_date = input(f"Fecha Nacimiento:   ").strip()
            new_hire_date =  input(f"Fecha Contratacion: ").strip()

        last_name  = new_last_name  or current.last_name
        first_name = new_first_name or current.first_name
        birth_date = str(new_birth_date or current.birth_date)
        hire_date  = str(new_hire_date  or current.hire_date)

        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
        hire_date  = datetime.strptime(hire_date,  "%Y-%m-%d").date()
        return {"employeeID": employeeID, "last_name":last_name, "first_name":first_name, "birth_date":birth_date, "hire_date":hire_date}  # dict
       

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
            print(" ID last_name    first_name  Fecha_Nac Fecha_Contratacion")
            for emp in employees:
                birth_date = emp.birth_date
                hire_date = emp.hire_date
                if isinstance(birth_date, str):
                    birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
                if isinstance(hire_date, str):
                    hire_date = datetime.strptime(hire_date, "%Y-%m-%d").date()
                print(
                    f"{emp.employeeID:>3} {emp.last_name:<12} {emp.first_name:<10}  "
                    f"{birth_date.strftime('%Y-%m-%d')}  {hire_date.strftime('%d-%m-%Y')}"
                )
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

        
      
    
