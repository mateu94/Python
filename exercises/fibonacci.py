def fibonacci(num):
    a, b = 0, 1
    count = 0
    while count < num:
        print(b, end = " ")
        b_old = b
        b += a
        a = b_old
        count += 1

numbers = int(input("How many Fibonnaccis do you want? "))
fibonacci(numbers)
print("")
