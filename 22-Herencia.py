class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} ladra"

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} maulla"

mi_perro = Perro("Rex")
mi_gato = Gato("Whiskers")

print(mi_perro.hablar())  # Resultado: "Rex ladra"
print(mi_gato.hablar())   # Resultado: "Whiskers maulla"
