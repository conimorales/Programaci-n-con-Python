def aprobado(promedio, nota_aprobacion = 4):

    if promedio >= nota_aprobacios: # scope
        status = True  # scope
    else:  # scope
        status = False  # scope
    return status  # scope

print(status) # espacio principal __main__

#ejecuta un error 
