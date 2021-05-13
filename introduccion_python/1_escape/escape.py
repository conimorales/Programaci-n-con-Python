import sys
import math

g = float(sys.argv[1])
r = float(sys.argv[2])

calculo = math.sqrt(2*g*r*1000)

redondeo= round(calculo,3)

print(redondeo)
