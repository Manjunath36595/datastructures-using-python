n=int(input("Enter n value:"))
for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()

"""
OUTPUT:

Enter n value:5
*
**
***
****
*****

"""
