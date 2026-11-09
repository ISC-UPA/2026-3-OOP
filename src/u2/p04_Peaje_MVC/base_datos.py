import os, sys
from datetime import datetime
from pathlib import Path
import mysql.connector
import pandas as pd
from dotenv import load_dotenv

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

def consultarPeaje(nombre):
    # Opción con pandas
    sql = "SELECT * FROM peajes WHERE nombre = %s"
    df = pd.read_sql_query(sql, conn, params=(nombre,))
    print("Registros: ", len(df))
    return df


