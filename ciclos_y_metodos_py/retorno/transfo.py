def transformar_de_fahrenheit(f):
    celsius = (f + 40) / 1.8 - 40
    return celsius
transformado = transformar_de_fahrenheit(110)
print(transformado)

