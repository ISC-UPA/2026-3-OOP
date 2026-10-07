import os

class CuentaBancaria:
    """Encapsulación: el saldo solo cambia por métodos controlados."""

    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser positiva.")
        self._saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= cantidad

    def __str__(self):
        return f"Cuenta de {self.titular}: ${self._saldo:,.2f}"

def main():
    cuenta = CuentaBancaria("Juan Pérez", 1000.0)
    print(cuenta)

    cuenta.depositar(500.0)
    print(f"Después de depositar: {cuenta}")

    try:
        cuenta.retirar(2000.0)
    except ValueError as e:
        print(f"Error al retirar: {e}")

    cuenta.retirar(300.0)
    print(f"Después de retirar: {cuenta}")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
    print("\n. . . H e c h o . . .")
        