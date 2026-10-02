import os
from datetime import date

class Persona:
    def __init__(self, nombre, sexo:bool,  salario:float, nacimiento:date):  # Constructor: Inicializar los atributos
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not isinstance(nacimiento, date):
            raise TypeError("La fecha de nacimiento debe ser un objeto date.")

        self.nombre = nombre
        self.sexo = sexo
        self.sueldo = salario
        self.nacimiento = nacimiento
        self.edad = date.today().year - nacimiento.year

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años. El es {'Hombre' if self.sexo else 'Mujer'}")


def main():
    p1 = Persona("Juan", True, 50000.0, date(1990, 5, 15))
    p1.saludar()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n. . . H e c h o . . .\n")
    