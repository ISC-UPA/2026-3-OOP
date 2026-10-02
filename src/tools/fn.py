import random
import unicodedata

def numero_aleatorio(min, max=100):
    if (min > max):
        raise ValueError("El valor mínimo no puede ser mayor que el máximo")
    return random.randint(min, max)

def sumar(a, b):
    return a + b

def etapaVida(edad):
    etapa = 1 if edad <=30 else 2 if edad <= 60 else 3 if edad <= 90 else 4
    return etapa

def esPalindromo1(cadena):
    cadena = str(cadena).lower().replace(" ", "")
    cadena = ''.join(c.lower() for c in cadena if c.isalnum())
    
    for a, b in [('á','a'), ('é','e'), ('í','i'), ('ó','o'), ('ú','u')]: # Recorre la lista de tuplas de acentos y sus reemplazos
        cadena = cadena.replace(a, b)
    cadena = unicodedata.normalize('NFD', cadena)  # Normalization Form Decomposed (NFD) descompone los caracteres acentuados en su forma base y la marca de acento, lo que permite eliminar los acentos más fácilmente.
    cadena = ''.join(c for c in cadena if unicodedata.category(c) != 'Mn')  # Mark , Nonspacing (Mn) es una categoría de caracteres en Unicode que representa marcas diacríticas que no ocupan espacio por sí mismas, como acentos, diéresis o tildes.
        
    return cadena == cadena[::-1]

def esPalindromo2(cadena):
    cadena = cadena.lower().replace(" ", "")
    longitud = len(cadena)
    for i in range(longitud // 2):
        if cadena[i] != cadena[longitud - 1 - i]:
            return False
    return True

def esPalindromo3(cadena):
    cadena = cadena.lower().replace(" ", "")
    return all(cadena[i] == cadena[-(i + 1)] for i in range(len(cadena) // 2))

def esPalindromo4(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == ''.join(reversed(cadena))

def esPalindromo5(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == ''.join(cadena[i] for i in range(len(cadena) - 1, -1, -1))

def esPalindromo6(cadena) -> bool:
    acentos = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")
    cadena = cadena.lower().replace(" ", "")
    cadena = cadena.translate(acentos)
    return cadena == ''.join(reversed(cadena))






