import sys

limit = int(sys.argv[1])

a = "(>'-')> "
b = "(¨-¨)"

contain = ""


for i in range(limit):

    if i % 3 == 0:
        contain += a

    else:
        contain += b
 
print(contain)
