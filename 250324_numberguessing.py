""" 
Number Guessing Game Exercise
Time Estimate: 10-15 minutes

Task Description:
Create a simple number guessing game where:
The program generates a random number between 1 and 100
The player gets 7 attempts to guess the correct number
After each guess, the program should tell the player if their guess was too high or too low
The game should end when either:
The player guesses the correct number (they win!)
The player runs out of attempts (they lose)

Requirements:
Use a while loop
Use if/elif/else statements
Use the random module
Keep track of the number of attempts remaining
Print appropriate messages to guide the player
"""
import random

print("I'm thinking of a number between 1 and 100. You have 7 attempts to guess it.")
number = random.randint(1,100)

attempt = 1
while attempt <= 7:
    guess = int(input(f"Guess {attempt}: "))
    if guess == number:
        print(f"You guessed it! The number was {number}")
        break

    if attempt == 7:
        print(f"Sorry, you're out of guesses! The number was {number}.")
    else:
        if guess > number:
            print(f"Too high! Try again :)")
        else:  # guess < number
            print(f"Too low! Try again :)")

    attempt += 1
