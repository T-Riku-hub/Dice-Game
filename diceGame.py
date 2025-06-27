import random

print("What is your name?")
name = input("> ")
print(f'Hello, {name}!')
print("Rolling dice...")
a = random.randint(1,6)
b = random.randint(1,6)
total=a+b
print(f'Die 1: {a}')
print(f'Die 2: {b}')
print(f'Total value : {total}')
if(total>=7):
    print(f"{name} won!")
else:
    print(f"{name} lost")