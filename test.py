import random
b="1,2"
a=tuple(map(int,b.split(",")))
r=random.randint(*a)
l=[random.randint(*a) for i in range(10)]
print(r)
print(l)
