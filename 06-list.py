lenguajes =['python', 'kotlin', ' java', 'javaScript']
print(lenguajes)

#llamar cada elemento
print(lenguajes[0])

#ordenar los elementos
lenguajes.sort()
print(lenguajes)

#acceder a un elemento de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[0]}'

#modificando valores de una list
lenguajes[2] = 'PHP'
print(lenguajes)

#Agregar elementos a una list
lenguajes.append('Ruby')
print(lenguajes)

#Eliminar
del lenguajes[1]
print(lenguajes)

#Eliminar (pop) (elimina por default la ultima posición, tambien se le puede dar una posición)
lenguajes.pop()
print(lenguajes)

#Eliminar por nombre 
lenguajes.remove('PHP')
print(lenguajes)

