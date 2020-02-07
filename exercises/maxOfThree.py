
if __name__ == "__main__":
    numbers = list(map(int, input("Enter three numbers: ").split()))
    sorted_numbers = numbers.copy()
    sorted_numbers.sort(reverse = True) 
    print("The max of", numbers, "is", sorted_numbers[0])
