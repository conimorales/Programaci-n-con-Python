#ocupacion = 'Estudiante'
print('Opciones de ocupación: Estudiante, Jubilado, Desempleado u otro')
ocupacion=input('Ingresa tu ocupación: ')

if ocupacion == 'Estudiante':
    print('Tienes 50% de descuento')
elif ocupacion == 'Jubilado':
    print('Tienes 75% de descuento')
elif ocupacion == 'Desempleado':
    print('Tienes 25% de descuento')

else:
    print('Debes pagar el 100%')