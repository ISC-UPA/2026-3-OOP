import os, sys
from pathlib import Path
import datetime
import pandas as pd
import pyodbc

sys.path.append(os.getcwd())
from src.tools import fn 
#from src.tools.fn import numero_aleatorio, sumar

def main():
    #numero =fn.numero_aleatorio(90)
    #print(f"El número aleatorio es: {numero}")
    
    db_file = os.getcwd()+ "/data/Estados.accdb"
    conn_str = (
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        fr"DBQ={db_file};"
    )
    # Conexión
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor() 
    
    sql = "SELECT * FROM Estados where Partido = 'PAN'"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    
    # Con pandas 
    df = pd.read_sql_query(sql, conn)
    conn.close()
    print(df)
    


    
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
    print(". . . H e c h o")
    
