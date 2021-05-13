lenguajes = ['Python', 'Kotlin', 'Java', 'Javascript']
print(lenguajes)
print(lenguajes[0]) # python

#ordenar
lenguajes.sort()
print(lenguajes)

#acceder
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#modificar
lenguajes[2] = 'PHP'
print(lenguajes)

#agregar 
lenguajes.append('Ruby')
print(lenguajes)

#eliminar un elemento de un arreglo 
del lenguajes[1]
print(lenguajes)

#eliminar el último elemento del arreglo
lenguajes.pop()
print(lenguajes)

#eliminar con pop elemento específico
lenguajes.pop(2)
print(lenguajes)

#eliminar por nombre 
lenguajes.remove('PHP')
print(lenguajes)