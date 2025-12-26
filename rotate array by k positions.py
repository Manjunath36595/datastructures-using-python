s=[1,2,3,4,5]

k = 118

k = k%len(s)
res = s[len(s)-k:] + s[:len(s)-k]
print(res)

"""
OUTPUT:

[4, 5, 1, 2, 3]

"""
