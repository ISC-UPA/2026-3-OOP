# pag 317
import os, sys

class Peaje:
    conteoPeaje = 0         # Total de Peajes Creados
    conteoVehiculos = 0     # Total de Vehiculos considerando todos los peajes
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.totalPeaje = 0  # Dinero acumulado por un peaje(Caseta)
        self.vehiculos = []  # Total de Vehiculos en un peaje
        Peaje.conteoPeaje+=1

    def addVehiculo(self, v:Vehiculo):
        self.vehiculos.append(v)
        Peaje.conteoVehiculos+=1
    
    def calcularPeaje(self, v:Vehiculo) -> int:
         if isinstance(v, Vehiculo):
             self.totalPeaje+= v.valorPeaje
             return v.valorPeaje
         return null

class Vehiculo:
    
    def __init__(self, placa):
        self.placa = placa
        self.valorPeaje = 100

def main():
    peaje = []
    peaje.append(Peaje("Norte"))
    peaje.append(Peaje("Sur"))
    
    v = Vehiculo("a")
    peaje[0].addVehiculo(v)

    v = Vehiculo("b")
    peaje[1].addVehiculo(v)
    v = Vehiculo("c")
    peaje[1].addVehiculo(v)
    print("Costo:", peaje[1].calcularPeaje(v))
    
    print(Peaje.conteoPeaje)
    print(Peaje.conteoVehiculos)
    
    print("Total de Vehiculos en Peaje 2:", len(peaje[1].vehiculos))

if __name__  == "__main__":
    os.system("cls")
    main()
    print("\. . . H e c h o")
    