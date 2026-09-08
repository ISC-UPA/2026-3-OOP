import os
from pathlib import Path
import csv
import sys 
import pandas as pd
from datetime import date

os.system('cls' if os.name == 'nt' else 'clear')
print("Hola Mundo")

print(os.getcwd())  # ruta absoluta incluyendo el proyecto
print("\n",sys.path, "\n")  # lista de rutas donde busca modulos y paquetes

# Leer ubicacion del archivo CSV usando Path   # Recomendado
# os.getcwd())      --> Ruta absoluta incluyendo el proyecto
# Path(p).resolve() --> Ruta absoluta incluyendo el archivo.py
# Path(p).parent()  --> Subete a la Carpeta padre
#db_file = Path(__file__).resolve().parent /  "Estados.csv"  # / cancatena
#print(db_file)
#-->
db_file = Path(__file__).resolve().parent  # / cancatena
print("-->", db_file)

# <--
'''
# Leer ubicacion del archivo CSV usando os.path  # Clasico o antiguo
#base_dir = os.path.dirname(os.path.dirname(__file__))  # sube un nivel de donde esta este archivo
#db_file = os.path.join(base_dir, "2026-3-OOP", "Estados.csv")
#print(db_file)

# ----- Leer archivo CSV usando pandas -----
# df = pd.read_csv("Estados.csv", encoding="latin-1")  # utf-8
df = pd.read_csv(db_file, encoding="latin-1")
# print(df)
gobernadoras = df[df["Sexo"] == False]
print(gobernadoras)

# ----- Leer archivo CSV usando csv  -----
archivo = open("PAN.csv", "w", newline="", encoding="utf-8")   # "a" append
escritor = csv.writer(archivo)

ciudades = []
partidos = {}

with open(db_file, 'r') as archivo:
    lector_csv = csv.DictReader(archivo) 
    for fila in lector_csv:
        idCiudad = int(fila['IdEstado'])
        abr = fila['Abr']
        fecha = date.strptime(fila['Inicio'], '%d/%m/%Y')   # '%Y-%m-%d'     '%d/%m/%Y'  
        #ciudades.append((idCiudad, abr, fecha, fecha.year))
        ciudades.append(fila)  # Agregar toda la fila al arreglo de ciudades

        if fila['Partido'] == 'PAN':
            #escritor.writerow([idCiudad, abr, fila['Partido'], fila['Nacimiento']])
            escritor.writerow(fila.values())  # Escribir toda la fila en el archivo CSV
            
        partidos[fila['Partido']] = partidos.get(fila['Partido'], 0) + 1
archivo.close()
     
print(ciudades)
print(partidos)


ruta_absoluta = db_file
ruta_proyecto = os.getcwd()
ruta_relativa = os.path.relpath(ruta_absoluta, ruta_proyecto)
print(ruta_absoluta)
print(ruta_proyecto)
print(ruta_relativa)

'''

