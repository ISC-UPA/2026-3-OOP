import os
from datetime import date
from random import randint

class Persona:
    def __init__(self, nombre, sexo:bool, salario:float, nacimiento:date): # Constructor: Inicializar
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not isinstance(nacimiento, date):
            raise TypeError("La fecha de nacimiento debe ser un objeto date.")
        self.nombre = nombre
        self.sexo = sexo
        self.sueldo = salario
        self.nacimiento = nacimiento
        # self.edad = date.today().year - nacimiento.year

    def __str__(self): # En vez de mostrar la dirección de memoria, muestra la información de la persona
        return f"Persona(nombre={self.nombre}, sexo={'Hombre' if self.sexo else 'Mujer'})"
   
    def saludar(self):
        texto = f'''
        Mi nombre es {self.nombre} y tengo {self.edad} años. 
        Mi sueldo es {self.sueldo} y nací el {self.nacimiento}. 
        {'El es Hombre' if self.sexo else 'Ella es Mujer'}'''
        print(texto)
        
    @staticmethod  # Decorador: Método estático, no necesita self
    def numero_aleatorio(min_val, max_val=100):
        return randint(min_val, max_val)    

    def calcular_edad(self) -> int: # Tarea: completar metodo para que retorne la edad
        pass
    
def esBisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    p1 = Persona("Jesus", True, 5000, date(1990, 5, 15))
    p2 = Persona("María", False, "seis mil", date(1985, 8, 22)) 
    p1.saludar()
    p2.saludar()
    print(p1)
    print(f"p1.nombre: {p1.nombre}")
    print(Persona.numero_aleatorio(1, 10))
    print(f"esBisiesto(2020): {esBisiesto(2020)}")
    
    personas = [
        Persona("Jesus", True, 60000, date.fromisoformat("1950-12-15")),
        Persona("Maria", False, 70000, date.strptime("2010-3-03" , "%Y-%m-%d")),
        Persona("Jose", True, 8000,  date(1990, 2, Persona.numero_aleatorio(1, 28)))
    ] # Tarea: Imprime la información de cada persona de manera tabular
      #        Nombre   Sexo    Sueldo  Nacimiento      Edad
      #        --------  ------  ------  --------------  ----
      #       Jesus     Hombre  60000   1950-12-15      73
      #       Maria     Mujer    7000   2010-03-03      13
    
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
    print("\n. . . H e c h o . . .\n")
    