import os, sys
from pathlib import Path
from datetime import date
import pandas as pd
import pyodbc

sys.path.append("src")
from tools import fn 

def palindromo():
    ejemplos = [
    3443,
    "oso",
    "reconocer",
    "Anita lava la tina",
    "Amo la pacífica paloma",
    "Hola mundo"
    ]

    for ej in ejemplos:
        resultado = "Es palíndromo" if fn.esPalindromo1(ej) else "NO es palíndromo"
        print(f"{str(ej):<25} -> {resultado}")


def pdEdad():
    etapaL=["", "Primera Edad", "Segunda Edad", "Tercera Edad", "Horas Extras"]
    etapaD ={1:"Primera Edad", 2:"Segunda Edad", 3:"Tercera Edad", 4:"Horas Extras"}
    semanaL= ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    semanaD= {0:"Lunes", 1:"Martes", 2:"Miércoles", 3:"Jueves", 4:"Viernes", 5:"Sábado", 6:"Domingo"}
    partido = 'MORENA'
    sql1 = "select IdEstado, abr, tot_mun, gobernador, sexo, nacimiento from Estados where Partido = 'MORENA'" 
    sql2 = f"select IdEstado, abr, tot_mun, gobernador, sexo, nacimiento from Estados where Partido = '{partido}'"
    sql3 ='''
    SELECT IdEstado, abr, tot_mun, Gobernador, nacimiento, sexo, inicio,
           YEAR(NOW ()) - YEAR(nacimiento) AS Edad,
           Switch (
               Edad <= 30,  1,
               Edad <= 60,  2,
               Edad <= 90,  3,
               True,        4
           ) AS Etapa
    FROM  Estados where partido =?
    '''
    sql4 ='''
    SELECT IdEstado, abr, tot_mun, Gobernador, nacimiento, sexo, inicio,
           (Weekday ([Inicio])) AS dia,
           WeekDayName (Weekday ([Inicio])) AS Semana,
              IIf(Weekday (Inicio) = 1, 'Domingo',
                  IIf(WeekdayName (Weekday (Inicio)) = 'sábado', 'Sábado', '' )) AS DiaSem
    FROM  Estados where partido =?
    '''
    
    #df = pd.read_sql_query(sql2, conn)
    df = pd.read_sql_query(sql4, conn, params=(partido,))
    
    # Obtener la edad de cada gobernador en la consulta SQL
    df['edad'] = pd.Timestamp.now().year - pd.to_datetime(df['nacimiento']).dt.year
    df["EtapaVida"] = df["edad"].apply(fn.etapaVida)
    
    # Reemplazar los valores de la columna "EtapaVida" con sus correspondientes descripciones
    df["EtapaVida"] = df["EtapaVida"].replace(etapaD)
    # df["EtapaVida"] = df["EtapaVida"].apply(lambda x: etapaL[x])
    
    df["DiaSemana"] = pd.to_datetime(df['nacimiento']).dt.day_of_week
    #df["DiaSemana"] = df["DiaSemana"].apply(lambda x: semanaL[x])
    df["DiaSemana"] = df["DiaSemana"].replace(semanaD)
   
    # Mostrar de df unicamente las mujeres
    df_mujeres = df[df['sexo'] == False]
    # obtener los diferentes sexos
    sexos = df['sexo'].unique()
    # Filtrar por sexo y contar el número de gobernadores por sexo
    df_todos = df[df['sexo'].isin(sexos)]
    # Contar en base al sexo
    df_sexo = df.groupby('sexo').size().reset_index(name='count').sort_values(by='count', ascending=False)
    # sumar el numero de municipios
    df_mun = df['tot_mun'].sum()
    # El mayor numero de municipios
    df_max_mun = df.loc[df['tot_mun'].idxmax()]
    
    print(df)
    print(f"Tipos de sexo: {sexos}")
    print(f"Total de gobernadoras: {len(df_mujeres)}")
    print(f"Total de gobernadores por sexo:\n {df_sexo}")
    print(f"Total de municipios: {df_mun}")
    print(f"Estado con más municipios: {df_max_mun['abr']} con {df_max_mun['tot_mun']} municipios")

def main():
    # palindromo()
    pdEdad()
    pass

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    db_file = os.getcwd()+ "/data/Estados.accdb"
    conn_str = (
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        fr"DBQ={db_file};"
    )
    # Conexión
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor() 

    main()
    print("\n. . . H e c h o . . .\n")
    
    

       