class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #atributo
        self.categoria = categoria #
        self.__precio = precio # Default: Public, Protected, Private

    def mostrar_info(self): 
        print(f'Nombre: {self.nombre}, categoría: {self.categoria}, precio: {self.__precio}')


restaurant = Restaurant('Pizzería Mexico', 'Comi italiana', 50) 

restaurant.__precio = 90 # se modifica en cualquier lado
restaurant.mostrar_info()

restaurant2 = Restaurant('Hamburguesas python', 'Comida casual', 100)

restaurant2.precio = 101119 # YA NO FUNCIONA
restaurant2.mostrar_info()