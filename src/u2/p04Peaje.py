import os, sys
from datetime import datetime

class Vehiculo:
    
    def __init__(self, placa):
        self.__placa = placa
        self.llegada = datetime.now()

def main():
    print("hola")
    pass

if __name__ == "__main__":
    os.system("cls")
    main()
    print("\n. . . H e c h o")
    