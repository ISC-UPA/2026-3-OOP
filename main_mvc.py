import os
import mysql.connector
from src.config import get_db_config

from src.mvc.repositories.database import Database
from src.mvc.repositories.employee_repository import EmployeeRepository
# from src.mvc.repositories.product_repository import ProductRepository

from src.mvc.views.main_view import MainView
from src.mvc.views.employee_view import EmployeeView
# from src.mvc.views.product_view import ProductView

from src.mvc.controllers.employee_controller import EmployeeController
# from src.mvc.controllers.product_controller import ProductController

from src.mvc.menu_employee import menuEmployee
#from src.mvc.menu_product  import menuProduct


def main() -> None:
    view = MainView()
    try:
        db = Database(get_db_config())
    except mysql.connector.Error as error:
        view.show_error(f"No se pudo conectar a la base de datos: {error}")
        return

    employeeController = EmployeeController(EmployeeRepository(db), EmployeeView())
    menus = {"1": employeeController.run,
             "2": menuEmployee}

    try:
        while True:
            os.system("cls")
            option = view.ask_option()  # Presenta MainMenu y captura opcion

            #''' Tipico:  Menu por cada Entidad
            if option == "1":
                employeeController.run() 
            elif option == "2":
                menuEmployee()
            elif option == "0":
                break
            else:
                print("Opción no válida. Intente nuevamente.")
            #'''

            ''' Avanzado: Por medio de los acciones del Controlador (base_controller)
            if option == "0":
                break
            menu = menus.get(option)
            if menu:
                menu()
            else:
                view.show_error("Opción no válida")
            '''

    finally:
        db.close() # Se cierra la DB


if __name__ == "__main__":
    os.system("cls")    
    main()
    print(". . . H e c h o")
