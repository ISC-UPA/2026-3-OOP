import os, sys
from dataclasses import dataclass
from numpy import double

@dataclass  # init,  repr,  eq          # En java Lombok @Data   setter, getter, constructor
class Producto:
    productoID:int
    descripcion:str
    precio: double


def main():
    a1 = Producto(1, "Coca", 20)
    print(a1)

    a2 = Producto(2, "Pepsi", 20)
    print(a2)

    a3 = Producto(1, "Coca", 20)

    print(a1 == a2)
    print(a1 == a3)

    print(Producto.__dict__)
    print()
    print(Producto.__doc__)
    print(a1)



if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
    print("\n. . . H e c h o")    