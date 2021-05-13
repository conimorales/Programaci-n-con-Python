import sys
import random 

width = int(sys.argv[1])


if width < 10:
    width = 10

output = ""

for i in range(1, 10):
# Creamos el primer número al azar, utilizando el iterador
# y el ancho del usuario
    rand_number = random.randint(1, width)
    # Usamos el número creado para agregar espacios en blanco antes de la nieve
    output += " " * rand_number + "*" + "\n"
    # Recorremos el segundo loop con rango de 1 a i
    for j in range(1, i):
    # Creamos el segundo número al azar,
    # utilizando el segundo iterador y el ancho
        rand_number_2 = random.randint(j, width)
    # Concatenamos la lluevia siguiendo la misma lógica
        output += " " * rand_number_2 + "/" + "\n"
# Mostramos el lienzo creado
print(output)