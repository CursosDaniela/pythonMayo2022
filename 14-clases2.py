class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #atributo   
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):
        print(f'\r\n \r\n Nombre: {self.nombre},\r\n Categoria: {self.categoria}, \r\n Precio: {self.precio}')

#Instaciar la clase
restaurant= Restaurant('Pizzeria', 'Italiana', 60)
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Hamburguesa', 'Rapida', 20)
restaurant2.mostrar_informacion()

