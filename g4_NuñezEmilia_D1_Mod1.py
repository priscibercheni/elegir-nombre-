nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad > 16:
    print(nombre, "puede votar")
else:
    print(nombre, "debe esperar para votar")