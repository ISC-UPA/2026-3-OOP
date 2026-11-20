from datetime import date
from decimal import Decimal, InvalidOperation


class BaseView:
    """Funciones de consola que comparten todas las vistas (pedir datos y mostrar mensajes)."""

    def ask_id(self) -> int:
        return self.ask_int("Ingrese el ID")

    def ask_text(self, label: str, current: str | None = None) -> str:
        return self._ask(label, self._parse_text, current, "Este dato es obligatorio.")

    def ask_int(self, label: str) -> int:
        return self._ask(label, int, None, "Escriba un número entero.")

    def ask_date(self, label: str, current: date | None = None) -> date:
        return self._ask(f"{label} (AAAA-MM-DD)", date.fromisoformat, current, "Fecha inválida.")

    def ask_price(self, label: str, current: Decimal | None = None) -> Decimal:
        return self._ask(label, self._parse_price, current, "Precio inválido.")

    def show_message(self, message) -> None:
        print(message)

    def show_error(self, message) -> None:
        print("***", message, "***")

    def _ask(self, label, parse, current, error_message):
        """Pregunta hasta que el dato sea válido.

        `parse` convierte el texto escrito (por ejemplo `int`) y lanza ValueError si no se puede.
        Si hay un valor actual, presionar Enter lo conserva.
        """
        hint = f" [{current}]" if current is not None else ""
        while True:
            text = input(f"{label} {hint}: ").strip()
            if not text and current is not None:  # Conservó el valor 
                return current
            try:
                return parse(text)                # Modificó el valor
            except (ValueError, InvalidOperation):
                print(error_message)

    @staticmethod
    def _parse_text(text: str) -> str:
        if not text:
            raise ValueError
        return text

    @staticmethod
    def _parse_price(text: str) -> Decimal:
        price = Decimal(text)
        if not price.is_finite():  # rechaza "nan" e "inf"
            raise ValueError
        return price
