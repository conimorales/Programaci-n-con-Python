#Constanza Morales
#Fuerza bruta
import string
abecedario = string.ascii_uppercase

intento = str(input("Ingrese una contraseña que sea menor o igual a 4 caracteres:\n")).upper()

recorrer_1 = abecedario.find(intento[0:1])+1
recorrer_2 = abecedario.find(intento[1:2])+1
recorrer_3 = abecedario.find(intento[2:3])+1
recorrer_4 = abecedario.find(intento[3:4])+1

if len(intento) == 4:
    suma_1 = 0
    for n1 in range(1, recorrer_1+1):
        suma_1 += 1

    suma_2 = 0
    for n1 in range(recorrer_1, recorrer_1+1):
        for n2 in range(1, recorrer_2+1):
            suma_2 += 1

    suma_3 = 0
    for n1 in range(recorrer_1, recorrer_1+1):
        for n2 in range(recorrer_2, recorrer_2+1):
            for n3 in range(1, recorrer_3+1):
                suma_3 += 1

    suma_4 = 0
    for n1 in range(recorrer_1, recorrer_1+1):
        for n2 in range(recorrer_2, recorrer_2+1):
            for n3 in range(recorrer_3, recorrer_3+1):
                for n4 in range(1, recorrer_4+1):
                    suma_4 += 1
    sum_total = suma_1+ suma_2+suma_3+suma_4
    print("{} intentos" .format(sum_total)  )

elif len(intento) == 3:
    suma_1 = 0
    for n1 in range(1, recorrer_1+1):
        suma_1 += 1

    suma_2 = 0
    for n1 in range(recorrer_1, recorrer_1+1):
        for n2 in range(1, recorrer_2+1):
            suma_2 += 1

    suma_3 = 0
    for n1 in range(recorrer_1, recorrer_1+1):
        for n2 in range(recorrer_2, recorrer_2+1):
            for n3 in range(1, recorrer_3+1):
                suma_3 += 1
    sum_total = suma_1+ suma_2+suma_3
    print("{} intentos" .format(sum_total))


elif len(intento) == 2:
    suma_1 = 0
    for n1 in range(1, recorrer_1+1):
        suma_1 += 1

    suma_2 = 0
    for n1 in range(recorrer_1, recorrer_1+1):
        for n2 in range(1, recorrer_2+1):
            suma_2 += 1

    sum_total = suma_1+ suma_2
    print("{} intentos" .format(sum_total))

elif len(intento) == 1:
    suma_1 = 0
    for n1 in range(1, recorrer_1+1):
        suma_1 += 1
    print("{} intentos" .format(suma_1))

else:
    print("Para ejecutar el programa tiene que ingresar una contraseña que sea igual o menor a 4 caracteres")