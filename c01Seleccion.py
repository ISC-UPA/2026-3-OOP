import os
import random

def numero_aleatorio(min, max=100):
    return random.randint(min, max)

def etapa_if(edad):
    etapa=0
    if (edad >=1 and edad <=30):
        etapa = 1
    if (edad >=31 and edad <=60):
        etapa =2
    if (edad >=61 and edad <=90):
        etapa = 3
    if (edad >=91):
        etapa = 4
    return etapa

if __name__ == "__main__":
    os.system("cls")
    print("Hola Mundo")
    print(numero_aleatorio(11,20))
    print(numero_aleatorio(30))
   
    print(". . . Hecho")
    
    



