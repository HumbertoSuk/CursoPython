def saludar(nombre):
    mensaje = f"Hola, {nombre}!"
    return mensaje

nombre = "Juan"
saludo = saludar(nombre)
print(saludo)  # Resultado: "Hola, Juan!"


def sumar(a, b):
    resultado = a + b
    return resultado

resultado = sumar(3, 5)
print(resultado)  # Resultado: 8

def factorial(n):
    # Caso base: el factorial de 0 es 1.
    if n == 0:
        return 1
    # Caso recursivo: el factorial de n es n multiplicado por el factorial de (n-1).
    else:
        return n * factorial(n - 1)

# Uso de la función para calcular el factorial de un número.
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")
