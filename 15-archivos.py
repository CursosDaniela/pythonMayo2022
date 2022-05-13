def app():
    archivo = open('archivo.txt', 'w') #w es archivo de escrituta

    #generar numeros en una archivo
    for i in range(0, 20):
        archivo.write('Esta es la linea ' + str(i)+ "\r\n" )

    #cerrar un archivo
    archivo.close()

    

app()