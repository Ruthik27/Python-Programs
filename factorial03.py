n = int(input("Enter the number : "))
result = 1
for i in range(n,0,-1): #using loop
    result = result*i # loop will carry on

print("factorial of", n , "is", result )
