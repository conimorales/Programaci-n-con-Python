n= 6
contain=''

for i in range(n + 1):
    contain += "*" * i + "\n"
print(contain)
contain=''

for i in range(n):
    for j in range(n - i):
        contain += '*'
    contain += '\n'
print(contain)