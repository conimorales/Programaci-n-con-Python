import sys


limit = int(sys.argv[1])

a = "o***o \n"
b = "*.*.* \n"



contain = ""


for i in range(limit):

    if i == 0:
        contain += "##### \n"

    elif i % 4 == 0:
        contain += b

    else:
        contain += a

contain += "##### \n"

print(contain)
