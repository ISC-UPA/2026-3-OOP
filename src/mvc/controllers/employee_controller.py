
import os
import sys
from dataclasses import replace

#'''
from pathlib import Path
# Add the project root so this file can also be run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from src.config import get_db_config
from src.mvc.repositories.database import Database
#'''

from src.mvc.models.employee import Employee
from src.mvc.repositories.employee_repository import EmployeeRepository
from src.mvc.views.employee_view import EmployeeView
from src.mvc.controllers.base_controller import BaseController

#class EmployeeController:
class EmployeeController(BaseController):
    def __init__(self, repository: EmployeeRepository, view: EmployeeView) -> None:
        #super().__init__(repository, view)
        self.repository = repository
        self.view = view
        #'''
        self.actions = {
            "1": self.insert,
            "2": self.delete,
            "3": self.update,
            "4": self.show,
            "5": self.list_all,
            "6": self.pdContratados,
        }
        #'''

    def insert(self) -> None: #1
        try:
            employee = self.view.insert()
            if not isinstance(employee, Employee):
                employee = Employee(**employee)
        except ValueError as error:  # el modelo rechazó los datos
            self.view.show_error(str(error))
            return        
        new_id = self.repository.insert(employee)
        self.view.show_message(f"Empleado con ID {new_id}: dado de Alta")

    def delete(self) -> None: #2
        employee = self._find_employee()
        if employee:
            conteo = self.repository.delete(employee.employeeID)        
            self.view.show_message(f"Empleado ID: {employee.employeeID} dado de baja")

    def update(self) -> None: #3
        employee = self._find_employee()
        if employee:
            self.view.show(employee)
            updated_employee = self.view.update(employee)
            conteo = self.repository.update(updated_employee)
            self.view.show_message(f"Empleado ID: {updated_employee.employeeID} Modificado")
        else:
            return

    def actualizar(self) -> None: #3
        # cadena.replace(viejo, nuevo)        
        employee = self._find_employee()
        if employee is None:
            return
        self.view.show(employee)
        new_dict = self.view.actualizar(employee)
        try:
            updated = replace(employee, new_dict)   # dataclasses 
        except ValueError as error:
            self.view.show_error(error)            
        conteo = self.repository.update(updated)
        self.view.show_message(f"Empleado ID: {id} Modificado")


    def show(self) -> None: #4
        employee = self._find_employee()
        if employee:
            self.view.show(employee)


    def list_all(self) -> None: #5
        lista = self.repository.list_all()        
        self.view.list_all(lista)

    def pdContratados(self) -> None: #6
        self.view.show_message("Empleados Contratados")
        edad = input("Ingrese la Edad: ")
        df = self.repository.pdContratados(edad)
        print(f"Contratados menores a {edad} años")
        print(df)

    def _find_employee(self) -> Employee | None:
        """Pide un ID y busca al empleado. Si no existe, avisa y devuelve None."""
        id = input("Ingrese el ID: ")
        employee = self.repository.show(id)
        if employee is None:
            self.view.show_error(f"El empleado {id} no existe")
        return employee


#'''        
def main():
    db = Database(get_db_config())
    repository = EmployeeRepository(db)
    view = EmployeeView()
    controller = EmployeeController(repository, view)

    #controller.show()
    controller.list_all()
    #controller.pdContratados()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
    print("\n. . . H e c h o")

#'''
