# Ask the user for their name and greet them.
name = input("What is your name? ")

print(f"Hello, {name}! Welcome to Python")

# Ask the user for their age and tell them how many days they've been alive.
age = int(input("How old are you? "))

ageInDays = age * 365

print(f"You have been alive for approximately {ageInDays} days")

# Ask the user for a number and tell them if it's odd or even.]
num = int(input("Enter a number: "))

if num % 2 != 0:
    print(f"{num} is odd")

else:
    print(f"{num} is even")
