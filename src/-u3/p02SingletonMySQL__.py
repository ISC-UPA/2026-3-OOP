import threading


class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        with self._lock:
            if hasattr(self, "connection_string"):
                return

            self.connection_string = "jdbc:mysql://localhost:3306/mydb"
            print("Conexión a base de datos establecida")

    def query(self, sql):
        print(f"Ejecutando query: {sql} en {self.connection_string}")


def main():
    db1 = DatabaseConnection()
    db1.query("SELECT * FROM users")

    db2 = DatabaseConnection()
    db2.query("SELECT * FROM products")
    print(f"¿Son la misma conexión? {db1 is db2}")


if __name__ == "__main__":
    main()
