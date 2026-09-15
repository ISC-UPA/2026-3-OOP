import os, sys
from pathlib import Path
from datetime import date
import pandas as pd
import pyodbc

sys.path.append("src")
#sys.path.append(os.getcwd())

from tools import fn                                 # general
# from src.tools import fn                             # general
# from src.tools.fn import numero_aleatorio, sumar     # especifica

def main():
    numero = fn.numero_aleatorio(90)
    print(f"El número aleatorio es: {numero}")
    
    db_file = os.getcwd()+ "/data/Estados.accdb"
    conn_str = (
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        fr"DBQ={db_file};"
    )
    # Conexión
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor() 
    
    sql1 = "SELECT * FROM Estados where Partido = 'PAN'"
    sql2 = "select IdEstado, abr, gobernador, nacimiento, \n" + \
           "       YEAR(NOW()) - YEAR(nacimiento) as Edad \n" + \
           "FROM Estados where Partido = ?"
    print(sql2)
    cursor.execute(sql1)
    cursor.execute(sql2, ("PAN",))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    
    # Con pandas 
    #df = pd.read_sql_query(sql1, conn)
    df = pd.read_sql_query(sql2, conn, params=("PAN"))    
    conn.close()
    print(df)
    
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    fecha = date.today()
    dia_semana = fecha.weekday()  # 0=lun, 6=dom
    print(f"día de la semana: {dia_semana}")
    nacimiento = date(2000, 9, 15)
    nacimiento = date.fromisoformat("2000-09-15")
    nacimiento = date.strptime("15/09/2000", "%d/%m/%Y")
    edad = fecha.year - nacimiento.year
    sueldo= 1234.567
    print(edad)
    print(f"El sueldo es: {sueldo:>15,.2f}")
    # main()
    print(". . . H e c h o")
    
