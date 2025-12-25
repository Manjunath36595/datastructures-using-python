a = 15
b = 20
n = a
m = b
while n != m:
    if n > m:
        n = n - m
    else:
        m = m - n
gcd = n
lcm = (a * b) // gcd
print(lcm)


"""
OUTPUT:

60


"""
