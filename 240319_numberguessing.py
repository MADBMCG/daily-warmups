"""
Python Warmup Exercise: Number Guessing Game
Task:
Write a simple number guessing game where:

The program picks a random number between 1 and 10.
The user has 3 attempts to guess the number.
The program should give feedback if the guess is too high or too low.
If the user guesses correctly, print a congratulatory message and exit.
If the user fails to guess in 3 attempts, reveal the number.

Hints:
Use the random module to generate a number.
Use a loop to allow multiple guesses.
Use if statements to check if the guess is correct, too high, or too low.
"""
import random

print("I'm thinking of a number between 1 and 10. You have 3 attempts to guess it.")
number = random.randint(1,10)

for i in range(3):
    guess = int(input(f"Guess: "))
    if guess > number:
        print("Too high! Try Again :)")
    elif guess < number:
        print("Too low! Try again :)")
    elif guess == number:
        print("Congrats, you guessed it!")
        exit()

print(f"You're out of guesses! The number was {number}")
    
    