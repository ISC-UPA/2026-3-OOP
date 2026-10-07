import os
from datetime import date
from abc import ABC, abstractmethod

#Clase: Molde para crear objetos, define atributos y metodos
#Objeto: Instancia de una clase, aquello que tiene nombre y apellido|

# 4 Pilares de POO
# Herencia:       Metodos que ya existen por parte de la clase padre
# Encapsulacion:  saldo cambia solo por depositar() y retirar()
# Abstraccion:    Calcular_impuesto() no importa el como, sino el resultado
# Polimorfismo:   Acelerar, funciona distinto entre una bici y un coche

# Alta cohesion:     Relacion entre los elementos de un modulo
#                    Alta: Tarea unica y bien definida
# Bajo acoplamiento: Dependencia entre dos modulos.
#                    Debil o bajo indica que no existe dependencia

# Palabras clave:
# Es un: Herencia
# Tiene un: Atributo tipo Clase

#class Persona(object):
#class Persona(ABC):
class Persona:
    # Atributo de clase
    conteo = 0  # Numero de personas
 
    def __init__(self, nombre, sexo: bool, nacimiento: date): #Constructor=Inicializar propiedaes  
        #  _sexo: Atributo protegido
        # __sexo: Atributo privado
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.nombre = nombre
        self._sexo = sexo
        self.nacimiento = nacimiento
        Persona.conteo += 1
    
    #def __str__(self):  # Evitar ver la direccion de memoria
        #return f"Nombre: {self.nombre}, Sexo: {'H' if self._sexo else 'M'}"

    def getSexo(self):
        return "Hombre" if self._sexo else "Mujer"

    def setSexo(self, value):
        self._sexo = value

    #@staticmethod    # Metodo de Clase
    #@abstractmethod  # Si hay un método abstracto, la clase debe ser abstracta
    def calcularEdad(birthdate) -> int:
        pass
        edad = date.today().year - birthdate.year
        return edad
    
    def info(self):
        edad = Persona.calcularEdad(self.nacimiento)
        return f"Nombre: {self.nombre}, Sexo: {self.getSexo()}, Nacimiento: {self.nacimiento}, Edad: {edad}"

    def _restarPersona(): # Metodo de clase protegido, se puede llamar desde la clase y subclases
        Persona.conteo -= 1
        
    def __subtractPersona(): # Metodo de clase privado, solo se puede llamar desde la clase
        Persona.conteo -= 1        
        
    def descontarPersona():
        Persona.__subtractPersona()
       
def esBisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    ano = 1999
    dia = 29 if esBisiesto(ano) else 28
    p1 = Persona("Juan", True, date(ano, 2, dia))
    print(f"Conteo de personas: {Persona.conteo}")
    print(p1)
    print(p1.info())
    
    print(f"Nombre: {p1.nombre}")
    # print(f"Sexo: {p1.__sexo}")   # Error: Atributo privado
    print(f"Sexo: {p1.getSexo()}")
    print(f"Bisiesto: {esBisiesto(p1.nacimiento.year)}")
    
    p1.setSexo(False)
    print(f"Sexo actualizado: {p1.getSexo()}")

    personas = [
        Persona("Jesus", True, date.fromisoformat("1950-12-15")),
        Persona("Maria", False, date.strptime("2020-3-03" , "%Y-%m-%d")),
    ] 
    personas.append(Persona("Jose", True,  date(2018, 2, 28)))
    
    #del personas[1]   
    personas = [p for p in personas if p.nombre != "Maria"]
    Persona._restarPersona()     
    #Persona.__subtractPersona() # Error
    #Persona.descontarPersona()   
    print(f"\nConteo de personas-->: {Persona.conteo}") 
    
    print(f"\n{'Nombre':<10} {'Sexo':<6} {'Nacimiento'} {'Edad':>5}")
    for p in personas:
        print(f"{p.nombre:<10} {p.getSexo():<6} {p.nacimiento} {Persona.calcularEdad(p.nacimiento):>5}")
    print(f"\nConteo de personas: {Persona.conteo}")
    
    print(f"Tipo de p1: {type(p1)}")
    print(f"¿p1 es una instancia de Persona? {isinstance(p1, Persona)}")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
    print("\n. . . H e c h o . . .")
    