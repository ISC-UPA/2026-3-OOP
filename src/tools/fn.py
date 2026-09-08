import random

def numero_aleatorio(min, max=100):
    if (min > max):
        raise ValueError("El valor mínimo no puede ser mayor que el máximo")
    return random.randint(min, max)


