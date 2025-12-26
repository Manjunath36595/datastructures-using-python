s=[1,34,56,23,56,0,1,2,7]

s1=[]
s2=[]
for num in s:
    if num%2 == 0:
        s1.append(num)
    else:
        s2.append(num)

print(s1)
print(s2)

"""
OUTPUT:

[34, 56, 56, 0, 2]
[1, 23, 1, 7]

"""
