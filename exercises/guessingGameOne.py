import random

while True:
    a = random.randint(1,9)
    print("Random number generated between 1 and 9, type exit to quit the game")
    tries = 0
    while True:
        try:
            inputData = input("Enter your guess: ")
            if inputData == "exit":
                break
            guess = int(inputData)
        except ValueError:
            print("You must enter an integer or exit to quit the game")
        else:
            break
    if inputData == "exit":
        break
    while inputData != "exit" and guess != a:
        tries += 1
        if guess < a:
            print("Your guess was below the random number")
        elif guess > a:
            print("Your guess was above the random number")
        while True:
            try:
                inputData = input("Enter your guess again (exit to quit): ")
                if inputData == "exit":
                    break
                guess = int(inputData)
            except ValueError:
                print("You must enter an integer or exit to quit the game")
            else:
                break
    if inputData == "exit":
        break
    print("You have guessed", str(tries), "times")
