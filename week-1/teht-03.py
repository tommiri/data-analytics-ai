import random

a = random.randint(0, 100)
b = random.randint(0, 100)

print (f'a: {a}')
print (f'b: {b}')

if (a > b):
    print('a is greater than b!')
elif (a < b):
    print('b is greater than a!')
else:
    print('a and b are equal!')
