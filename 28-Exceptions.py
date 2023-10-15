try:
    # Código que podría causar una excepción
    resultado = 10 / 0  # Esto generará una excepción "ZeroDivisionError"
except ZeroDivisionError:
    # Manejo de la excepción
    print("¡División por cero!")


try:
    resultado = 10 / 0
except:
    print("¡Se ha producido una excepción!")


try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("¡División por cero!")
else:
    print("La división fue exitosa.")
finally:
    print("Este bloque se ejecuta siempre.")


def dividir(a, b):
    if b == 0:
        raise ValueError("¡División por cero no está permitida!")
    return a / b
