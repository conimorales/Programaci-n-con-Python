import math


def  letra_x(x):
#si el número es par se suma 1, si no se deja igual
    if x%2!=0:
        x= x
    else:
        x= x+1

#mitad de la x
    mitad = math.ceil(x/2)
 
    contain = ""
    resta= 0
    suma = 1

    for i in range(mitad):

        if i == mitad-1: 
            contain += " " * i +  "*" +"\n"
        else: 
            #la resta se hace para crear la segunda parte de los * 
            resta += 1
            resta_2= x  - resta-1
            contain += " " * i + "*" + " "  * (resta_2-i) + "*\n"
 

    for i in range(mitad, x):
        if i == x-1: 
             contain += "*" + " "  * (x-2) + "*\n"
        else:

# creando la primera parte de los espacios
            resta += 1
            resta_2= x - resta-1

# creando la segunda parte de los espacios luego del asterisco
            suma += 2
            num_impar = suma-2

            contain += " " * (resta_2)  + "*" + " " * num_impar  + "*\n"
    

    print(contain)


letra_x(9)

