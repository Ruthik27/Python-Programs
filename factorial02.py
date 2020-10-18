def fact(n):
    if n == 0: # base
        return 1
    else: #recursion
        return n*fact(n-1) #pause and go back to factorial function
n = int(input("Enter the number: "))
result = fact(n)
print("factorial of ",n , "is" , result)
