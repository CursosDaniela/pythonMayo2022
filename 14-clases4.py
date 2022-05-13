class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #atributo   
        self.categoria = categoria
        self.__precio = precio

    def mostrar_informacion(self):
        print(f'\r\n \r\n Nombre: {self.nombre},\r\n Categoria: {self.categoria}, \r\n Precio: {self.__precio}')

#GETTERS AND SETTERS - Get = obtiene un valor, SET = agrega un valor
    def get_precio(self):
        print(self.__precio)

    def set_precio(self, precio):
        self.__precio = precio

#Instaciar la clase
restaurant= Restaurant('Pizzeria', 'Italiana', 60)
restaurant.mostrar_informacion()
restaurant.set_precio(80)
restaurant.get_precio()

restaurant2 = Restaurant('Hamburguesa', 'Rapida', 20)
restaurant2.mostrar_informacion()
restaurant2.set_precio(50)
restaurant2.get_precio()


#crear una clase hijo
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel = Hotel('Hotel POO', '5 Estrellas', 200)
hotel.mostrar_informacion()