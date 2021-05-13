class Restaurant:
    def agregar_restaurant(self, nombre): #self el mismo objeto se pasa
        #print('agregandooo') #llamar funcion 
        self.nombre = nombre #atributo de la clase 

    def mostrar_info(self): 
        print(f'Nombre: {self.nombre}')


#instanciar la clase
restaurant = Restaurant()
print(restaurant) #imprime el objeto
restaurant.agregar_restaurant('Pizzería Mexico') #es obligatorio

restaurant.mostrar_info()

restaurant2 = Restaurant() # 2da instancia y objeto
restaurant2.agregar_restaurant('Hamburguesas python')
restaurant2.mostrar_info()

#mostrar la información
print (f'Nombre Restaurant: {restaurant.nombre}')
print (f'Nombre Restaurant: {restaurant2.nombre}')