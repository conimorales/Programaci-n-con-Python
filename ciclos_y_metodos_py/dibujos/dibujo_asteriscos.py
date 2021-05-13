n = 5
contain = ''
for i in range(n):
    contain += '*'
print(contain)


contain_middle = "*" # Se inicia con el primer asterisco
# Se llena con espacios en blanco, que será la cantidad ingresada - 2 (se restan los
# espacios destinados para los asteriscos del principio y del final)
for i in range(n - 2):
    contain_middle += " "
contain_middle += "*\n" # Se concatena con el asterisco final y se agrega el salto de línea
print(contain_middle)

n = 5
contain_middle = "*"

for j in range(n - 2):
    contain_middle += " "
contain_middle += "*\n"

print(contain_middle * (n - 2))



n = 5
contain_bounds = ''
for i in range(n):
    contain_bounds += '*'

contain_middle = "*"

for j in range(n - 2):
    contain_middle += " "
contain_middle += "*\n"

print(contain_bounds)
print(contain_middle * (n - 2))
print(contain_bounds)
