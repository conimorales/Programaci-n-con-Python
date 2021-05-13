
def mostrar_menu(saldo=0):
    print('Bienvenido al portal del Banco Amigo. Escoja una opción:\n ')
    print('1. Consultar saldo')
    print('2. Hacer depósito')
    print('3. Realizar giro')
    print('4. Salir')


saldo = 0

while True:


    
    mostrar_menu()
    opcion = input("Inserta una opción: ")
    

    if opcion == "1":
        print(f'El saldo es {saldo}')
# deposito
    elif opcion == "2":
        print(f"Tu saldo actual es de {saldo}")
        cantidad = int(input("Ingrese cantidad a depositar: "))
        saldo += cantidad
        print(f"Tu saldo nuevo es de {saldo}")

    

    elif opcion == "3": 
        print(f"Tu saldo actual es de {saldo}")
        giro = int(input("Ingrese cantidad a girar: "))
        if saldo - giro <0:
            print(f"No puede realizar giros. Su saldo es {saldo}")
            
        else:
            saldo -= giro
            print(f"Giraste {giro}, y tu nuevo saldo es de {saldo}")

    elif opcion == "4": 
        print("Saliendo")
        break
    else:
        print("Opción inválida. Por favor ingrese 1, 2, 3 ó 4.")