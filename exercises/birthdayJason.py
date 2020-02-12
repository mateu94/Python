import json

with open("birthdays.json", "r") as f:
    birthdays = json.load(f)

def addBirthday(birthdays):
    name = input("Enter the name: ")
    date = input("Enter the date: ")
    birthdays[name] = date
    with open("birthdays.json", "w") as f:
        json.dump(birthdays, f)

option = input("What do you want to do with the birtday list? Add/List/Exit: ").capitalize()
while option is not "Exit":
    if option == "Add":
        addBirthday(birthdays)
    elif option == "List":
        for key in birthdays:
            print(key, birthdays[key])
    elif option == "Exit":
        break
    option = input("What do you want to do with the birtday list? Add/List/Exit: ").capitalize()

