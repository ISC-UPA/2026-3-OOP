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

def insertar_estados(IdEstado, abr, Nombre, gobernador, nacimiento):
    sql = "INSERT INTO Estados (IdEstado, abr, nombre, gobernador, nacimiento) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(sql, (IdEstado, abr, Nombre, gobernador, nacimiento))
    conn.commit()
    print(f"Estado '{IdEstado}' insertado correctamente.")

def actualizar_estado(IdEstado, Nombre, nacimiento):
    sql = "UPDATE Estados SET nombre = ?, nacimiento = ? WHERE IdEstado = ?"
    cursor.execute(sql, (Nombre, nacimiento, IdEstado))
    conn.commit()
    print(f"Estado '{IdEstado}' actualizado correctamente.")

def eliminar_estado(IdEstado):
    sql = "DELETE FROM Estados WHERE IdEstado = ?"
    cursor.execute(sql, (IdEstado,))
    conn.commit()
    print(f"Estado '{IdEstado}' eliminado correctamente.")


def main():
    numero = fn.numero_aleatorio(90)
    print(f"El número aleatorio es: {numero}")
    
    partido = "PAN"       
    sql1 = "SELECT * FROM Estados where Partido = 'PAN'"
    sql2 = f"SELECT * FROM Estados where Partido = '{partido}'"
    sql3 = "select IdEstado, abr, gobernador, nacimiento, \n" + \
           "       YEAR(NOW()) - YEAR(nacimiento) as Edad \n" + \
           "FROM Estados where Partido = ?"
  
    print(sql2)
    cursor.execute(sql1)
    cursor.execute(sql3, (partido))
    for row in cursor.fetchall():
        print(row)
    
    # Con pandas 
    # df = pd.read_sql_query(sql1, conn)
    df = pd.read_sql_query(sql3, conn, params=(partido))    
    print(df)
    
    insertar_estados(33, "For", "Foraneos", "Pepito", date(2000, 9, 15)) # Se queman los folios
    actualizar_estado(33, "Foragiditos", date(2020, 9, 15))
    eliminar_estado(33)
    # cursor.close()
    
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    '''
    fecha = date.today()
    dia_semana = fecha.weekday()  # 0=lun, 6=dom
    print(f"día de la semana: {dia_semana}")
    nacimiento = date(2000, 9, 15)
    nacimiento = date.fromisoformat("2000-09-15")
    nacimiento = date.strptime("15/09/2000", "%d/%m/%Y")
    edad = fecha.year - nacimiento.year
    sueldo= 1234.567
    print(edad)
    print(f"El sueldo es: {sueldo:^15,.2f}")
    '''
    
    db_file = os.getcwd()+ "/data/Estados.accdb"
    conn_str = (
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        fr"DBQ={db_file};"
    )
    # Conexión
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor() 
    main()
    print(". . . H e c h o")
    
