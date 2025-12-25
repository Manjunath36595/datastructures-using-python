import math
def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
for i in range(2, 11):
    if check_prime(i):
        print(i, end=" ")


"""
OUTPUT:

2 3 5 7 

"""
