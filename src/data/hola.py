import os
import sys
from pathlib import Path

print(os.system('cls'))
print("\n",sys.path, "\n")  # lista de rutas donde busca modulos y paquetes
print(os.getcwd())
db_file = Path(__file__).resolve().parent
print(db_file)


ruta_absoluta = db_file
ruta_proyecto = os.getcwd()
ruta_relativa = os.path.relpath(ruta_absoluta, ruta_proyecto)
print(ruta_absoluta)
print(ruta_proyecto)
print(ruta_relativa)
