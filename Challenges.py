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

# Ask the user for a temperature in Celsius and convert it to Fahrenheit.
temp = float(input("Enter temperature in Celcius: "))

tempInFahrenheit = (temp * (9/5) + 32)

print(f"{temp} degrees Celsius is {tempInFahrenheit} degrees Fahrenheit")

# This one is a classic — it gets asked in real coding interviews. Print every number from 1 to 20, but:

# If divisible by 3, print Fizz
# If divisible by 5, print Buzz
# If divisible by both 3 and 5, print FizzBuzz
# Otherwise print the number

for i in range (1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(f"Fizzbuzz")
    elif i % 3 == 0:
        print(f"Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Ask the user to enter 3 of their favorite foods one at a time, store them in a list, then print the whole list.
foods = []
for i in range (1, 4):
    food = input("Enter food: ")
    foods.append(food)

print(f"Your favorite foods are: {foods}")