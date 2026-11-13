import os
import sys
from pathlib import Path

# Add the project root so this file can also be run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from src.mvc.repositories.employee_repository import EmployeeRepository
from src.mvc.views.employee_view import EmployeeView
from src.mvc.repositories.database_oop import DatabaseConnection

class EmployeeController:
    def __init__(self, repository: EmployeeRepository, view: EmployeeView) -> None:
        self.repository = repository
        self.view = view

    def showEmployee(self, id=0): # pudiera omitirse el id
        self.view.showMessage("Consulta de un Empleado")
        id = input("Ingrese el ID: ")
        employee = self.repository.showEmployee(id)
        if employee:
            self.view.showEmployee(employee)
        else:
            self.view.showError(f'Empleado con ID: {id} No Existe')

    def listEmployee(self):
        lista = self.repository.listEmployee()        
        self.view.listEmployee(lista)

    def pdContratadosMenores(self, edad):
        df = self.repository.pdContratadosMenores(edad)
        print(f"Contratados menores a {edad} años")
        print(df)


    def insertEmployee(self, modelEmpleado):
        id = self.repository.insertEmployee(modelEmpleado)
        self.view.showMessage(f"Empleado: {id} dado de Alta")
        
    def insertarEmployee(self):
        employee = self.view.insertEmployee()
        if not employee.last_name:
            self.view.showError("Nombre Obligatorio")
            return
        id = self.repository.insertEmployee(employee)
        if id:
            self.view.showMessage(f"Empleado con ID {id}: dado de Alta")


    def deleteEmployee(self, id=0):  # pudiera omitirse el id
        self.view.showMessage("Baja de Empleados")
        id = input("Ingrese el ID: ")
        conteo = self.repository.deleteEmployee(id)
        if conteo:
            self.view.showMessage(f"Empleado ID: {id} dado de baja")
        else:
            self.view.showError(f'Empleado con ID: {id} No Existe')

   
    def updateEmployee(self, id=0):   # pudiera omitirse el id
        self.view.showMessage("Cambios en el Empleado")
        id = input("Ingrese el ID: ")
        employee = self.repository.showEmployee(id)
        if employee:
            self.view.showEmployee(employee)
            updated_employee = self.view.updateEmployee(employee)
            conteo = self.repository.updateEmployee(updated_employee)
            self.view.showMessage(f"Empleado ID: {id} Modificado")
        else:
            self.view.showError(f'Empleado con ID: {id} No Existe')        
                        
        
def main():
    db = DatabaseConnection()
    repository = EmployeeRepository(db)
    view = EmployeeView()
    controller = EmployeeController(repository, view)

    controller.showEmployee()
    controller.listEmployee()
    controller.pdContratadosMenores(25)

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
    print("\n. . . H e c h o")

