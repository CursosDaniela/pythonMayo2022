class Restaurant:

    def agregar_restaurant(self, nombre):
        self.nombre = nombre #atributo

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')

#Instaciar la clase
restaurant= Restaurant()
restaurant.agregar_restaurant('Pizzeria')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Hamburguesa')
restaurant2.mostrar_informacion()

#mostrar la información
print(f'Nombre Restaurante: {restaurant.nombre}')
