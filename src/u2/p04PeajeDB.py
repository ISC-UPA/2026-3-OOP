import os, sys
from datetime import datetime
from pathlib import Path
import mysql.connector
from dotenv import load_dotenv
import pandas as pd

load_dotenv(Path(__file__).resolve().parents[2] / ".env", override=True)
config = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

# Conexión
conn = mysql.connector.connect(**config)
cursor = conn.cursor(dictionary=True)  # dictionary=True → resultados como dict

# ============================
# ALTAS (INSERT)
# ============================
def insertarPeaje(nombre, tipo, placa, llegada, monto):
    sql = "INSERT INTO peajes (nombre, tipo, placa, llegada, montoPeaje) VALUES (%s, %s, %s, %s, %s)"
    #sql =f"insert into peajes values(null, {nombre}, {tipo}, {placa}, {llegada}, {monto})"
    #print(sql)
    cursor.execute(sql, (nombre, tipo, placa, llegada, monto))
    conn.commit()
    print(f"Peaje:'{placa}' insertado correctamente.")

    cursor.close()
    conn.close()    
    # cursor.rowcount  # Numero de registros:  Insert, Delete or Update
    
    id_generado = cursor.lastrowid
    print(f"Peaje insertado correctamente. ID: {id_generado}")
    return id_generado    

def consultarPeaje(nombre):
    # Opción con cursor
    sql = "SELECT * FROM peajes WHERE nombre = %s"
    cursor.execute(sql, (nombre,))
    rows = cursor.fetchall()   # len(rows) # Numero de registros
    for row in rows:
        print(row)

    # Opción con pandas
    sql = "SELECT * FROM peajes WHERE nombre = %s"
    df = pd.read_sql_query(sql, conn, params=(nombre,))
    print("Registros: ", len(df))
    return rows, df

def main():
    #nuevo_id = insertarPeaje("3C", "Carro", "C2", "2026-10-22 21:47:06", 20000)
    #print("Nuevo registro:", nuevo_id)
    consultarPeaje("Norte")

if __name__ == "__main__":
    os.system("cls")
    main()
    print("\n. . . H e c h o")
    
    
    