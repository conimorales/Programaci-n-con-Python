
num = int(input("Ingrese un número: "))

i = 1
suma = 0

while i <= num:
    cant = int(input("Ingrese n*{} ".format(i)))
    i += 1
    suma += cant


promedio= suma/num
print("el promedio es: {}".format(promedio))


