def sumar(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

resultado = sumar(1, 2, 3, 4, 5)
print(resultado)  # Resultado: 15





def detalles_persona(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

detalles_persona(nombre="Juan", edad=30, ciudad="Ejemploville")
