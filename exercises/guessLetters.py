import random

def enterLetter(word_letters, guessed_letters, correct_letters, word_game):
    letter = input("Enter a capital letter: ")
    while letter in guessed_letters or letter.islower():
        if letter.islower():
            letter = input("The letter you have entered was lowercase, enter a capital letter: ")
        elif letter in guessed_letters:
            letter = input("The letter you have entered was already used before, enter another letter: ")
    guessed_letters.add(letter)
    for i, val in enumerate(word_letters):
        if val == letter:
            word_game[i] = letter

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
    word_letters_count = len(word_letters)
    guessed_letters = set() 
    correct_letters = []
    correct_letters_count = 0
    word_game = ["_" for x in word_letters]

    print(word_game)
   
    while correct_letters_count < word_letters_count:
        for letter in word_game:
            print(letter, end = " ")
        print("")
        enterLetter(word_letters, guessed_letters, correct_letters, word_game)
        correct_letters_count = len(word_game) - word_game.count("_")
    print("Correct, the word was", word)
            
