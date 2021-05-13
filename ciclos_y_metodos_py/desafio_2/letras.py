#Constanza Morales 
# DESAFÍO letras 
# 4/mayo/2021

import string
import math

# DESAFIO 1 - LETRAS
abecedario = string.ascii_lowercase


def gen(x):
    letra= abecedario[0:x]
    print(letra)

print("desafío cantidad de letras ")
gen(4)
gen(10)
print("\n")

# DESAFÍO 2 - LETRA_O
a = "***** \n"
b = "*   * \n"
c = "*****"

def  letra_o(x):
    contain = ""
    for i in range(x):

        if i == 0:
            contain += a

        elif i == x-1:
                contain += c

        else:
            contain += b
    print(contain)

print("desafío letra o  ")
letra_o(5)
print("\n")

# DESAFÍO 3 - LETRA I 

d = "***** \n"
e = "  *   \n"
f = "*****"

def  letra_i(x):
    contain = ""
    for i in range(x):

        if i == 0:
            contain += d

        elif i == x-1:
                contain += f

        else:
            contain += e
    print(contain)

print("desafío letra i  ")
letra_i(5)
print("\n")


# DESAFÍO 4 - LETRA X

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
print("desafío letra x  ")
letra_x(5)



