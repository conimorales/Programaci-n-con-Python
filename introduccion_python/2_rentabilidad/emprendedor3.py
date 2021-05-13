import sys

precio = int(sys.argv[1])
usuarios = int(sys.argv[2])
gastos = int(sys.argv[3])

utilidad_nueva = ( precio * usuarios ) - gastos

if len(sys.argv) == 5:
    utilidad_anterior = int(sys.argv[4])
    if utilidad_nueva > utilidad_anterior:
        print("La utilidad actual de {} es mayor a la anterior ".format(utilidad_nueva))

    else:
        print("La utilidad anterior es mayor: {}". format(utilidad_anterior))

else:
    utilidad_anterior = 1000
    if utilidad_nueva > utilidad_anterior:
        print("La utilidad actual de {} es mayor a la anterior ".format(utilidad_nueva))

    else:
        print("La utilidad anterior es mayor: {}". format(utilidad_anterior))


