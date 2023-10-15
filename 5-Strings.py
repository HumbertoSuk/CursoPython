cadena = "Hola, mundo"
longitud = len(cadena)  # Resultado: 11

cadena = "Hola, mundo"
mayusculas = cadena.upper()  # Resultado: "HOLA, MUNDO"

cadena = "Hola, Mundo"
minusculas = cadena.lower()  # Resultado: "hola, mundo"

cadena = "   Espacios en blanco   "
sin_espacios = cadena.strip()  # Resultado: "Espacios en blanco"

cadena = "Manzana,Naranja,Uva"
frutas = cadena.split(",")  # Resultado: ['Manzana', 'Naranja', 'Uva']

cadena = "Python es genial"
nuevo_cadena = cadena.replace("Python", "JavaScript")  # Resultado: "JavaScript es genial"

cadena = "Python es un lenguaje de programación"
indice = cadena.find("lenguaje")  # Resultado: 14

cadena = "Python es un lenguaje de programación. Python es genial."
conteo = cadena.count("Python")  # Resultado: 2

print(cadena)