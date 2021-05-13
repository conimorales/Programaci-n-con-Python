
pregunta = 'Ingresa un número, para conocer si es par o impar: '
pregunta += '(Escribe cerrar para salir de la app) '
preguntar = True

while preguntar:
    
    numero = input(pregunta)
    
    if numero == 'cerrar': #cierra la ejecución
        preguntar = False
        
    else:
        numero = int(numero)

        if numero % 2 == 0:
            print(f'El número {numero} es par')
        else:
            print(f'El número {numero} es impar')