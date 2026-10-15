import os
import threading
import pyodbc
# Efectivo


class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    # se ejecuta antes de crear la instancia
    # Se encarga de construir y devolver el objeto (normalmente una instancia de la clase).
    def __new__(cls):
        # garantizas que solo un hilo a la vez pueda ejecutar esa sección crítica
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    # Se ejecuta después de que el objeto ya fue creado por __new__.
    def __init__(self):
        with self._lock:
            if hasattr(self, "connection"):
                return

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

    db2 = DatabaseConnection()
    db2.query("SELECT * FROM Estados WHERE Partido = ?", ("MC",))
    print(f"¿Es la misma conexión? {db1.connection is db2.connection}")


if __name__ == "__main__":
    main()
