
MIN = 0
MAX = 100

if __name__ == "__main__":
    number = int(input("Enter a number between 0 and 100: "))
    while number < 0 and number > 100:
        number = int(input("You must enter a number between 0 and 100, enter it again: "))

    left = MIN
    right = MAX
    guess = 50
    tries = 0
    print("My guess is ", guess)
    result = input("How is my guess? Too high(1), too low(2), or correct(0): ")
    while result != "0":
        if result == "1":
            right = max(guess - 1, MIN)
        elif result == "2":
            left = min(guess + 1, MAX)
        else:
            result = input("You must indicate too high(1), too low(2) or correct(0): ")
            continue
        guess = (left + right) // 2
        tries += 1
        print("My guess is ", guess)
        result = input("How is my guess? Too high(1), too low(2), or correct(0): ")
        
    print("I tried", tries, "times")
