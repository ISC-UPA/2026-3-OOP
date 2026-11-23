from datetime import date
from decimal import Decimal, InvalidOperation


class BaseView:
    """Funciones de consola que comparten todas las vistas (pedir datos y mostrar mensajes)."""

    def show_message(self, message) -> None:
        print(message)

    def show_error(self, message) -> None:
        print("***", message, "***")

    