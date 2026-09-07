import os
from pathlib import Path
import csv
import sys 
import pandas as pd
from datetime import date

os.system('cls' if os.name == 'nt' else 'clear')

# Leer ubicacion del archivo CSV usando Path   # Recomendado
# Path(p).resolve() --> Ruta absoluta y el archivo
# Path(p).parent()  --> Carpeta padre
db_file = Path(__file__).resolve().parent /  "Estados.csv"
print(db_file)

# Leer ubicacion del archivo CSV usando os.path  # Clasico o antiguo
#base_dir = os.path.dirname(os.path.dirname(__file__))  # sube un nivel de donde esta este archivo
#db_file = os.path.join(base_dir, "2026-3-OOP", "Estados.csv")
#print(db_file)

# df = pd.read_csv("Estados.csv", encoding="latin-1")  # utf-8
df = pd.read_csv(db_file, encoding="latin-1")
print(df)
gobernadoras = df[df["Sexo"] == False]

print(os.getcwd())  # ruta donde esta el proyecto
print(sys.path)


