import os
from datetime import date

class Persona:
    def __init__(self, nombre, sexo:bool, salario:float, nacimiento:date): # Constructor:Inicializar
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not isinstance(nacimiento, date):
            raise TypeError("La fecha de nacimiento debe ser un objeto date.")
        self.nombre = nombre
        self.sexo = sexo
        self.sueldo = salario
        self.nacimiento = nacimiento
        self.edad = date.today().year - nacimiento.year
        pass


def main():
    pass

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
    print("\n. . . H e c h o . . .\n")
    