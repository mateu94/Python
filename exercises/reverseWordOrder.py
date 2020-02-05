def reverseOrder(string):
    return "a".join(string.split()[::-1])

string = input("Enter multiple words: ")
print(reverseOrder(string))
