playlist = {} # Diccionario vacío 

playlist['canciones'] = [] # lista vacía de canciones

#Proyecto con while, funciones, listas y diccionarios
def app():

    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('¿Cómo deseas nombrar la playlist? \r\n')

        if nombre_playlist :
            playlist['nombre'] = nombre_playlist

            #desactivar el true
            agregar_playlist = False
            break
     

        
        
app()