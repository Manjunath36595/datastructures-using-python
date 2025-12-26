s = [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1]
count = 0
res = 0
for num in s:
    if num == 1:
        count += 1
    else:
        if count > res:
            res = count
        count = 0
if count > res:
    res = count
print(res)
