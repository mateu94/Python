import random


def enterLetter(word_letters, guessed_letters, word_game, maximum_guesses):
    letter = input("Enter a capital letter: ")
    while letter in guessed_letters or letter.islower():
        if letter.islower():
            letter = input("The letter you have entered was lowercase, enter a capital letter: ")
        elif letter in guessed_letters:
            letter = input("The letter you have entered was already used before, enter another letter: ")
    guessed_letters.add(letter)
    found = False
    for i, val in enumerate(word_letters):
        if val == letter:
            word_game[i] = letter
            found = True
    if not found:
        maximum_guesses -= 1
    return maximum_guesses

def readWords(file_name):
    word_list = []
    with open(file_name, "r") as f:
        line = f.readline().strip()
        while line:
            word_list.append(line)
            line = f.readline().strip()
    return word_list

if __name__ == "__main__":
    print("Welcome to Hangman")
    word_list = readWords("sowpods.txt")
    word = random.choice(word_list)
    word_letters = list(word)
    guessed_letters = set() 
    word_game = ["_" for x in word_letters]
    maximum_guesses = 6

    print(word_game)
   
    while maximum_guesses:
        for letter in word_game:
            print(letter, end = " ")
        print("")
        maximum_guesses = enterLetter(word_letters, guessed_letters, word_game, maximum_guesses)
        if len(word_game) == word_game.count("_"):
            print("Correct, the word was", word)
            break

    if not maximum_guesses:
        print("Hanged, the word was", word)
