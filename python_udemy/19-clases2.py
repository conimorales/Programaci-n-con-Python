class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #atributo
        self.categoria = categoria 
        self.precio = precio

    def mostrar_info(self): 
        print(f'Nombre: {self.nombre}, categoría: {self.categoria}, precio: {self.precio}')


restaurant = Restaurant('Pizzería Mexico', 'Comi italiana', 50) 
restaurant.mostrar_info()

restaurant2 = Restaurant('Hamburguesas python', 'Comida casual', 100)
restaurant2.mostrar_info()