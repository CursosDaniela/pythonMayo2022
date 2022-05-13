playlist = {} #diccionario vacio
playlist['canciones'] = []

#funcion principal
def app():
    
    #agregar playlist
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Cómo deseas nombrar la playlist\r\n')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist

            #ya tenemos un nombre, desctivar True
            agregar_playlist = False

            #Manadar a llamar la función para agregar canciones
            agregar_canciones()

def agregar_canciones():
    #agregar canciones
    agregar_cancion = True
    while agregar_cancion:

        #Preguntar al usuarioqie canción desea agregar
        nombre_playlist = playlist['nombre']
        pregunta =f'\r\nAgrega canciones para la playlist {nombre_playlist}:\r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones\r\n'

        cancion = input(pregunta)        
        if cancion== 'X':
            #Dejar de agregar canciones
            agregar_cancion = False

            #mostar resumen de la playlist
            mostrar_resumen()
        else:
            playlist['canciones'].append(cancion) 

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist}\r\n')         
    print('canciones:\r\n')
    for cancion in playlist['canciones']:
        print(cancion)
app()