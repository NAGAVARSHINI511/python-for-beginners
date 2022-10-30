for n in range(1,101):
    if(n%3==0 and n%5==0):
     print("FizzBuzz")
    elif(n%3==0): #if the num is divisible by 3 reminder is 0
     print("Fizz")
    elif(n%5==0): #if the num is divisible by 5 reminder is 0
     print("Buzz")
    else:
     print(n)
