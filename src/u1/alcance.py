
from datetime import date
import os, sys
from pathlib import Path

sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+"/src")
sys.path.append(os.getcwd()+"/src"+"/u2")
from src.u2.p02Herencia import Empleado

'''
# Ruta hasta donde se encuentra el archivo actual incluido el nombre del archivo
# src_root = Path(__file__).resolve() 
src_root = Path(__file__).resolve().parents[1] # sube un nivel: Abarca hasta src incluido
sys.path.insert(0, str(src_root))
sys.path.insert(0, str(src_root / "u2"))
from u2.p02Herencia import Empleado
'''

def main():
    empleado = Empleado("Ana", False, date(1990, 5, 15), "Gerente", 50000)
    print(empleado.info())
    print(empleado.trabajar())
    print(empleado.cuenta)
    print(f"Saldo:  ${empleado.cuenta._saldo:,.2f}")
    print(f"Sueldo: ${empleado._salario:,.2f}")

if __name__ == "__main__":
    main()
    print("\nFin del programa")
    