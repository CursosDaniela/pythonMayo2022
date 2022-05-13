from pickle import FALSE
from tkinter import N


#nombre = input('Cuál es tu nombre: \r\n')

#print(f'Hola {nombre}')

#Leer datos  que seran números
#edad = input('Cuál es tu edad?')
#convertir edad (string) a int
#edad = int(edad)

#if edad >= 18:
    #print('Ya puedes votar')
#else:
    #print('Aún no puedes votar')

pregunta =  'Agrega un numero y te dire si es par o impar \r\n'
pregunta += '(Escribe "cerrar" para salir de la aplicación) \r\n'

preguntar = True
while preguntar:

#Mezclarlo con operadores

    numero = input(pregunta)
    
    if numero == 'cerrar':
        preguntar = False 
    else:
        numero = int(numero)

        if numero % 2 == 0:
            print (f'El número {numero} es par')
        else:
            print (f'El número {numero} es impar')