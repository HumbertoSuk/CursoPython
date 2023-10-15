
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Ejemploville"
}

nombre = mi_diccionario["nombre"]  # Acceder al valor asociado a la clave "nombre"

mi_diccionario["profesión"] = "Programador"  # Agregar un nuevo par clave-valor

mi_diccionario["edad"] = 31  # Modificar el valor de la clave "edad"

del mi_diccionario["ciudad"]  # Eliminar la clave "ciudad" y su valor

if "edad" in mi_diccionario:
    print("La clave 'edad' existe en el diccionario.")

claves = mi_diccionario.keys()  # Obtiene una lista de claves
valores = mi_diccionario.values()  # Obtiene una lista de valores

for clave in mi_diccionario:
    valor = mi_diccionario[clave]
    print(f"Clave: {clave}, Valor: {valor}")

# Otra forma de iterar a través de los pares clave-valor
for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")
