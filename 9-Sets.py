#Declarar
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = set([3, 4, 5, 6, 7])

frutas = {"manzana", "banana", "cereza", "manzana"}  #VAlOR DUPLICADO
colores = set(["rojo", "verde", "azul", "rojo"])

#Agregar
frutas.add("naranja")
#Eliminar
frutas.remove("banana")
frutas.discard("pera")

#Union 
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1.union(conjunto2)

#Intersecccion 
interseccion = conjunto1.intersection(conjunto2)

#Diferencia
diferencia = conjunto1.difference(conjunto2)

#Subconjuntos
es_subconjunto = conjunto1.issubset(conjunto2)
