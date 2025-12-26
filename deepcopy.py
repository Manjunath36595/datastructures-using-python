import copy
s=[1,2,[300,400]]

s2=copy.deepcopy(s)

s[2][0]=500
print(s)
print(s2)

"""
OUTPUT:

[1, 2, [500, 400]]
[1, 2, [300, 400]]

"""
