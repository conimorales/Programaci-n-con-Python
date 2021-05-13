def fahrenheit():
    fahrenheit = int(input("Ingrese la temperatura en Fahrenheit"))
    celsius = (fahrenheit + 40) / 1.8 - 40
    print("La temperatura es de {} grados Celsius".format(celsius))


def fahrenheit(f):
    celsius = (f + 40) / 1.8 - 40
    print("La temperatura es de {} grados Celsius".format(celsius))
fahrenheit(int(input("Ingrese la temperatura en Fahrenheit")))

import random
def fahrenheit(f):
    celsius = (f + 40) / 1.8 - 40
    print("La temperatura es de {} grados Celsius".format(celsius))
fahrenheit(random.randint(1, 100))
