#Method-1

s1 = [1, 2, 5, 7]
s2 = [3, 6, 8,9]
i = 0
j = 0
res = []
while i < len(s1) and j < len(s2):
    if s1[i] < s2[j]:
        res.append(s1[i])
        i += 1
    else:
        res.append(s2[j])
        j += 1
while i < len(s1):
    res.append(s1[i])
    i += 1
while j < len(s2):
    res.append(s2[j])
    j += 1

print(res)



#Method-2


s1 = [1, 2, 5, 7]
s2 = [3, 6, 8, 10]
s = s1 + s2

s.sort()
print(s)

print(sorted(s))



"""
output:

[1, 2, 3, 5, 6, 7, 8, 9]
[1, 2, 3, 5, 6, 7, 8, 10]
[1, 2, 3, 5, 6, 7, 8, 10]

"""









