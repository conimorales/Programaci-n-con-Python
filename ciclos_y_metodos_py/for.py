buscar = 5
for i in range(10000000):
    if i == buscar:
        print("¡Elemento encontrado! Se saldrá del ciclo")
        break
    else:
        print("Elemento no encontrado")
print("Se ha salido del ciclo")

""" 
Elemento no encontrado
Elemento no encontrado
Elemento no encontrado
Elemento no encontrado
Elemento no encontrado
¡Elemento encontrado! Se saldrá del ciclo
Se ha salido del ciclo 
"""

for i in range(10):
    print("Iteración: ", i)

print("Utilizando 1 parámetro (stop)")
for i in range(3):
    print(i) # 0 1 2
print()

print("Utilizando 2 parámetros (start y stop)")
for i in range(1, 3):
    print(i) # 1 2
print()

print("Utilizando 3 parámetros (start, stop y step)")
for i in range(0, 10, 2):
    print(i) # 0 2 4 6 8


lista = list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
type(lista)
# list

#lista for
n_interno = 3
for i in range(n_interno):
    print("<li> {} </li>".format(i))    

#range es tipo range