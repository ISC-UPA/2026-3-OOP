import os, sys
from datetime import datetime
class Vehiculo:
    
    def __init__(self, placa):
        self.__placa = placa
        self.llegada = datetime.now()

    def getPlaca(self) -> str:
        return self.__placa

    def setPlaca(self, placa:str):
        self.__placa = placa
        
class Carro(Vehiculo):
    valorPeaje = 10e3

    def __init__(self, placa):
        super().__init__(placa)
        #self.setPlaca(placa)
        #self.__placa = placa

    def imprimir(self):
        print(f"Carro con placa: {self.getPlaca()} llegada: {self.llegada} peaje: {Carro.valorPeaje}")
      
class Peaje:
    totalPeajes = 0.0     # Total  de dinero Global
    conteoPeajes = 0      # Numero de casetas creadas   
    conteoVehiculos = 0   # Numero de vehiculos globales
    conteoCarros = 0      # Numero de carros    globales

    def __init__(self, nombre):
        Peaje.conteoPeajes+=1
        self.nombre = nombre
        self.totalPeaje = 0   # dinero de una caseta
        self.vehiculos = []

    def addVehiculo():
        pass
    
    def calcularPeaje():
        pass
    
def main():
    hoy = datetime.now()
    print(hoy)

if __name__ == "__main__":
    os.system("cls")
    main()
    print("\n. . . H e c h o")
    