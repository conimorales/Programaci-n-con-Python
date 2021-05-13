#ciclo anidado
for i in range(10):
    print("5 * {} = {}".format(i, (5 * i)))


for i in range(10):
    for j in range(10):
        print("{} * {} = {}".format(i,j, (j * i)))
