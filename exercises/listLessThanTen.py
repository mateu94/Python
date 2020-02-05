a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
elems_less_than_five = [(x) for x in a if x < 5] 
print([(x) for x in a if x < 5])
#for x in a:
#    if x < 5:
#        elems_less_than_five.append(x)
print(elems_less_than_five)

threshold = int(input("Enter a threshold: "))
print([(x) for x in a if x < threshold])
