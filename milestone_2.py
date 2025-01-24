word_list = ["mango", "banana", "apple", "pineapple", "plum"]
print(word_list)

import random

word = random.choice(word_list)
print(word)

guess = input("Guess a letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
