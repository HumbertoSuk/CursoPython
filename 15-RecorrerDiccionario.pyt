personas = {
    "Juan": 30,
    "Ana": 25,
    "Luis": 17,
    "María": 22
}

for nombre, edad in personas.items():
    if edad > 18:
        print(f"{nombre} tiene {edad} años y es mayor de 18.")
