import sys

usuarios_normal = int(sys.argv[1])
usuarios_premium = int(sys.argv[2])
usuario_prueba = int(sys.argv[3])
valor_estandar = int(sys.argv[4])
gastos = int(sys.argv[5])

utilidad = ( valor_estandar * usuarios_normal ) - gastos
utilidad_premium = 2 * utilidad


print("El usuario normal paga {}, el usuario premium paga {}, el usuario en periodo de prueba no paga ningún monto".format(utilidad, utilidad_premium))




