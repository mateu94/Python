import random

def searchNumber(numbers, number):
    print(numbers)
    if numbers.count(number):
        print(number, "is in the list")
    else:
        print(number, "is not in the list")

if __name__ == "__main__":
    numbers = random.sample(range(0,30), 20)
    numbers.sort()
    number_to_search = int(input("Enter a number to search: "))
    searchNumber(numbers, number_to_search)
