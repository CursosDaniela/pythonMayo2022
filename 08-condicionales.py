#revisar se una condición es mayor a 
balance = 0
if balance > 501:
    print('Puede pagar')
else:
    print('No tiene saldo')

#likes
likes = 200
if likes == 200:
    print('Excelente, 200 likes')
else:
    print('Ya casi llegas a los 200 likes')

#IF con texto
lenguaje = 'Python'
if not lenguaje == 'Python':
    print('Excelente decisión')

#Evaluar un Boolean
usuario_autenticado = True

if usuario_autenticado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesión')

#evaluar un elemento de una lista
lenguajes =['python', 'kotlin', ' java', 'javaScript']

if 'PHP' in lenguajes:
    print('PHP si existe')
else:
    print('No esta en la lista')

#Evaluar un Boolean
usuario_autenticado = True
usuario_admin = True

if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sesión')

#elif
ocupacion = 'Estudiante'

if ocupacion == 'Estudiante':
    print('Tienes un 50% de descuento')
elif ocupacion == 'Junilado':
    print('Tienes un 70% de descuento')
else:
    print('Debes paar el 100%')