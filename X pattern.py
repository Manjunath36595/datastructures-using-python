n=int(input("Enter n value:"))
for i in range(n):
    for j in range(n):
        if i == j or j == n - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



"""
OUTPUT:

Enter n value:7
*           * 
  *       *   
    *   *     
      *       
    *   *     
  *       *   
*           * 



"""
