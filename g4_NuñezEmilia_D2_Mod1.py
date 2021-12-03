lista = [100,9,2,10,33,11,4,12,5,130,687,14,7,15,8]
mayor = 0
menor = 999999
suma = 0
for x in lista:
    suma += x
    if x > mayor:
        mayor = x
    if x < menor:
        menor = x
promedio = suma / 15
print("Mayor:",mayor)
print("Menor:",menor)
print("Suma:",suma)
print("Promedio:",promedio)
