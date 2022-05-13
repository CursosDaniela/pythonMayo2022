from ast import Expression
import os

CARPETA = 'contactos/' #Carpeta de contactos
EXTENSION = '.txt' #Extensión de archivos

#contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    #Revisa si la carpeta existe o no
    crear_directorio()

    #mostar el menú
    mostrar_menu()

    #preguntar al usuario la acción a realizar

    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción \r\n')
        opcion = int(opcion)

        #Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('No es una opción valida, intente de nuevo')

#ELIMINAR
def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar:\r\n')
    try:
        os.remove(CARPETA + nombre + EXTENSION )
        print('\r\n Eliminado correctamente')
    except IOError:
        print('El contacto no existe')
        print(IOError)
    app()

#BUSCAR
def buscar_contacto():
    nombre = input('Seleccion el contacto que desea buscar:\r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Información del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)
    
    #Reiniciar la app
    app()

#VER CONTACTO

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [ i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open (CARPETA + archivo)  as contacto:
            for linea in contacto:
                #imprime los contenidos
                print(linea.rstrip())
            #imprime separador entre contactos
            print('\r\n')
#EDITAR
def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('nombre del contacto que desea editar: \r\n')

    #revisar si el archivo existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            nombre_contacto = input('Agrega el nuevo nombre: \r\n')
            telefono_contacto = input('Agrega el nuevo teléfono: \r\n') 
            categoria_contacto = input('Agrega la nueva categoría conatacto: \r\n')

            #instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribiendo en el archivo
            archivo.write('Nombre: ' + nombre_contacto + '\r\n')
            archivo.write('Teléfono: ' + telefono_contacto + '\r\n')
            archivo.write('Categoría: ' + categoria_contacto + '\r\n')
            archivo.close()
            
            #Renombrando el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            #Mostrar mensaje de creación exitosa
            print('\r\n Contacto editado exitosamente \r\n')

    else: 
        print('Ese contacto ya existe')

    app()
#AGREGAR  
def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del contacto: \r\n') 

    #revisar si el archivo existe antes de editarlo
    existe = existe_contacto(nombre_contacto)

    #Revisar si el archivo existe
    existe = os.path.isfile(CARPETA + nombre_contacto + EXTENSION)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            telefono_contacto = input('Agrega el teléfono: \r\n') 
            categoria_contacto = input('Categoría conatacto: \r\n')

            #instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write('Nombre: ' + nombre_contacto + '\r\n')
            archivo.write('Teléfono: ' + telefono_contacto + '\r\n')
            archivo.write('Categoría: ' + categoria_contacto + '\r\n')

            #Mostrar mensaje de creación exitosa
            print('\r\n Contacto  creado exitosamente \r\n')

    else:
        print('Ese contacto ya existe')

    #reiniciar la app
    app()

def mostrar_menu():
    print('Seleccione que desea realizar')
    print('1) Angregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver contacto')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')

def crear_directorio():
    if not os.path.exists('contactos/'):
        os.makedirs('contactos/')
        #crear la carpeta

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()