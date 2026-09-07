import os
from pathlib import Path
import csv 
import pandas as pd
from datetime import date

os.system('cls' if os.name == 'nt' else 'clear')
# Leer ubicacion del archivo CSV usando Path   # Recomendado
# Path(p).resolve() --> Ruta absoluta
# Path(p).parent()  --> Carpeta padre
db_file = Path(__file__).resolve().parent /  "Estados.csv"

# Leer ubicacion del archivo CSV usando os.path
#base_dir = os.path.dirname(os.path.dirname(__file__))  # sube un nivel de donde esta este archivo
#db_file = os.path.join(base_dir, "2026-3-OOP", "Estados.csv")


