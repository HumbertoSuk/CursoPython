#F
nombre = "Juan"
edad = 30
mensaje = f"Hola, soy {nombre} y tengo {edad} años."
print(mensaje)

numero = 3.14159265
cadena_formateada = f"El valor de π es aproximadamente {numero:.2f}"  # Redondea a 2 decimales
print(cadena_formateada)

#Format
nombre = "Ana"
edad = 25
mensaje = "Hola, soy {} y tengo {} años.".format(nombre, edad)
print(mensaje)

mensaje = "Hola, soy {0} y tengo {1} años.".format(nombre, edad)

mensaje = "Hola, soy {nombre} y tengo {edad} años.".format(nombre=nombre, edad=edad)

numero = 42
cadena_formateada = "El número es: {:.2f}".format(numero)  # Redondea a 2 decimales

precio = 99.95
precio_formateado = f"${precio:.2f}"  # Muestra el precio con 2 decimales y el símbolo $
print(precio_formateado)

precio = 99.95
precio_formateado = "${:.2f}".format(precio)
print(precio_formateado)

grados_celsius = 25
grados_formateados = f"{grados_celsius}°C"  # Agrega el símbolo °C
print(grados_formateados)
