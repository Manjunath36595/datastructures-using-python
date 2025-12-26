s=[100,1,4,7,2,10,15,20,-1]
first_lar = float("-inf")
second_lar = first_lar
for num in s:
    if num > first_lar:
        second_lar = first_lar
        first_lar = num
    elif num < first_lar and num > second_lar:
        second_lar = num
print(second_lar)

"""
OUTPUT:

20

"""
