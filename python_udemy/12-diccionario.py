cancion = {
    'artista': 'Metallica', 
    'cancion': 'Enter Sandman',
    'lanzamiento': 1992,
    'likes': 3000
}
print(cancion)
#accede a un elemento
print(cancion['artista'])
#mezclar con un string 
artista= cancion['artista']
print(f'Estoy escuchando a {artista}')
#agregar nuevos valores
cancion['playlist'] = 'Heavy Metal'
print(cancion)
#reemplazar valor existente 
cancion['cancion'] = 'Seek & Destroy'
print(cancion)
#eliminar valor
del cancion['lanzamiento']
print(cancion)