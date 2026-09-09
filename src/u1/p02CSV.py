import csv
import os
from datetime import date
from pathlib import Path
import pandas as pd

import sys
sys.path.append(os.getcwd() + "/src")

import src.tools.fn as fn
#from src.tools import fn
#from src.tools.fn import numero_aleatorio

def rutaRelativa(ruta_absoluta):
    ruta_proyecto = os.getcwd()
    return os.path.relpath(ruta_absoluta, ruta_proyecto)


def consultarPandas(db_file):
    df = pd.read_csv(db_file, encoding="latin-1")  # utf-8  latin-1 ascii
    print("1--->",df)
    #gobernadoras = df[df["Sexo"] == False]
    #print(gobernadoras)


def consultarCSV(db_file):
    nombre = "PAN.csv"
    destino = Path(__file__).resolve().parent.parent.parent / "data" / nombre

    with open(destino, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        ciudades = []
        partidos = {}

        with open(db_file, "r", encoding="latin-1", newline="") as lectura:
            lector_csv = csv.DictReader(lectura)
            cabeceras = lector_csv.fieldnames
            print("Cabeceras:", cabeceras)

            for fila in lector_csv:
                idCiudad = int(fila["IdEstado"])
                abr = fila["Abr"]
                fecha = date.strptime(fila["Inicio"], "%d/%m/%Y")

                if fila["Partido"] == "PAN":
                    ciudades.append((idCiudad, abr, fecha.year))
                    escritor.writerow([idCiudad, abr, fila["Partido"], fila["Nacimiento"]])

                partidos[fila["Partido"]] = partidos.get(fila["Partido"], 0) + 1

    print(ciudades)
    print("\nConteo de partidos:\n", partidos)


def main():
    #db_file = Path(__file__).resolve().parent.parent.parent / "data" / "Estados.csv"
    #db_file = os.getcwd() + "/data/Estados.csv"      # ruta absoluta
    db_file = os.getcwd() + "\\data\\Estados.csv"   # ruta absoluta
    print("Ruta:", db_file)
    
    consultarPandas(db_file)
    #consultarCSV(db_file)

if __name__ == "__main__":
    os.system("cls")
    main()
    #print("Número aleatorio:", numero_aleatorio(11, 20))
    print("Número aleatorio:", fn.numero_aleatorio(11, 20))
    print(". . . Hecho")

