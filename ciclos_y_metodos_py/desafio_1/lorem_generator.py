#Constanza Morales
#Lorem
n = int(input("Ingrese la cantidad de parametros: \n"))


lorem = ""
for i in range(1,n+1,1):

    lorem += "<p> Parrafo {}: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ac lacinia nibh, nec faucibus enim. Nullam quis lorem posuere, hendrerit tellus eget, tincidunt ipsum. Nam nulla tortor, elementum in elit nec, fermentum dignissim sapien.</p>.\n".format(i)
   

print(lorem)
