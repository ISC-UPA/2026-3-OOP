import os
from dataclasses import dataclass
from datetime import date

# En la DB.employees el atributo se llama employeeID,
# Por lo tanto, no es necesario que se llame igual en la Clase Employee
# pero poner atencion al metodo del repositorio    _to_employee

@dataclass
class Employee:
    last_name: str
    first_name: str
    birth_date: date
    hire_date: date
    employeeID: int | None = None

    def __post_init__(self) -> None:
        if not self.last_name.strip():
            raise ValueError("El apellido es obligatorio")
        if not self.first_name.strip():
            raise ValueError("El nombre es obligatorio")
        if self.birth_date >= self.hire_date:
            raise ValueError("La fecha de nacimiento debe ser anterior a la de contratación")

def main():
    employee = Employee("Lopez", "Jenifer", date.fromisoformat("2000-01-02"), date.fromisoformat("1990-11-12"), 20)
    print(employee)
    print(employee.birth_date)

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
    print("\n. . . H e c h o")

