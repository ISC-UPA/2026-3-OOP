import os
from datetime import date
from p01Clase import Persona
from p03Tiene import CuentaBancaria

class Empleado(Persona):
    def __init__(self, nombre, sexo, nacimiento, puesto, salario):
        super().__init__(nombre, sexo, nacimiento)
        self.puesto = puesto
        self.salario = salario
        self.cuenta = CuentaBancaria(nombre)

    def trabajar(self):
        return f"{self.nombre} está trabajando como {self.puesto}."

    def info(self):
        edad = Persona.calcularEdad(self.nacimiento)
        return f"Nombre: {self.nombre}, Sexo: {self.getSexo()}, Nacimiento: {self.nacimiento}, Edad: {edad}, Puesto: {self.puesto}, Salario: {self.salario}"

class Estudiante(Persona):
    def __init__(self, nombre, sexo, nacimiento, carrera):
        self.nombre = nombre
        self._sexo = sexo
        self.nacimiento = nacimiento

        self.carrera = carrera

    def trabajar(self):
        return f"{self.nombre} está estudiando {self.carrera}."

    def info(self):
        edad = Persona.calcularEdad(self.nacimiento)
        return f"Nombre: {self.nombre}, Sexo: {self.getSexo()}, Nacimiento: {self.nacimiento}, Edad: {edad}, Carrera: {self.carrera}"
    

def main():
    p1 = Empleado("Ana", False, date(1990, 5, 15), "Gerente", 50000)
    p2 = Estudiante("Luis", True, date(2000, 8, 20), "Ingeniería")
    print(f"Conteo de personas: {Persona.conteo}")
    print(p1.info())
    print(p2.info())
    
    for p in [p1, p2]:
        print(p.trabajar())
    

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
    print("\n. . . H e c h o . . .")
        

