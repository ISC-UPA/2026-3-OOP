import os

class CuentaBancaria:

    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def getSaldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser positiva.")
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.__saldo:
            raise ValueError("Saldo insuficiente.")
        self.__saldo -= cantidad

    def __str__(self):
        return f"Cuenta de {self.titular}: ${self.getSaldo():,.2f}"

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
    
    print(f"Saldo actual: ${cuenta.getSaldo():,.2f}")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
    print("\n. . . H e c h o . . .")
        