import os, sys
from dataclasses import dataclass
from datetime import date 

@dataclass
class Employee:
    
    def __init__(self, employeeID: int, last_name: str, first_name: str, birth_date: date, hire_date: date):
        self.employeeID = employeeID
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.hire_date = hire_date

    def __str__(self) -> str:
        return (
            f"employeeID: {self.employeeID} | "
            f"Apellido: {self.last_name} | "
            f"Nombre: {self.first_name}  | "
            f"Nacimiento: {self.birth_date}"
    )

def main():
    employee = Employee(20, "Lopez", "Jenifer", "2000-01-02", "2010-11-12")
    print(employee)
    print(employee.birth_date)

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
    print("\n. . . H e c h o")



    