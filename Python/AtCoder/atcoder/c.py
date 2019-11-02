import math
def isPrime(n):
    for k in range(2, int(math.sqrt(n))+1):
        if n % k == 0:
            return False
    return True
def searchMulti(n):
    i, j = 0, 0
    for x in range(2, n):
        if n % x == 0:
            y = n / x
            print(x, y)
            if y - x > 0:
                i = x
                j = y 
    return i, j
n = int(input())
if isPrime(n) == True:
    print(n-1)
else:
    i, j = searchMulti(n)
    print(i, j)
    print((i-1)+(j-1))