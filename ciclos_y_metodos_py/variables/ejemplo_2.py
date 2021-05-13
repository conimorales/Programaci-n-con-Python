age = 41
def any_function():
# Se asigna un nuevo valor
    age = 100
    print("En el scope de la función, age tiene el valor de:", age)

any_function()
print("Luego de ejecutar any_function(), tiene el valor de:",age)
