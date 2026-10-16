import os, sys
from datetime import datetime

from matplotlib.layout_engine import PlaceHolderLayoutEngine

class Vehiculo:
    
    def __init__(self, placa):
        self.__placa = placa
        self.llegada = datetime.now()

    def getPlaca(self) -> str:
        return self.__placa

    def setPlaca(self, placa:str):
        self.__placa = placa
        
class Carro(Vehiculo):
    pass

           
        


def main():
    print("hola")
    pass

if __name__ == "__main__":
    os.system("cls")
    main()
    print("\n. . . H e c h o")
    