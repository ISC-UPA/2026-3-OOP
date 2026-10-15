import os
from typing import Optional

class Persona:
    _instancia = None
    #_instancia: Optional['Persona'] = None    
    #_inicializado = False

    # se ejecuta antes de crear la instancia
    # Se encarga de construir y devolver el objeto (normalmente una instancia de la clase).
    def __new__(cls, nombre, y):
        if cls._instancia is None:
            print("→ Entrando a __new__")
            cls._instancia = super().__new__(cls)   # aquí se crea el objeto
        return cls._instancia                       # se devuelve la instancia

    # Se ejecuta después de que el objeto ya fue creado por __new__.
    def __init__(self, nombre, edad):
        if not hasattr(self, "nombre"):
        #if not Persona._inicializado:            
            print("→ Entrando a __init__")
            self.nombre = nombre
            self.edad = edad
            #Persona._inicializado = True

    def info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

os.system("cls")
# Crear objeto
p1 = Persona("Carlos", 30)
print(p1)
p2 = Persona("Herrera", 31)
print(p2)
print(f"¿Es la misma conexión? {p1 is p2}")
print(f"Nombre: {p1.nombre}, Edad: {p1.edad}")
print(f"Nombre: {p2.nombre}, Edad: {p2.edad}")
print(p2.info())


