import os, sys
from datetime import datetime
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    
    def __init__(self, placa):
        self.__placa = placa
        self.llegada = datetime.now()

    def getPlaca(self) -> str:
        return self.__placa

    def setPlaca(self, placa:str):
        self.__placa = placa
        
    #@abstractmethod
    #def method():
    #    pass        
        
class Carro(Vehiculo):
    valorPeaje = 10e3

    def __init__(self, placa):
        super().__init__(placa)
        #self.setPlaca(placa)
        #self.__placa = placa  # Error
        #self.llegada = datetime.now()

    def imprimir(self):
        print(f"Carro con placa: {self.getPlaca()} llegada: {self.llegada} peaje: {Carro.valorPeaje}")
        
    #def method():
    #    pass        
      
class Moto(Vehiculo):
    valorPeaje = 5e3

    def __init__(self, placa):
        super().__init__(placa)
        #self.setPlaca(placa)
        #self.__placa = placa  # Error
        #self.llegada = datetime.now()

    def imprimir(self):
        print(f"Moto con placa: {self.getPlaca()} llegada: {self.llegada} peaje: {Moto.valorPeaje}")

class Camion(Vehiculo):
    valorPeaje = 5e3

    def __init__(self, placa, ejes):
        super().__init__(placa)
        self.numeroEjes=ejes
        #self.setPlaca(placa)
        #self.__placa = placa  # Error
        #self.llegada = datetime.now()

    def imprimir(self):
        print(f"Camion con placa: {self.getPlaca()} llegada: {self.llegada} peaje: {Camion.valorPeaje*self.numeroEjes}")


class Peaje:
    montoPeajes = 0.0     # Total  de dinero Global
    conteoPeajes = 0      # Numero de casetas creadas    
    conteoVehiculos = 0   # Numero de vehiculos globales 
    conteoCarros = 0      # Numero de carros    globales
    conteoMotos = 0       # Numero de carros    globales
    conteoCamiones = 0    # Numero de carros    globales

    def __init__(self, nombre):
        Peaje.conteoPeajes+=1
        self.nombre = nombre
        self.montoPeaje = 0   # dinero de una caseta
        self.vehiculos = []   # vehiculos de una caseta

    def addVehiculo(self, v:Vehiculo):
        self.vehiculos.append(v)
        Peaje.conteoVehiculos+=1

        costoVehiculo = 0    
        if isinstance(v, Carro):
            Peaje.conteoCarros+=1
            #costoVehiculo = Carro.valorPeaje
            costoVehiculo = self.calcularPeaje(v)
        elif isinstance(v, Moto):
            Peaje.conteoMotos+=1
            #costoVehiculo = Moto.valorPeaje
            costoVehiculo = self.calcularPeaje(v)
        elif isinstance(v, Camion):
            Peaje.conteoCamiones+=1
            #costoVehiculo = Camion.valorPeaje * v.numeroEjes
            costoVehiculo = self.calcularPeaje(v)
        else:
            print("Vehiculo No Identificado")

        self.montoPeaje+=costoVehiculo     # monto de una caseta
        Peaje.montoPeajes+=costoVehiculo   # monto de todas las casetas         
        
    def calcularPeaje(self, v) -> int:  # dinero de un Vehiculo
        costoUnidad = 0
        if isinstance(v, Carro):
            costoUnidad = Carro.valorPeaje
        elif isinstance(v, Moto):
            costoUnidad = Moto.valorPeaje
        elif isinstance(v, Camion):
            costoUnidad = Camion.valorPeaje * v.numeroEjes
        else:
            print("Vehiculo Desconocido")
        return costoUnidad

    def imprimir(self):
        print(f'Nombre: {self.nombre} Monto: {self.montoPeaje} Vehiculos: {len(self.vehiculos)}')

    def getTipo(self, v) -> str:
        tipo = "OVNI"
        if isinstance(v, Carro):
            tipo = "Carro"
        elif isinstance(v, Moto):
            tipo = "Moto"
        elif isinstance(v, Camion):
            tipo = "Camion"
        else:
            print("Vehiculo OVNI")
        return tipo  

def main():
    hoy = datetime.now()
    print("Fecha de hoy:", hoy)
    #                   Y    M   D   h   m  s    
    fecha2 = datetime(2026, 11, 22, 12, 15, 0)
    fecha1 = datetime(2026, 11, 22, 10, 25, 0)
    diferencia = fecha2 - fecha1
    print(diferencia)

    print("dias:   ",diferencia.days)
    print("horas:  ", diferencia.seconds // 3600)
    print("minutos:", (diferencia.seconds % 3600) // 60 )

    peajes = []
    peajes.append(Peaje("Norte"))
    peajes.append(Peaje("Sur"))
    
    #a1 = Vehiculo("a")
    #peajes[0].addVehiculo(a1)    

    a2 = Camion("b",3)
    peajes[0].addVehiculo(a2)
    a2.imprimir()

    
    autos=[
        Camion("T1",2),
        Carro("C1"),
        Carro("C2"),
        Moto("M1"),
        Moto("M2"),
        Camion("T1",2),
        Camion("T2",3),
        Camion("T3",4)
    ]
    for i in autos:
        peajes[1].addVehiculo(i)
   
    print()
    for v in peajes[1].vehiculos:
        print(peajes[1].nombre, peajes[1].getTipo(v), v.getPlaca(), v.llegada,  peajes[1].calcularPeaje(v))
        #insertarPeaje("Centro", "Carro", "C2", "2026-10-22 21:47:06", 20000)
    
    print()
    peajes[0].imprimir()
    peajes[1].imprimir()
    
    print("No. Casetas:  ", Peaje.conteoPeajes)
    print("Monto Total:  ", Peaje.montoPeajes)      
    print("Peaje[0]  $:  ", peajes[0].montoPeaje )   
    print("Peaje[1]  $:  ", peajes[1].montoPeaje )  
    print("No. Vehiculos:", Peaje.conteoVehiculos)
    print("No. Carros:   ", Peaje.conteoCarros)
    print("No. Motos:    ", Peaje.conteoMotos)
    print("No. Camiones: ", Peaje.conteoCamiones)
    print("No. Vehiculos en Peaje[0]", len(peajes[0].vehiculos))
    print("No. Vehiculos en Peaje[1]", len(peajes[1].vehiculos))




if __name__ == "__main__":
    os.system("cls")
    main()
    print("\n. . . H e c h o")
    
    
    