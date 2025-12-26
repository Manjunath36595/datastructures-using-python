s={1,4,10,25,67}
for num in s:
    print(num,(hash(num)%len(s)))
    
print(s)

"""
OUTPUT:

1 1
67 2
4 4
25 0
10 0
{1, 67, 4, 25, 10}

"""
