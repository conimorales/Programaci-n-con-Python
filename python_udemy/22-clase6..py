class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #atributo
        self.categoria = categoria #
        self.precio = precio 

# Reescribir un método que tiene que llamarse igual
    def mostrar_info(self): 
        print(f'Nombre: {self.nombre}, categoría: {self.categoria}, precio: {self.precio}, alberca: {self.alberca}')

    def get_precio(self):
        print('Precio por getter:' f'{self.precio}')
    
    def set_precio(self, precio):
        self.precio = precio

#clase hijo constructor
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca 

    def get_alberca(self):
        return self.alberca

hotel = Hotel('Hotel', '5 estrellas', 200, 'Si')
hotel.mostrar_info()
alberca = hotel.get_alberca()
print(alberca)