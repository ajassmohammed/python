import math

def primeCheck(x):
    status = 1
    for i in range(2, int(math.sqrt(x)) +1):
        if x % i ==0:
            status = 0
            print("Not Prime")
            break
        else:
            continue
    if status == 1:
        print("prime")
    return status
num = int(input("Enter the number: "))
ret = primeCheck(num)


