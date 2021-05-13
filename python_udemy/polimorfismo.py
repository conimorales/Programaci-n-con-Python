class Animal: 
    def __init__(self, nombre, edad, raza):
        self.__nombre = nombre
        self.__edad = edad
        self.__raza = raza
    
    def mostrar_informacion(self):
        print(f"""
        ### Descripción de la mascota
            Nombre: {self.__nombre}
            Edad: {self.__edad}
            Raza: {self.__raza}
        ###
        """)
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_edad(self, edad):
        self.__edad = edad
    def set_raza(self, raza):
        self.__raza = raza

conejo = Animal('Bella', '5 meses', 'Conejo polish')

conejo.set_nombre('Coco Pipo')
conejo.set_edad('4 meses')
conejo.set_raza('Cabeza de león')

conejo.mostrar_informacion()

#POLIMORFISMO

class Humano(Animal):
    def __init__(self, nombre, edad, raza, carrera):
        super().__init__(nombre, edad, raza)
        self.__nombre = nombre
        self.__edad = edad
        self.__raza = raza
        self.carrera = carrera
 
    
    def get_carrera(self):
        return self.carrera

    
    def mostrar_informacion(self):
        print(f"""
        ### Descripción de la Humano
            Nombre: {self.__nombre}
            Edad: {self.__edad}
            Raza: {self.__raza}
            Carrera: {self.carrera}
        ###
        """)


humano1 = Humano('Constanza', '24', 'Blanca', 'Ingeniería industrial')

humano1.mostrar_informacion()