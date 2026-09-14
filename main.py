# main.py
import runpy
import sys, os
from pathlib import Path

carrera = "TIID"

# Ahora puedes importar directamente
from src.u1 import p02CSV as prg

def main():
    #global MATERIA
    MATERIA ="POO"
    print(f"Bienvenido al curso de {MATERIA} en la carrera de {carrera}")  # POO
   
    #prg.main()
    #runpy.run_module(prg.__name__, run_name="__main__")
    runpy.run_path(prg.__file__)

if __name__ == "__main__":
      MATERIA="OOP"  # Variable global
      os.system("cls" if os.name == 'nt' else 'clear')  # Limpiar pantalla
      main()
      print(f"Nos vemos mañana  en {MATERIA}") # OOP
      print(". . . Hecho")
      
  