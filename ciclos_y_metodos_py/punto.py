import sys
n = int(sys.argv[1])
if n == 1:  
    print('*')
elif n == 2:
    print('**')
elif n == 3:
    print('***')
elif n == 4:
    print('****')
elif n == 5:
    print('*****')




import sys
n = int(sys.argv[1])
print('*' * n)



import sys

n = int(sys.argv[1])
contain = ""

for i in range(n):
    contain += '*'
print(contain)
