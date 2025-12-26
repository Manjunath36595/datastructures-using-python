s=[1,2,3,2,1]


def palindrome(s):
    i=0
    j=len(s) - 1
    while i<j:
        if s[i] != s[j]:
            return "Not a palindrome"
        i+=1
        j-=1
    return "Palindrome" 
print(palindrome(s))   

"""OUTPUT:

 Palindrome

"""
