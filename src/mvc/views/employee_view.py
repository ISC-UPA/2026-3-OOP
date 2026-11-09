from datetime import datetime
from src.mvc.models.employee import Employee

class EmployeeView:
    def menu_Employee() -> None:
        print('''
========== Menu de Empleados ==========
1. Alta
2. Baja
3. Cambio
4. Consulta
5. Listado
6. Query
0. Salir
======================================='''
        )

    def alta_employees() -> Employee:
        print("Alta de empleado")
        LastName = input("Ingrese el apellido del empleado: ")
        FirstName = input("Ingrese el nombre del empleado: ")
        birth_date_str = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
        hire_date_str = input("Ingrese la fecha de contratación (YYYY-MM-DD): ")    
        empleado = Employee(
            employee_id=0,  # Se asignará automáticamente en el controlador
            last_name=LastName,
            first_name=FirstName,
            birth_date= datetime.strptime(birth_date_str, "%Y-%m-%d").date(),
            hire_date= datetime.strptime(hire_date_str, "%Y-%m-%d").date()
        )    
        return empleado
    
      
    

