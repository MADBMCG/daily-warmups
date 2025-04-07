""" 
Task:
Create a simple vocabulary game where:
The program has a small dictionary (that you create) of words and their definitions
The program randomly selects a word from the dictionary
Shows the definition to the user
The user has 3 attempts to guess the word that matches the definition
After each guess, tell the user if they're correct or to try again
If they don't guess it in 3 tries, reveal the word
Requirements:
Create a dictionary with at least 5 word-definition pairs
Use the random module to select a random word
Keep track of the number of guesses
Make the game case-insensitive (so "APPLE" and "apple" are treated the same)
"""

import random

dictionary = {
    "python": "A programming language named after a snake",
    "juice": "Sweet liquid from a fruit, or the worlds most perfect black cat",
    "olive": "Small fruit that goes well in a martini, or the worlds most perfect tabby cat"
}

word, definition =  random.choice(list(dictionary.items()))
print(definition)

attempt = 1
while attempt <= 3:
    guess = input(f"Guess {attempt}: ")
    if guess.lower() == word:
        print("Nice")
        break

    if attempt == 3:
        print(f"Nope, the word was {word}, obviously")
    else:
        print(f"Nope, try again")
    attempt += 1
