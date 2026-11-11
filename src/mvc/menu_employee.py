import os, sys
from pathlib import Path

# Add the project root so this file can also be run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.mvc.repositories.database_oop import DatabaseConnection
from src.mvc.controllers.employee_controller import EmployeeController
from src.mvc.repositories.employee_repository import EmployeeRepository
from src.mvc.views.employee_view import EmployeeView

def menuEmployee() -> None:
    db = DatabaseConnection()
    repository = EmployeeRepository(db)
    view = EmployeeView()
    controller = EmployeeController(repository, view)
    
    '''
    # Alta
    employeeModel = view.insertEmployee()
    controller.insertEmployee(employeeModel)
    '''
    # controller.insertarEmployee()
    '''
    # Baja
    print("Baja de empleado")
    id = input("Ingrese el ID: ")
    controller.deleteEmployee(id)
    '''
    # controller.deleteEmployee()
    # controller.showEmployee()
    # controller.updateEmployee()
    # controller.pdContratadosMenores(25)

    while True:
        view.menuEmployee()
        option = input("Seleccione una opción: ")
        if option == "1":   # Altas
            employeeModel = view.insertEmployee()
            controller.insertEmployee(employeeModel)  
            # controller.insertarEmployee()          
        elif option == "2": # Bajas
            controller.deleteEmployee()
        elif option == "3": # Cambios
            controller.updateEmployee()            
        elif option == "4": # Consultas
            controller.showEmployee()
        elif option == "5": # Listado
            controller.listEmployee()
        elif option == "6": # Query
            edad = input("Dame la edad: ")
            controller.pdContratadosMenores(edad)
        elif option == "0":
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
    db.close()



if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    menuEmployee()
    print("\n. . . H e c h o")

