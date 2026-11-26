import os
from dataclasses import dataclass
from decimal import Decimal

@dataclass  # init,  repr,  eq          # En java Lombok @Data   setter, getter, constructor
class Product:
    description:str
    price: Decimal
    stock: int = 0
    product_id: int | None = None  # None = todavía no se guarda en la base de datos

    def __post_init__(self) -> None:
        self.description = self.description.strip()
        if not self.description:
            raise ValueError("La descripción es obligatoria")
        if self.price < 0:
            raise ValueError("El precio no puede ser negativo")


def _to_product(row: dict) -> Product:
    return Product(        # No importa el orden de los atributos
        product_id=row["productID"],
        description=row["description"],
        price=row["price"],
        stock=row["stock"],
    )

def main():
    datos= {"description":"Coca", "price":20, "productID": 1, "stock": 0 }
    a1 = _to_product(datos)
    print(a1)
    print(type(a1)) # Product

    a2 = Product("Pepsi", 18, 0, 2)
    print(a2)

    a3 = Product("Coca", 20, 0, 1)

    print(a1 == a2) # False
    print(a1 == a3) # True

    print("describe:  ",Product.__doc__)   # describe
    print("contenido: ", a1)

    #print(Product.__dict__)
    #print()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
    print("\n. . . H e c h o")    