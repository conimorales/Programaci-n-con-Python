a = "***** \n"
b = "*   * \n"
c = "*****"

def  letra_o(x):
    contain = ""
    for i in range(x):

        if i == 0:
            contain += a

        elif i == x-1:
                contain += c

        else:
            contain += b
    print(contain)

letra_o(5)


