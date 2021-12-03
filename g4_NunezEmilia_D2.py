"""Diseñar un programa en python, que usando diccionario nos permita:
	a)cargar la agenda telefónica de nuestros colegas(al menos 5)
	b)nos permita buscar el teléfono de algún contacto"""
agenda = {}
print("Ingrese una opcion")
contador = 1

opcion = int(input("si desea agregar un contacto ingrese 1, si desea buscar ingrese 2, si desea salir ingrese 0: "))
while opcion != 0:
	if opcion == 1:
		while contador < 6:
			agregar = input("Agregue el nombre del contacto, si ya no desea agregar coloque 0: ")
			while agregar != "0":
				numero = input("Agregue el número del contacto: ")
				valor = agenda.setdefault(agregar,numero)
				print(agenda)
				contador += 1
				agregar = input("Agregue el nombre del contacto, si ya no desea agregar coloque 0: ")

	else:
		buscar = input("ingrese el nombre del contacto que desea buscar: ")
		valor = agenda.setdefault(buscar)
		print(f"El numero de {buscar} es: {valor}")
	opcion = int(input("si desea agregar un contacto ingrese 1, si desea buscar ingrese 2, si desea salir ingrese 0: "))











"""	get() keys

Recibe como parámetro una clave, devuelve el valor de la clave. Si no lo encuentra, devuelve un objeto none.

dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
valor = dic.get(‘b’) 

valor → 2


setdefault()

Funciona de dos formas. En la primera como get

dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
valor = dic.setdefault(‘a’)

valor → 1
Y en la segunda forma, nos sirve para agregar un nuevo elemento a nuestro diccionario.

dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
valor = dic.setdefault(‘e’,5)

dic → {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4 , ‘e’ : 5}"""