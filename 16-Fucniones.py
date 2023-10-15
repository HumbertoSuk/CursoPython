import random

numeros = [10, 5, 8, 20, 3]

minimo = min(numeros)
print(f"El valor mínimo en la lista es: {minimo}")

maximo = max(numeros)
print(f"El valor maximo en la lista es: {maximo}")


numero_aleatorio = random.random()
print(numero_aleatorio)

cartas = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cartas)
print(cartas)

opciones = ["manzana", "banana", "cereza", "dátil"]
seleccion = random.choice(opciones)
print(seleccion)