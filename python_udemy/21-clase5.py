class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #atributo
        self.categoria = categoria #
        self.__precio = precio 

    def mostrar_info(self): 
        print(f'Nombre: {self.nombre}, categoría: {self.categoria}, precio: {self.__precio}')

    def get_precio(self):
        print('Precio por getter:' f'{self.__precio}')
    
    def set_precio(self, precio):
        self.__precio = precio

#clase hijo
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel = Hotel('Hotel', '5 estrellas', 200)
hotel.mostrar_info()