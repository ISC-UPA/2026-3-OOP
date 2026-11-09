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
        
        print(self.nombre, self.getTipo(v), v.getPlaca(), v.llegada,  self.calcularPeaje(v))
        #insertarPeaje("Centro", "Carro", "C2", "2026-10-22 21:47:06", 20000)
        
        
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
    