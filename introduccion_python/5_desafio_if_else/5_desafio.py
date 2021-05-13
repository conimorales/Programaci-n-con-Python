password = str(input("Ingrese contraseña: "))
largo = int(len(password))

if largo >= 6:
    print("aviso")

else:
    print("Error, tiene que ingresar una contraseña que tenga más de 6 letras")
