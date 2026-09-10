# main.py
import runpy
import sys, os
from pathlib import Path

# Ahora puedes importar directamente
from src.u1 import p02CSV as prg

def main():
    # global MATERIA
    MATERIA ="POO"
    print(f"Bienvenido al curso de {MATERIA}")
    
    prg.main()
    
    # prg.main()
    #runpy.run_module(prg.__name__, run_name="__main__")
    #runpy.run_path(prg.__file__)

if __name__ == "__main__":
      MATERIA="OOP"  # Variable global
      os.system('cls')
      main()
      print(f"Nos vemos mañana  en {MATERIA}")
      print(". . . Hecho")
      
  