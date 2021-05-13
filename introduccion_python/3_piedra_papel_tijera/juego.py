import sys
import random

ingreso = str(sys.argv[1])
aleatorio = int(random.randint(1,3))

uno = "piedra"
dos = "papel"
tres = "tijera"

if ingreso == "piedra" and aleatorio == 1:
    print("Computador juega {}".format(uno))
    print("Empataste")
elif ingreso == "piedra" and aleatorio == 2:
    print("Computador juega {}".format(dos))
    print("Perdiste")
elif ingreso == "piedra" and aleatorio == 3:
    print("Computador juega {}".format(tres))
    print("Ganaste")

elif ingreso == "papel" and aleatorio == 2:
    print("Computador juega {}".format(dos))
    print("Empataste")
elif ingreso == "papel" and aleatorio == 3:
    print("Computador juega {}".format(tres))
    print("Perdiste")
elif ingreso == "papel" and aleatorio == 1:
    print("Computador juega {}".format(uno))
    print("Ganaste")
    
elif ingreso == "tijera" and aleatorio == 3:
    print("Computador juega {}".format(tres))
    print("Empataste")
elif ingreso == "tijera" and aleatorio == 1:
    print("Computador juega {}".format(uno))
    print("Perdiste")
elif ingreso == "tijera" and aleatorio == 2:
    print("Computador juega {}".format(dos))
    print("Ganaste")

    



    
    



