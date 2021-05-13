import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num3 and num2 >= num1:
    print(num2)
elif num3 >= num1 and num3 >= num2:
    print(num3)
