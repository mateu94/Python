def isPrime(number, numberRange):
    for x in numberRange:
        if not number%x:
            return False
    return True

number = int(input("Give me a number: "))
possible_divisors = range(2, number//2+1)
if isPrime(number, possible_divisors):
    print(str(number), "is prime")
else:
    print(str(number), "is not prime")
    
