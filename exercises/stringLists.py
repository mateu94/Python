string = input("Enter a string: ")
reversedString = "".join(reversed(string))
if string == reversedString:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
