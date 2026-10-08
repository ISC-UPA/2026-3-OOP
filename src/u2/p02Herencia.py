import os
from datetime import date
from p01Clase import Persona
from p03Tiene import CuentaBancaria

'''
try:
    from .p01Clase import Persona
    from .p03Tiene import CuentaBancaria
except ImportError:
    from p01Clase import Persona
    from p03Tiene import CuentaBancaria
'''

class Estudiante(Persona):
    def __init__(self, nombre, sexo, nacimiento, carrera):
        super().__init__(nombre, sexo, nacimiento)
        self.carrera = carrera

    def trabajar(self):
        return f"{self.nombre} está estudiando {self.carrera}."

    def info(self):
        edad = Persona.calcularEdad(self._nacimiento)
        return f"Nombre: {self.nombre}, Sexo: {self.getSexo()}, Nacimiento: {self._nacimiento}, Edad: {edad}, Carrera: {self.carrera}"
class Empleado(Persona):
    def __init__(self, nombre, sexo, nacimiento, puesto, salario):
        super().__init__(nombre, sexo, nacimiento)
        self.puesto = puesto
        self._salario = salario
        self.cuenta = CuentaBancaria(nombre)

    def trabajar(self):
        return f"{self.nombre} está trabajando como {self.puesto}."

    def info(self):
        edad = Persona.calcularEdad(self._nacimiento)
        return f"Nombre: {self.nombre}, Sexo: {self.getSexo()}, Nacimiento: {self._nacimiento}, Edad: {edad}, Puesto: {self.puesto}, Salario: {self._salario}"


def main():
   # DRY (Don't Repeat Yourself)
    print("Subclases:", Persona.__subclasses__())
    print("Clase Padre:", Empleado.__bases__)
    print("MRO o Method Order Resolution:", Empleado.__mro__)
    print("Es subclase de Persona:", issubclass(Empleado, Persona))

    lista =[]
    lista.append(Estudiante("Luis", True, date(2000, 8, 20), "Ingeniería"))
    lista.append(Empleado("Ana", False, date(1990, 5, 15), "Gerente", 50000))
    print(f"\nConteo de personas: {Persona.conteo}")

    for p in lista:
        print(p.info())
 
    print("\nPolimorfismo: mismo método, distinto comportamiento según la clase")
    for p in lista:
        print(p.trabajar())
        
    print(lista[1].cuenta)
    print(f"Saldo actual: ${lista[1].cuenta.getSaldo():,.2f}")
    

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
    print("\n. . . H e c h o . . .")
        

