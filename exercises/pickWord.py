import random

if __name__ == "__main__":
    word_list = []
    with open("sowpods.txt", "r") as f:
        line = f.readline().strip()
        while line:
            word_list.append(line)
            line = f.readline().strip()

    word = random.choice(word_list)
    print(word)
            
