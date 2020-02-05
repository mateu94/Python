name = input("Enter your name please: ")
age = int(input("Enter your age please: "))
year = 2020 - age + 100
copies = input("Enter how many copies of the message you want: ")
for x in range(0,int(copies)):
   print("Hi", name, "in the year", year, "you will be 100")
