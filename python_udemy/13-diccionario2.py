#iniciar un diccionario vacío
jugador = {}
print(jugador)

#se une un jugador 
jugador['nombre'] = 'Juan'
jugador['puntaje'] = 0
print(jugador)

#aumentar puntaje
jugador['puntaje'] = 100
print(jugador)

#acceder a un valor
print(jugador.get('consola', 'No existe ese valor'))
print(jugador.get('puntaje'))

#iterar en el diccionario
for llave, valor in jugador.items():
    print(llave) #puntaje
    print(valor) #100

#eliminar jugador y puntaje 
del jugador['nombre']
del jugador['puntaje']
print(jugador) #objeto se elimina completo