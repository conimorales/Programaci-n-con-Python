#Constanza Morales
# Crear un programa llamado solo_pares.py, que muestre todos los números pares hasta "n" (incluyendo "n", si éste es par), donde "n" es un valor ingresado por el usuario.
fin = int(input("Ingrese un número para que se finalice la cuenta \n"))

numero = 0

while numero <= fin:
    if numero % 2 == 0:
        print(numero)

    numero += 1 


