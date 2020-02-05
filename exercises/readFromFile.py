
list_names = {}

with open("namesList.txt", "r") as names:
    name = names.readline().strip()
    while name:
        if not name in list_names:
            list_names[name] = 1
        else:
            list_names[name] += 1
        name = names.readline().strip()

print(list_names)
        
