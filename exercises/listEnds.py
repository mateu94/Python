import random

def firstAndLast(l):
    return [l[0], l[len(l)-1]]

a = random.sample(range(1,100), 15)
print("a:", a)
print(firstAndLast(a))

