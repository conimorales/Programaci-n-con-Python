
limite = int(input("Ingrese un número: "))

i = 0
suma = 0

while i < limite:
    i += 1
    suma += i

promedio=suma/limite
print("el promedio es: {}".format(promedio))