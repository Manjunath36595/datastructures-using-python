n = [1, 2, 5, 1, 4, 3, 6, 5]
res = {}
for num in n:
    if num not in res:
        res[num] = 1
    else:
        res[num] = res[num] + 1
print(res)

"""
OUTPUT:

{1: 2, 2: 1, 5: 2, 4: 1, 3: 1, 6: 1}


"""
