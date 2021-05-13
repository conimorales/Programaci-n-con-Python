saldo = 0
contador = 0
def depositar(cantidad):
    global saldo
    saldo += cantidad
    print(f"Tu saldo nuevo es de {saldo}")
    return saldo

def girar(cantidad):
    global saldo
    if saldo - giro <0:
            print(f"No puede realizar giros. Su saldo es {saldo}")  
    else:
        saldo -=  giro
        print(f"Giraste {giro}, y tu nuevo saldo es de {saldo}")

def mostrar_menu():
    print('Bienvenido al portal del Banco Amigo. Escoja una opción:\n ')
    print('1. Consultar saldo')
    print('2. Hacer depósito')
    print('3. Realizar giro')
    print('4. Salir')



while True:

    
    mostrar_menu()
    opcion = input("Inserta una opción: ")

    if opcion == "1":
        print(f'El saldo es {saldo}')

    elif opcion == "2":
        print(f"Tu saldo actual es de {saldo}")
        cantidad = int(input("Ingrese cantidad a depositar: "))
        depositar(cantidad)
        continue
        
    elif opcion == "3": 
        print(f"Tu saldo actual es de {saldo}")
        giro = int(input("Ingrese cantidad a girar: "))
        girar(cantidad)
        continue

    elif opcion == "4": 
        print("Saliendo")
        break
    else:
            print("Opción inválida. Por favor ingrese 1, 2, 3 ó 4.")
    
    contador = contador + 1