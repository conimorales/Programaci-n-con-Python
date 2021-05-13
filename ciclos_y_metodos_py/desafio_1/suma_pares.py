#Constanza Morales
#Suma pares

limit= int(input("Ingrese un número \n"))
i = 0
suma = 0

while i < limit:
    i += 1
    if i % 2 == 0:
        suma += i
print(suma)