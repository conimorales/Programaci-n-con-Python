
num = int(input("Ingrese una opción: \n 1: sumar\n 2: restar\n 3: multiplicar\n 4: dividir \n "))

num_1 = int(input("Ingrese n*1 "))
num_2 = int(input("Ingrese n*2 "))

if num == 1:
    suma = num_1 + num_2 
    print(suma)

elif num == 2:
    resta = num_1 - num_2 
    print(resta)

elif num == 3:
    multi = num_1 * num_2 
    print(multi)

elif num == 4:
    div = num_1 / num_2 
    print(div)