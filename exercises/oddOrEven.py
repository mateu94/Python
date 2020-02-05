number = int(input("Enter a number: "))
if not(number%4):
    print(str(number), "is multiple of 4")
elif number%2:
    print(str(number) + " is odd")
else:
    print(str(number) + " is even")
    
num = int(input("""\
Now enter two numbers.
First number: 
"""))
check = int(input("Second number: "))
if num%check:
    print(str(check), "divides oddly into ", str(num))
else:
    print(str(check), "divides evenly into ", str(num))
