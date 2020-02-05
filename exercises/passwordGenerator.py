#!/usr/bin/env python3.6

import random
import string

possibilities = []
possibilities.append(list(string.ascii_lowercase))
possibilities.append(list(string.ascii_uppercase))
possibilities.append(list(string.digits))
possibilities.append(list(string.punctuation))

length = int(input("Enter the length desired for the password: "))
choices2 = random.choices(range(0,len(possibilities)), k=length)
for x in choices2:
    print(random.choice(possibilities[x]), end="")

print("")
