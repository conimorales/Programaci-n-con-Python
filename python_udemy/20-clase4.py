class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #atributo
        self.categoria = categoria #
        self.__precio = precio # Default: Public, Protected, Private

    def mostrar_info(self): 
        print(f'Nombre: {self.nombre}, categoría: {self.categoria}, precio: {self.__precio}')

    #getter y setter - get: obtiene un valor, set: agrega un valor
    def get_precio(self):
        print(self.__precio)
    
    def set_precio(self, precio):
        self.__precio = precio

restaurant = Restaurant('Pizzería Mexico', 'Comi italiana', 50)
restaurant.mostrar_info()
restaurant.set_precio(80)
restaurant.get_precio()

restaurant2 = Restaurant('Hamburguesas python', 'Comida casual', 100)
restaurant2.mostrar_info()
restaurant2.get_precio()