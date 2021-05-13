valor1 = int(input("Ingrese valor 1: "))
valor2 = int(input("Ingrese valor 2: "))
if valor1 >= valor2:
    print("valor1 {} es mayor".format(valor1))
else:
    print("valor2 {} es mayor".format(valor2))




password = str(input("Ingrese contraseña: "))
largo = int(len(password))

if largo >= 6:
    print("aviso")

else:
    print("Error, tiene que ingresar una contraseña que tenga más de 6 letras")
