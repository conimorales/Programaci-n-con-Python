nombre = input('Cuál es tu nombre: \r\n ')
print(f'Hola {nombre}')

# leer datos que serán números

edad = input('Cuál es tu edad?')
edad = int(edad)

if edad >= 18:
    print('Ya puedes votar')
else:
    print('No puedes votar')
    
# número par o impar
numero = input('Ingresa un número, para conocer si es par o impar: ')
numero = int(numero)

if numero % 2 == 0:
    print(f'El número {numero} es par')
else:
    print(f'El número {numero} es impar')