#Creacion 
mi_lista = [1, 2, 3, "manzana", "banana", "cereza"]

#Acceso 
print(mi_lista[0])  # Acceder al primer elemento (1)
print(mi_lista[3])  # Acceder al cuarto elemento ("manzana")

#Agregar
mi_lista.append("uva")  # Agrega "uva" al final
mi_lista.insert(1, "pera")  # Inserta "pera" en la posición 1

#Eliminar
mi_lista.remove("manzana")  # Elimina "manzana"
elemento_eliminado = mi_lista.pop(2)  # Elimina el tercer elemento y lo almacena en elemento_eliminado

#Tamaño
longitud = len(mi_lista)  # Devuelve la longitud de la lista

#Orden o invertir
mi_lista.sort()  # Ordena la lista
mi_lista.reverse()  # Invierte la lista

#Copiar
copia_lista = mi_lista[:]  # Copia utilizando la notación de corte
copia_lista = mi_lista.copy()  # Copia utilizando el método copy()

#Agregar de otra lista
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)  # lista1 ahora contiene [1, 2, 3, 4, 5, 6

#Contar
mi_lista = [1, 2, 2, 3, 2, 4]
conteo = mi_lista.count(2)  # Devuelve 3, ya que "2" aparece 3 veces en la lista

#Index
mi_lista = [10, 20, 30, 40, 50]
indice = mi_lista.index(30)  # Devuelve 2, ya que 30 está en la posición 2

#Clear
mi_lista = [1, 2, 3, 4, 5]
mi_lista.clear()  # La lista se vacía y se convierte en []

#Concatenar
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenada = lista1 + lista2
print(concatenada)  # Resultado: [1, 2, 3, 4, 5, 6]


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenada = lista1[:] + lista2[:]
print(concatenada)  # Resultado: [1, 2, 3, 4, 5, 6]
