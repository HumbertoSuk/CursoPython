suma = lambda a, b: a + b
resultado = suma(3, 4)
print(resultado)  # Resultado: 7

cuadrado = lambda x: x**2
resultado = cuadrado(5)
print(resultado)  # Resultado: 25

puntos = [(3, 1), (1, 2), (2, 5)]
puntos_ordenados = sorted(puntos, key=lambda x: x[1])
print(puntos_ordenados)  # Resultado: [(3, 1), (1, 2), (2, 5)]

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)  # Resultado: [2, 4, 6, 8]


