import sys

limit = int(sys.argv[1])

a = "★"
b = "·.·"
c = "´¯`"

contain = ""


for i in range(limit + 1):
# Primer caso: Concatenar puntos si el elemento es inpar
    if i % 2 != 0:
        contain += b
    # Segundo caso: Concatenar estrella si el elemento es divisible por 4
    elif i % 4 == 0:
        contain += a
    # El resto serán las líneas
    else:
        contain += c
    # Se imprime el acumulador
print(contain)
