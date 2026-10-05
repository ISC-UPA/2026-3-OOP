class Usuario:
    # constructor de la clase usuario
    def __init__(self, param_nombre: str)->None:
        self.nombre: str = param_nombre
        print("Soy el constructor")

persona_1: Usuario = Usuario("Alejandro")
print(persona_1.nombre)

persona_2: Usuario = Usuario("Sofia")
print(persona_2.nombre)

#persona_3: Usuario = Usuario()
persona_3 = Usuario("Juan")
print(persona_3.nombre)
