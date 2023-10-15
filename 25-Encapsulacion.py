class MiClase:
    def __init__(self):
        self._atributo_privado = 42

    def _metodo_privado(self):
        return "Soy un método privado"

objeto = MiClase()
print(objeto._atributo_privado)  # Esto es posible, pero es una convención para no accederlo directamente.
print(objeto._metodo_privado())  # Esto también es posible, pero es una convención para no llamarlo directamente.


class MiClase2:
    def __init__(self):
        self.__atributo_privado = 42

    def __metodo_privado(self):
        return "Soy un método privado"

objeto = MiClase2()
print(objeto.__atributo_privado)  # Esto generará un error de atributo.
print(objeto.__metodo_privado())  # Esto generará un error de atributo.
