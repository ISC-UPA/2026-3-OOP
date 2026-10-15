"""Consulta y exporta reportes de la base de datos Northwind.

OBJETIVO
    Consultar clientes, productos y ventas de Northwind y exportar los resultados
    a consola, CSV o JSON, aplicando patrones de diseño.

PATRONES APLICADOS
    1. Singleton  -> DatabaseConnection / DatabaseConnectionMySQL: conexiones a Access y MySQL
    2. Repository -> CustomerRepository, ProductRepository, SalesRepository:
                     encapsulan el SQL; el resto del programa no conoce las tablas
    3. Factory    -> RepositoryFactory: crea repositorios por nombre
    4. Strategy   -> Exporter (Console / Csv / Json): formato intercambiable
    5. Facade     -> NorthwindFacade: interfaz para el cliente (CLI)

USO
    python northwind_patrones.py clientes --pais Mexico
    python northwind_patrones.py productos-top --limit 5 --formato csv --salida top.csv
    python northwind_patrones.py ventas-clientes --limit 10 --formato json
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import threading
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import mysql.connector
from dotenv import load_dotenv
import pyodbc

# ---------------------------------------------------------------------------
# Nombres de tablas (ajústalos si tu script de Northwind los nombra distinto,
# p. ej. `orderdetails` u `order_details`). En Linux MySQL distingue mayúsculas.
# ---------------------------------------------------------------------------
T_CUSTOMERS = "customers"
T_PRODUCTS = "products"
T_ORDERS = "orders"
T_DETAILS = "`order details`"
T_DETAILS = "OrderDetails"

# ===========================================================================
# 1. SINGLETON - Conexión única a la base de datos
# ===========================================================================

class DatabaseConnectionAccess:
    """Conexión Singleton a Access, con la misma interfaz que MySQL."""

    _instance = None
    _lock = threading.Lock()
    placeholder = "?"
    dialect = "access"

    def __new__(cls) -> DatabaseConnectionAccess:
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        with self._lock:
            if getattr(self, "_initialized", False):
                return

            self._db_file = Path(__file__).resolve().parents[2] / "data" / "NorthWind.accdb"
            self._connection = None
            self._initialized = True

    def get_connection(self) -> pyodbc.Connection:
        """Devuelve la conexión única; la abre de nuevo después de cerrarla."""
        with self._lock:
            if self._connection is None:
                if not self._db_file.is_file():
                    raise FileNotFoundError(f"No se encontró la base de datos: {self._db_file}")
                connection_string = (
                    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
                    f"DBQ={self._db_file};"
                )
                self._connection = pyodbc.connect(connection_string)
            return self._connection

    def close(self) -> None:
        with self._lock:
            if self._connection is not None:
                self._connection.close()
                self._connection = None


class DatabaseConnectionMySQL:
    """Singleton thread-safe. Lee la configuración desde el archivo .env."""

    _instance: DatabaseConnectionMySQL | None = None
    _lock = threading.Lock()
    placeholder = "%s"
    dialect = "mysql"

    def __new__(cls) -> DatabaseConnectionMySQL:
        with cls._lock:
            if cls._instance is None:
                instance = super().__new__(cls)
                instance._connection = None
                instance._config = instance._load_config()
                cls._instance = instance
            return cls._instance

    @staticmethod
    def _load_config() -> dict[str, Any]:
        load_dotenv()
        required = ["DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME"]
        missing = [k for k in required if not os.getenv(k)]
        if missing:
            raise RuntimeError(f"Faltan variables en .env: {', '.join(missing)}")
        return {
            "host": os.getenv("DB_HOST"),
            "port": int(os.getenv("DB_PORT", "3306")),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "database": os.getenv("DB_NAME"),
        }

    def get_connection(self):
        """Devuelve la conexión única; reconecta si se perdió."""
        with self._lock:
            if self._connection is None or not self._connection.is_connected():
                self._connection = mysql.connector.connect(**self._config)
            return self._connection

    def close(self) -> None:
        with self._lock:
            if self._connection is not None and self._connection.is_connected():
                self._connection.close()
            self._connection = None


# Selecciona el motor que usarán los repositorios.
DATABASE_CONNECTION = DatabaseConnectionAccess
# Para MySQL, usa: DATABASE_CONNECTION = DatabaseConnectionMySQL


# ===========================================================================
# 2. REPOSITORY - Acceso a datos
# ===========================================================================
class BaseRepository(ABC):
    """Clase base: todos los repositorios comparten la conexión seleccionada."""

    def __init__(self) -> None:
        self._db = DATABASE_CONNECTION()

    def _query(self, sql: str, params: tuple = ()) -> list[dict[str, Any]]:
        conn = self._db.get_connection()
        cursor = conn.cursor()
        try:
            sql = sql.replace("%s", self._db.placeholder)
            cursor.execute(sql, params)
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        finally:
            cursor.close()


class CustomerRepository(BaseRepository):
    def by_country(self, country: str | None = None) -> list[dict[str, Any]]:
        sql = f"SELECT CustomerID, CompanyName, ContactName, City, Country FROM {T_CUSTOMERS}"
        if country:
            return self._query(sql + " WHERE Country = %s ORDER BY CompanyName", (country,))
        return self._query(sql + " ORDER BY Country, CompanyName")


class ProductRepository(BaseRepository):
    def top_by_revenue(self, limit: int = 10) -> list[dict[str, Any]]:
        sql = f"""
            SELECT p.ProductID, p.ProductName,
                   SUM(d.Quantity) AS UnidadesVendidas,
                   ROUND(SUM(d.UnitPrice * d.Quantity * (1 - d.Discount)), 2) AS Ingresos
            FROM {T_PRODUCTS} p
            JOIN {T_DETAILS} d ON d.ProductID = p.ProductID
            GROUP BY p.ProductID, p.ProductName
            ORDER BY Ingresos DESC
            LIMIT %s
        """
        return self._query(sql, (limit,))


class SalesRepository(BaseRepository):
    def by_customer(self, limit: int = 10) -> list[dict[str, Any]]:
        if self._db.dialect == "access":
            if limit < 1:
                raise ValueError("limit debe ser mayor que cero")

            sql = f"""
                SELECT TOP {limit} c.CustomerID, c.CompanyName, c.Country,
                       SUM(d.UnitPrice * d.Quantity * (1 - d.Discount)) AS TotalVentas
                FROM (CUSTOMERS AS c
                      INNER JOIN ORDERS AS o ON o.CustomerID = c.CustomerID)
                     INNER JOIN {T_DETAILS} AS d ON d.OrderID = o.OrderID
                GROUP BY c.CustomerID, c.CompanyName, c.Country
                ORDER BY SUM(d.UnitPrice * d.Quantity * (1 - d.Discount)) DESC
            """
            rows = self._query(sql)
            order_counts = self._query(
                f"SELECT CustomerID, COUNT(*) AS Pedidos "
                f"FROM {T_ORDERS} GROUP BY CustomerID"
            )
            counts_by_customer = {
                row["CustomerID"]: row["Pedidos"] for row in order_counts
            }
            for row in rows:
                row["Pedidos"] = counts_by_customer.get(row["CustomerID"], 0)
            return rows

        sql = f"""
            SELECT c.CustomerID, c.CompanyName, c.Country,
                   COUNT(DISTINCT o.OrderID) AS Pedidos,
                   ROUND(SUM(d.UnitPrice * d.Quantity * (1 - d.Discount)), 2) AS TotalVentas
            FROM {T_CUSTOMERS} c
            JOIN {T_ORDERS} o ON o.CustomerID = c.CustomerID
            JOIN {T_DETAILS} d ON d.OrderID = o.OrderID
            GROUP BY c.CustomerID, c.CompanyName, c.Country
            ORDER BY TotalVentas DESC
            LIMIT %s
        """
        return self._query(sql, (limit,))


# ===========================================================================
# 3. FACTORY - Creación de repositorios
# ===========================================================================
class RepositoryFactory:
    _registry: dict[str, type[BaseRepository]] = {
        "customers": CustomerRepository,
        "products": ProductRepository,
        "sales": SalesRepository,
    }

    @classmethod
    def create(cls, name: str) -> BaseRepository:
        try:
            return cls._registry[name]()
        except KeyError:
            raise ValueError(
                f"Repositorio '{name}' no existe. Opciones: {list(cls._registry)}"
            ) from None


# ===========================================================================
# 4. STRATEGY - Formatos de exportación intercambiables
# ===========================================================================
class Exporter(ABC):
    @abstractmethod
    def export(self, rows: list[dict[str, Any]], destination: str | None = None) -> None: ...


class ConsoleExporter(Exporter):
    def export(
        self, rows: list[dict[str, Any]], destination: str | None = None
    ) -> None:
        if not rows:
            print("Sin resultados.")
            return
        headers = list(rows[0].keys())
        widths = {h: max(len(h), *(len(str(r[h])) for r in rows)) for h in headers}
        line = " | ".join(h.ljust(widths[h]) for h in headers)
        print(line)
        print("-" * len(line))
        for r in rows:
            print(" | ".join(str(r[h]).ljust(widths[h]) for h in headers))
        print(f"\n{len(rows)} registro(s).")


class CsvExporter(Exporter):
    def export(
        self, rows: list[dict[str, Any]], destination: str | None = None
    ) -> None:
        if not rows:
            print("Sin resultados.")
            return
        target = destination or "reporte.csv"
        with open(target, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
        print(f"CSV generado: {target}")


class JsonExporter(Exporter):
    def export(
        self, rows: list[dict[str, Any]], destination: str | None = None
    ) -> None:
        target = destination or "reporte.json"
        with open(target, "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2, default=str)
        print(f"JSON generado: {target}")


EXPORTERS: dict[str, type[Exporter]] = {
    "consola": ConsoleExporter,
    "csv": CsvExporter,
    "json": JsonExporter,
}


# ===========================================================================
# 5. FACADE - Interfaz simplificada sobre repositorios y exportadores
# ===========================================================================
class NorthwindFacade:
    def __init__(self) -> None:
        self._customers: CustomerRepository = RepositoryFactory.create("customers")  # type: ignore
        self._products: ProductRepository = RepositoryFactory.create("products")  # type: ignore
        self._sales: SalesRepository = RepositoryFactory.create("sales")  # type: ignore

    def _export(
        self, rows: list[dict[str, Any]], fmt: str, destination: str | None
    ) -> None:
        EXPORTERS[fmt]().export(rows, destination)

    def report_customers(
        self,
        country: str | None,
        fmt: str = "consola",
        destination: str | None = None,
    ) -> None:
        self._export(self._customers.by_country(country), fmt, destination)

    def report_top_products(
        self, limit: int = 10, fmt: str = "consola", destination: str | None = None
    ) -> None:
        self._export(self._products.top_by_revenue(limit), fmt, destination)

    def report_sales_by_customer(
        self, limit: int = 10, fmt: str = "consola", destination: str | None = None
    ) -> None:
        self._export(self._sales.by_customer(limit), fmt, destination)

    @staticmethod
    def shutdown() -> None:
        connection = DATABASE_CONNECTION._instance
        if connection is not None:
            connection.close()

# ===========================================================================
# CLI
# ===========================================================================
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Reportes Northwind con patrones de diseño")
    parser.add_argument("--formato", choices=EXPORTERS.keys(), default="consola")
    parser.add_argument("--salida", help="Archivo de salida (csv/json)")

    def add_output_arguments(command_parser: argparse.ArgumentParser) -> None:
        command_parser.add_argument(
            "--formato", choices=EXPORTERS.keys(), default=argparse.SUPPRESS
        )
        command_parser.add_argument("--salida", default=argparse.SUPPRESS)

    sub = parser.add_subparsers(dest="comando", required=True)

    p = sub.add_parser("clientes", help="Listar clientes")
    add_output_arguments(p)
    p.add_argument("--pais", help="Filtrar por país")

    p = sub.add_parser("productos-top", help="Productos con más ingresos")
    add_output_arguments(p)
    p.add_argument("--limit", type=int, default=10)

    p = sub.add_parser("ventas-clientes", help="Ventas totales por cliente")
    add_output_arguments(p)
    p.add_argument("--limit", type=int, default=10)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        app = NorthwindFacade()
        if args.comando == "clientes":
            app.report_customers(args.pais, args.formato, args.salida)
        elif args.comando == "productos-top":
            app.report_top_products(args.limit, args.formato, args.salida)
        elif args.comando == "ventas-clientes":
            app.report_sales_by_customer(args.limit, args.formato, args.salida)
        return 0
    except (RuntimeError, mysql.connector.Error, pyodbc.Error, FileNotFoundError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    finally:
        NorthwindFacade.shutdown()


if __name__ == "__main__":
    sys.exit(main())
