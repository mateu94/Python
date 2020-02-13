import json
from collections import Counter

months_relation = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "Setember",
        "10": "October",
        "11": "November",
        "12": "December"
        }

birthdays = {}
with open("birthdays.json", "r") as f:
    birthdays = json.load(f)

birthday_months = []
for key in birthdays:
    month = birthdays[key].split("/")
    birthday_months.append(months_relation[month[1]])

birthday_months_counter = Counter(birthday_months)
for month in birthday_months_counter:
    print(month, ": ", birthday_months_counter[month], sep = "")
