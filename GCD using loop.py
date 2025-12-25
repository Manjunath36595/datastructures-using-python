def gcd(n, m, x):
    for i in range(x, 0, -1):
        if n % i == 0 and m % i == 0:
            return i

print(gcd(15, 20, 15))


"""
OUTPUT:

5

"""
