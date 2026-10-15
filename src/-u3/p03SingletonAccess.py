import os
import pyodbc


class DatabaseConnection:
    _instance = None

    # se ejecuta antes de crear la instancia
    # Se encarga de construir y devolver el objeto (normalmente una instancia de la clase).
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Para evitar re-inicializar la conexión cada vez
        if not hasattr(self, "connection"):
            db_file = os.path.join(os.getcwd(), "data", "Estados.accdb")
            connection_string = (
                r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
                f"DBQ={db_file};"
            )
            self.connection = pyodbc.connect(connection_string)
            self.cursor = self.connection.cursor()

    def query(self, sql, params=()):
        self.cursor.execute(sql, params)
        for row in self.cursor.fetchall():
            print(row)


def main():
    db1 = DatabaseConnection()
    db1.query("SELECT * FROM Estados WHERE sexo = False")

    print()
    db2 = DatabaseConnection()
    db2.query("SELECT * FROM Estados WHERE Partido = ?", ("MC",))
    print(f"¿Es la misma conexión? {db1.connection is db2.connection}")
    print(db1)
    print(db2)

if __name__ == "__main__":
    os.system("cls")
    main()
    print(". . . Hecho")

