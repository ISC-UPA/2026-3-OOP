import os
from datetime import date
from random import randint, random

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

    def __str__(self):
        return f"Persona(nombre={self.nombre}, sexo={'Hombre' if self.sexo else 'Mujer'})"

    def saludar(self):
        texto = f'''
        Mi nombre es {self.nombre} y tengo {self.edad} años. 
        Mi sueldo es {self.sueldo} y nací el {self.nacimiento}. 
        El es {'Hombre' if self.sexo else 'Mujer'}'''
        print(texto)
    
    def numero_aleatorio(min, max=100):
        if (min > max):
            raise ValueError("El valor mínimo no puede ser mayor que el máximo")
        return randint(min, max)

def esBisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
        
        

def main():
    p1 = Persona("Juan", True, 50000.0, date(1990, 5, 15))
    p2 = Persona("María", False, 60000.0, date(1985, 8, 20))
    p1.saludar()
    p2.saludar()
    print(p1)
    print(Persona.numero_aleatorio(1, 10))
    print("El año 2020 es bisiesto:", esBisiesto(2020))
    
    
    

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
    print("\n. . . H e c h o . . .\n")
    