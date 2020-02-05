import random

a = random.sample(range(1,100), 15)
b = random.sample(range(1,100), 20)
print(a)
print(b)

c = ([x for x in set(a) if x in b])
print(c)
