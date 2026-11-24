import os, sys
from pathlib import Path

# Add the project root so this file can also be run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.config import get_db_config
from src.mvc.repositories.database import Database
from src.mvc.controllers.employee_controller import EmployeeController
from src.mvc.repositories.employee_repository import EmployeeRepository
from src.mvc.views.employee_view import EmployeeView


def menuEmployee() -> None:
    db = Database(get_db_config())
    repository = EmployeeRepository(db)
    view = EmployeeView()
    controller = EmployeeController(repository, view)
    
    '''
    # Alta
    employeeModel = view.insert()
    controller.insert(employeeModel)
    '''
    # controller.insertar()

    # controller.delete()
    # controller.show()
    # controller.update()
    # controller.pdContratados()

    while True:
        option = view.menu()
        if option == "1":   # Altas
            controller.insert()          
        elif option == "2": # Bajas
            controller.delete()
        elif option == "3": # Cambios
            controller.update()            
        elif option == "4": # Consultas
            controller.show()
        elif option == "5": # Listado
            controller.list_all()
        elif option == "6": # Query
            controller.pdContratados()
        elif option == "0":
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")



if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    menuEmployee()
    print("\n. . . H e c h o")
