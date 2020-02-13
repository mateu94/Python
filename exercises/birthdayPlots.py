import json
from bokeh.plotting import figure, show, output_file
from collections import Counter

output_file("plot.html")

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

x_categories = [month for month in months_relation.values()]
x = [month for month in birthday_months_counter.keys()]
y = [month_count for month_count in birthday_months_counter.values()]

p = figure(x_range = x_categories, plot_width = 1000)

p.vbar(x=x, top=y, width=0.5)

show(p)


