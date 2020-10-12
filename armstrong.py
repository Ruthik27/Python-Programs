for i in range(1001): #loop added so it continues till it reaches end of range
    num = i # initializing num as i
    result = 0 # and result to zero so it does not hold previous value
    n = len(str(i)) # to get num vo digit, converting it to strg and then getting its length
    while (i!=0): # continue loop till i is not equal to zero, when it coes zero it goes forward
        digit = i %10 # using 10 modulus so to get last digit
        result = result + digit ** n #adding  on the cubes
        i = i // 10 # eliminating the used number (trunket div= gives only int part)
    if num == result: 
        print(num)
