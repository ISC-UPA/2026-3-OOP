import os, sys
import datetime

class Vehiculo:
    
    def __init__(self, placa:str):
        self.__placa = placa
        self.llegada = datetime.datetime.now()
        
    def getPlaca(self) -> str:
        return self.__placa
    
    def setPlaca(self, placa):
        self.__placa = placa
            

class Carro(Vehiculo):
    valorPeaje = 10000
    #valorPeaje:int = 10000
    
    pass        
    def __init__(self, placa):
        super().__init__(placa)
        #self.setPlaca(placa)
        #self.__placa = placa

    def imprimir(self):
        return f"Carro con placa: {self.getPlaca()} llegada: {self.llegada} peaje: {self.valorPeaje}"

class Peaje:
    totalPeajes = 0.0     # Total  de dinero Global
    conteoPeajes = 0      # Numero de casetas creadas   
    conteoVehiculos = 0   # Numero de vehiculos globales
    conteoCarros = 0      # Numero de carros    globales

    def __init__(self, nombre):
        self.nombre = nombre
        self.totalPeaje = 0   # dinero de una caseta
        Peaje.conteoPeajes+=1
        self.vehiculos:Vehiculo = []

       # addVehiculo()
        
    
def main():
    hoy = datetime.datetime.now()
    print(hoy)
    pass

if __name__ == "__main__":
    os.system("cls")
    main()
    print("\n. . . H e c h o")
    