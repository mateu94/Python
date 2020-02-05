import random

def removeDuplicatesNoSet(a):
    a_no_duplicates = []
    for x in a:
        if x not in a_no_duplicates:
            a_no_duplicates.append(x)
    return a_no_duplicates

def removeDuplicatesSet(a):
    return list(set(a))

a = sorted([random.choice(range(30)) for i in range(10)])
print(a)
print("The list without duplicates is:", removeDuplicatesNoSet(a))
print("Again, the list without duplicates is:", removeDuplicatesSet(a))
