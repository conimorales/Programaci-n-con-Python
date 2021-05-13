import random

def generador_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    caracteres = mayusculas + minusculas + simbolos + numeros 
    contrasena = []
    
    for i in  range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    
    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generador_contrasena()
    print('tu nueva contraseña es: ' + contrasena)

if __name__ =='__main__':
    run()