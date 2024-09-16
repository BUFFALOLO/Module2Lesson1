"""
Python Indentation Practice with if Statements
Objective: The aim of this assignment is to understand the importance of indentation in Python, especially with if statements.
"""

# Task 1: Code Correction. Below is a piece of Python code with incorrect indentation. Your task is to corerct it
weather = "sunny"

if weather == "sunny":
    print("Wear Sunglasses!")
else:
    print("Take an umbrella!")

# Task 2: Your Mood Today. Ask the user how they feel today. If they say "happy", print "That's great to hear!", 
# and if they say "sad", print "I hope your day gets better!". Ensure your if statement is properly indented. 
# HINT: Use the input() function to ask the user how they feel! 

mood = input("How are you feeling today? ")

if mood == "happy":
    print("That's great to hear!")
elif mood == "sad":
    print("I hope your day gets better!")
else:
    print("Have a magical day!")
