import os
import random

def numero_aleatorio(min, max=100):
    if (min > max):
        raise ValueError("El valor mínimo no puede ser mayor que el máximo")
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

def etapa_ifelse(edad):
   etapa=0
   if (edad <=30):
        etapa = 1
   elif (edad <=60):
        etapa =2
   elif (edad <=90):
        etapa = 3
   else :
        etapa = 4
   return etapa    

def etapa_switch(edad):
    match edad:
        case edad if edad <= 30:
            return 1
        case edad if edad <= 60:
            return 2
        case edad if edad <= 90:
            return 3
        case _:
            return 4

def etapa_ternario(edad):
    etapa = 1 if edad <=30 else 2 if edad <= 60 else 3 if edad <= 90 else 4
    etapa = (
          1 if edad <= 30 else
          2 if edad <= 60 else
          3 if edad <= 90 else
          4
      )
    return etapa  

if __name__ == "__main__":
    os.system("cls")
    
    print("Hola Mundo")
    c = numero_aleatorio( 1 , 20)
    print("Aleatorio:", numero_aleatorio(30))
    print("Etapa: ",    etapa_ternario(95))
    
   
    print(". . . Hecho")
    
    



