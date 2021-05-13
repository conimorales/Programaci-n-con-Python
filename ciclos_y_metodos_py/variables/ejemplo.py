# estas variables se definen dentro del ambiente __main__
name = 'Alan Turing'
age = 41
def any_function():
# Esta variable está siendo definda en un ambiente nuevo: el de any_function
    birthplace = 'Londres'
# Como age es una variable global, se puede acceder desde este scope
# Y también se puede acceder a birthplace, porque aunque sea local, se está en su mismo scope
    print("Edad de", age, "años. Residencia: ", birthplace)
# Acá se vuelve al __main__ (se elimina la identación de 4 espacios)
# La varianle birthplace no existe en este espacio.
print("Nombre: ", name)
any_function()