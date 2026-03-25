# Print() displays text in the terminal
# \n means to make a new line and it can be used to make a blank line for spacing
print("Welcome to Mad Libs")
print("Answer the questions and I'll tell you a story. \n")

# input() pauses the program and waits for the user to type something
# Whatever they type gets stored in the variable on the left
name = input("Enter a person's name: ")
adjective1 = input("Enter an adjective (describing word): ")
animal = input("Enter an animal: ")

# Variables can be named anything -- just keep them descriptive
verb = input("Enter a verb (action word): ")
place = input("Enter a place: ")
adjective2 = input("Enter another adjective: ")
food = input("Enter a food: ")

# \n at the start adds a blank line before the story begins
print("\n---Your Story---\n")

# f-strings start with the letter f before the quote
# Anything inside {} gets replaed with the variable's value
# This is Python's version of JavaScript's template literals '${variable}'
print(f"One day, {name} woke up feeling very {adjective1}")
print(f"They looked outside and saw a {animal} trying to {verb} across the street.")
print(f"They decided to follow it all the way to {place}.")
print(f"the {place} was incredibly {adjective2}, and smelled like {food}.")

# You can use the same variable more than once
print(f"'{animal}s are so weird,' said {name}. 'But I love them anyway.'")
print("\n---The End---")