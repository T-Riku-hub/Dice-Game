import random
print("Rolling dice...")
a = random.randint(1,6)
b = random.randint(1,6)
total=a+b
print(f'Die 1: {a}')
print(f'Die 2: {b}')
print(f'Total value : {total}')
if(total>=7):
    print("You won!")
else:
    print("You lost")