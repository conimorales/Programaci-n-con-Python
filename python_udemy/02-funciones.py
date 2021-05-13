#funciones 
def information():
    print('soy constanza')
information()
# information(), se puede llamar más veces
# siempre se define y luego se llama a la función

def changeName(name,puesto):
    print(f'Soy {name} y soy {puesto}')
changeName('Constanza', 'desarrolladora')
changeName('Felipe', 'desarrollador')

#funciones que retornan un valor 
def information2(name2):
    return name2
empleado = information2('Constanza')

print(empleado)

#funciones y métodos 
nombre = 'Constanza'

def mostrar_nombre(nombre):
    print(f'Hola {nombre}')
mostrar_nombre(nombre)

print(nombre.upper())
print(nombre.title())

#Bienvenido 
print('Buen día')
nombre = input("Dime como te llamas: ")
print(f"Hola {nombre}, bienvenid@")
