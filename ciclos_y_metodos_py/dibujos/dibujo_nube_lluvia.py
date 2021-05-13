import sys
import random

width = int(sys.argv[1])
# Validamos que no sea menor a 10
if width < 10:
    width = 10
# Creamos el con el ancho de la nube
output = "@" * width + "\n"
# Recorremos de 1 a 9 en el loop externo
for i in range(1, 10):
    # Creamos el primer número al azar con el 80% del ancho
    start_random = int(0.8 * width)
    rand_number = random.randint(start_random, width)
    # Transformamos la nieve en nube
    output += "@" * rand_number + "\n"
    # Recorremos el segundo loop con rango de 1 a 10
for j in range(1,10):
    # Creamos el segundo número al azar,
    # utilizando el segundo iterador y el ancho
    rand_number_2 = random.randint(j, width)
    # Concatenamos la lluevia siguiendo la misma lógica
    output += " " * rand_number_2 + "/" + "\n"
# Mostramos el lienzo creado
print(output)