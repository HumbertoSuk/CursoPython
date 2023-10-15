class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando")

mi_perro = Perro("Rex", "Labrador")
mi_perro.ladrar()
