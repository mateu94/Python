number = int(input("Enter a number: "))
listRange = list(range(1,number+1))
divisors = []
for x in listRange:
    if not number % x:
        divisors.append(x)

print("Divisors of", str(number) + ":", divisors)
