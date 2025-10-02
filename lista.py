lista = ["pera", "manzana", "sandia", "piña"]


lista.append(input("dame una fruta"))

lista.append(input("dame otra fruta"))


print(lista)

print("la longitud de la lista es", len(lista))

#eliminar el elemento con orden 1 de la lista y mostrar el resultano.

quitar = int(input("introduce la posicion que quieras eliminar"))

lista.remove(lista[quitar])

print(lista)
