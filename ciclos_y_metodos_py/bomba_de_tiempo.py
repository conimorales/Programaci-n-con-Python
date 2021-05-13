import time
i = 5
while i > 0:
    i -=1 # En cada iteración descontamos 1.
    print(i)
    time.sleep(1)
    if i == 0:
        print("BOOM!")