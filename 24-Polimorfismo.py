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

# Función que hace que un animal hable sin importar su tipo
def hacer_hablar(animal):
    return animal.hablar()

# Crear instancias de diferentes tipos de animales
mi_perro = Perro("Rex")
mi_gato = Gato("Whiskers")

# Llamar a la función que hace hablar a los animales
print(hacer_hablar(mi_perro))  # Resultado: "Rex ladra"
print(hacer_hablar(mi_gato))   # Resultado: "Whiskers maulla"
