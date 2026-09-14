import os, sys
from pathlib import Path
import datetime
import pandas as pd
import pyodbc

sys.path.append(os.getcwd())
from src.tools import fn 
#from src.tools.fn import numero_aleatorio, sumar

def main():
    numero =fn.numero_aleatorio(90)
    print(f"El número aleatorio es: {numero}")
    
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
    print(". . . H e c h o")
    
