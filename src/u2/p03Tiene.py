import os

class CuentaBancaria:

    def uppercase_decorator(function):
        def wrapper(param1):
            func = function(param1)
            make_uppercase = func.upper()
            return make_uppercase
        return wrapper

    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def getSaldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser positiva.") # Se para el programa
        assert cantidad > 0, "La cantidad a depositar debe ser positiva."  # Si no se cumple, se para el programa
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.__saldo:
            raise ValueError("Saldo insuficiente.")
        self.__saldo -= cantidad

    @uppercase_decorator
    def __str__(self):
        return f"Cuenta de {self.titular}: ${self.getSaldo():,.2f}"


def main():
    cuenta = CuentaBancaria("Juan Pérez", 1000.0)
    assert(isinstance(cuenta, CuentaBancaria)), "cuenta debe ser una instancia de CuentaBancaria"
    print(cuenta)

    cuenta.depositar(500.0)
    print(f"Después de depositar: {cuenta}")

    try:  # Excepciones para manejar errores
        cuenta.retirar(20.0) 
    except ValueError as e:
        print(f"Error al retirar: {e}")
    except Exception as e:
        print(f"Error inesperado: {e} \n {type(e)}")
    else: # en caso de que no haya excepciones (opcional)
        print(f"Retiro exitoso: {cuenta}")
    finally: # Siempre se ejecuta, haya o no excepciones (opcional)
        print("Operación de retiro finalizada.")

    cuenta.retirar(300.0)
    print(f"Después de retirar: {cuenta}")
    
    print(f"Saldo actual: ${cuenta.getSaldo():,.2f}")
   

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
    print("\n. . . H e c h o . . .")
        