#Constanza Morales
# Crear una variante del programa anterior llamado solo_pares_refactor.py. En este caso, el cero no debe ser considerado (el cero no es par).

fin = int(input("Ingrese un número para que se finalice la cuenta \n"))

numero = 0

while numero <= fin:
    if numero % 2 == 0 and numero != 0:
        print(numero)
    numero += 1 
