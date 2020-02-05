
if __name__ == "__main__":
    number = int(input("Enter a number between 0 and 100: "))
    while number < 0 and number > 100:
        number = int(input("You must enter a number between 0 and 100, enter it again: "))

    guess = 50
    tries = 0
    print("My guess is ", guess)
    result = input("How is my guess? Too high(1), too low(2), or correct(0): ")
    while result != "0":
        print("My guess is ", guess)
        result = input("How is my guess? Too high(1), too low(2), or correct(0): ")
        
