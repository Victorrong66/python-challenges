# Ask the user for their name and greet them.
name = input("What is your name? ")

# The f in the print statement allows for the variable in the {} to be 
# recognized as code/variable and not just text
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

# This one is a classic — it gets asked in real coding interviews. Print 
# every number from 1 to 20, but:

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

# Ask the user to enter 3 of their favorite foods one at a time, store 
# them in a list, then print the whole list.
foods = []
for i in range (1, 4):
    food = input("Enter food: ")
    foods.append(food)

print(f"Your favorite foods are: {foods}")

# 3/30/26
# Using the same foods list idea, ask the user for 3 foods again but 
# this time print:

# The first item in the list
# The last item in the list
# How many items are in the list

# Expected output:
# Enter food 1: Pizza
# Enter food 2: Ramen
# Enter food 3: Tacos
# First food: Pizza
# Last food: Tacos
# Total foods: 3

foods = []
for i in range (1,4) :
    food = input("Enter food: ")
    foods.append(food)

print(f"First food: {foods[0]}")
print(f"Last food: {foods[-1]}")
print(f"Total food: {len(foods)}")
# len() gets the count of the numbers in the list

# Write a function called greet that takes a name as input and prints 
# a greeting. Then call it three times with three different names.
def greet(name): # How you define functions
    print(f"Hello, {name}! Good to see you.")

greet("Victor")
greet("Sarah")
greet("Marcus")

# Write a function called multiply that takes two numbers, multiplies 
# them together, and returns the result. Then print the result outside 
# the function.

def multiply(num1, num2):
    product = num1 * num2
    return product
# using return allows for the value stored to be used in other places

result = multiply(4,6)
print(f"The result is: {result}")
# Printing becomes a dead end for values and cannot be used anywhere else

# This one combines everything from Stage 2 — lists, loops, and functions.

# Write a function called get_average that takes a list of numbers and 
# returns the average. Then build a list by asking the user for 4 numbers, call 
# the function, and print the result.

def get_average(num):
    return sum(num) / len(num)

nums = []
for i in range(1, 5):
    num = int(input(f"Enter number {i}: "))
    nums.append(num)

result = get_average(nums)
print(f"The average is: {result}")

# Build a shopping cart program that lets the user keep adding items until 
# they're done, then displays everything they added and the total count.

cart = []

while True:
    item = input("Enter item (or 'done' to finish) : ")
    if item == "done":
        break
    cart.append(item)

print(f"Your cart: {cart}")
print(f"Total items: {len(cart)}")

# Ask the user to enter 5 numbers one at a time, store them in a list, then print 
# the highest, lowest, and the average.

def getMaxAndMin(num):
    return max(num), min(num), sum(num) / len(num)
# Tuple unpacking: return three values from one function and unpack then later 
# all in one line

nums = []

for i in range (1, 6):
    num = int(input(f"Enter number {i}: "))
    nums.append(num)

maxNum, minNum, averageNum = getMaxAndMin(nums)
# Values get unpacked here
print(f"Highest: {maxNum}")
print(f"Lowest: {minNum}")
print(f"Average: {averageNum}")

# 3/31/26
# Ask the user to type a sentence, then tell them how many words are in it and 
# print each word on its own line numbered.

sentence = input(f"Enter a sentence: ")
words = sentence.split()

print(f"Word count: {len(words)}")

for index, word in enumerate(words, 1):
    print(f"{index}. {word}")


# Write a program that asks the user to create a password and checks if it's 
# strong enough. A strong password must:
#
# Be at least 8 characters long
# Contain at least one number
# 
# Keep asking until they enter a strong password.

while True:
    password = input("Enter a password: ")

    if len(password) < 8:
        print("Your password's too short, add more characters")
    elif not any(char.isdigit() for char in password): # any() with a loop inside is called a list comprehension style expression
        print("Add a number! Your password must contain at least one number")
    else:
        print("Password accepted")
        break

# Ask the user to enter 5 numbers, store them in a list, then print them in 
# both ascending and descending order.

nums = []

for i in range(1, 6):
    num = int(input(f"Enter number: "))
    nums.append(num)

# .sort() will sort the numbers you entered int the array
nums.sort()
ascendingNum = nums
# sort() will sort the nums and the reverse=True will reverse the numers 
# already in order
descendingNum = sorted(nums, reverse=True)

print(f"Ascending: {ascendingNum}")
print(f"Descending: {descendingNum}")

# The computer picks a random number between 1 and 10. The user keeps guessing 
# until they get it right. Tell them if they're too high or too low each time.

import random
randomNum = random.randint(1,10)

numTries = 0

while True:
    num = int(input("Guess a number between 1 and 10: "))

    if num > randomNum:
        print(f"You're too high! Try again")
        numTries += 1
    elif num < randomNum:
        print(f"You're too low! Try again")
        numTries += 1
    else:
        numTries += 1
        # The f in the print statement allows for the variable in the {} to be 
        # recognized as code/variable and not just text
        print(f"You got the number in {numTries}")
        break

# Ask the user to enter 6 numbers one at a time. If they enter a number that's 
# already in the list, tell them and don't add it. At the end print the final list.

nums = []

i = 1

while i  <= 6:
    num = int(input(f"Enter number {i}"))

    if num in nums:
        print(f"{num} has been already added to the list!")
    else:
        # putting the append and the increment inside the else statement will allow for
        # the number of tries to go up and the number to be added if it's not a duplicate
        nums.append(num)
        i += 1

print(f"Your list: {nums}")

# Create a dictionary called person with name, age, and city.
# Print each value using its key.

person = {"name": "Victor", "age": 27, "city": "Fredericksburg"}

# In print values, the dictionary item will be put in {} and you will write the dictionary
# Item in there
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")

# Dictionary items are written like this:
# person["name"] - Reading a value
#
# person["name"] = "New Name" - Updating a value
#
# person["job"] = "Network Technician"] - Adding a brand new key
# 

# Start with the same person dictionary, then:

# Update the city to a new city
# Add a brand new key called job
# Print the whole dictionary to see the result

person = {
    'name': 'Victor',
    'age': 27, 
    'city': 'Springfield',
}

person['city']= 'Fredericksburg'
person['job']= 'Network Technician'

print(person)

# Remember dictionary items need to have : to act as the = sign, 
# Outside the dictionary items, it can be =

# Create a dictionary with 3 of your favorite movies as keys and 
# their release years as values. Then loop through it and print each one.

movies = {
    'Iron Man': 2008,
    'The Amazing Spider-Man': 2012,
    'Project Hail Mary': 2026
}

# The key, value is how the dictionary items are separated
for key, value in movies.items():
    print(f"Movie: {key} - Year: {value}") #Enumeration method (enumerate())

# Create a list of 3 dictionaries, where each dictionary represents a 
# person with a name and score. Then loop through the list and print each 
# person's name and score.
#
# Ex: Victor scored 95
#     Sarah scored 87
#     Marcus scored 72

scores = [
    {'name': 'victor', 'score': 95}, 
    # Each dictionary item in the list needs to be written out like this if
    # everything is associated to each other
    {'name': 'sarah', 'score': 87},
    {'name': 'marcus', 'score': 72}
]

# You call the entire list name and you change it to person to change it to one
# dictionary item each time it loops
for person in scores:
    print(f"{person['name']} scored {person['score']}")


# Create a dictionary of 4 countries and their populations. Then:
#
# Print all the keys
# Print all the values
# Check if a specific country is in the dictionary
#
# Ex: 
# Countries: dict_keys(['USA', 'China', 'Japan', 'Brazil'])
# Populations: dict_values([331000000, 1400000000, 125000000, 213000000])
# Is Germany in the list? False
# Is Japan in the list? True

population = {
    'USA': 331000000,
    'China': 1400000000,
    'Japan': 125000000,
    'Brazil': 213000000
}

# .keys() allows you to pull just keys item in the dictionary
countries = population.keys() 

# .values() allows you to pull just the values item of the dictionary
populationSize = population.values() 

# List out the list of values that are associated to the variable
print(f"Countries: {countries}")
print(f"Populations: {populationSize}")


# prints out true or false after comparing if the keys item is one of the dictionary items
print(f"Is Germany in the list? {'Germany' in countries}")
print(f"is Japan in the list? {'Japan' in countries}")