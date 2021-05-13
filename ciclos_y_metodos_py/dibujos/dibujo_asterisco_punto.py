import sys 

n= int(sys.argv[1])

contain = ""

for i in range(n):
    if i % 2 == 0:
        contain += "*"
    else:
        contain += "."


print(contain)