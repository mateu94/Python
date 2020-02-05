import random

number = random.randint(1000, 9999)

def guessNumber():
    cows, bulls = 0, 0
    guessed_number = input("Enter a number: ")
    cows = [(x,y) for x,y in enumerate(guessed_number) for xx,yy in enumerate(str(number)) if x == xx and y == yy]
    bulls = [y for x,y in enumerate(guessed_number) for xx,yy in enumerate(str(number)) if x != xx and y == yy]
    if len(cows) == len(str(number)):
        return True
    else:
        print(len(cows), "cows,", len(bulls), "bulls", sep = " ") 
    return False

if __name__ == "__main__":
    print("Welcome to the Cows and Bulls Game!")
    guessed = False
    while not guessed:
        guessed = guessNumber()
    print("Congratulations, the number was", number, sep = " ")
