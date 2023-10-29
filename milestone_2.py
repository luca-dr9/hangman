import random

word_list = ["apple","pear","orange","banana","mango"]
word = random.choice(word_list)

guess = input("Make a guess: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")