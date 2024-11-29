import random
from Gui import *

# select a random txt file of words
files = ["animals.txt", "technology.txt", "food.txt"]
file = open(random.choice(files))

#add words from file to array and select a random word
words = []
for i in file:
    words.append(i.replace('\n', ''))
word = random.choice(words)

#add each letter from word to an array
word_letters = []
for i in word:
    word_letters.append(i)

guesses = []
attempts = 7
def take_a_guess(t_attempts, t_results, t_label1, t_entry):
    global attempts
    user_letter = t_entry.get()
    winner = True
    word_status = str()
    attempts -= 1

    if len(user_letter) != 1:
        results = "You must enter 1 letter!"
        attempts += 1
    elif user_letter in guesses:
        results = "You already guessed " + user_letter
        attempts += 1
    else:
        if user_letter in word_letters:
            attempts += 1
            results = "Congrats! You guessed " + user_letter + "!"
        else:
            results = "Wrong letter!"
        guesses.append(user_letter)

    for i in word_letters:
        if i in guesses:
            word_status += i
        else:
            word_status += "_ "
            winner = False

    if winner:
        results = "You won!!"
        t_attempts.set("Play again?")
    elif not winner and attempts == 0:
        results = "You lost. The word was " + word + "."
        t_attempts.set("Play again?")
    else:
        t_attempts.set("You have " + str(attempts) + " guesses left.")
    t_results.set(results)
    t_label1.set("Guess the word: " + word_status)

gui(word, attempts, take_a_guess)