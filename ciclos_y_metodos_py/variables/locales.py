def ejemplo(parametro):
    print("este es el parámetro: ", parametro)
    definido_dentro= "variable local"
    return parametro, definido_dentro

retorno_1, retorno_2 = ejemplo("hola")

#parametro no esta definido ni definido dentro por fuera, existen solo dentro de la función