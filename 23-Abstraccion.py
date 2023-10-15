class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        pass

class Coche(Vehiculo):
    def arrancar(self):
        return f"Arrancando el coche {self.marca} {self.modelo}"

class Moto(Vehiculo):
    def arrancar(self):
        return f"Arrancando la moto {self.marca} {self.modelo}"
