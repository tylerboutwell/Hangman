import random
from Gui import *

files = ["animals.txt", "technology.txt", "food.txt"]
word = str()
attempts = int()
game_complete = bool
guesses = []
word_letters = []

def init_game():
    global word, attempts, guesses, word_letters, game_complete
    words = []
    guesses = []
    attempts = 7
    game_complete = False
    # select a random txt file of words
    file = open(random.choice(files))

    #add words from file to array and select a random word
    for i in file:
        words.append(i.replace('\n', ''))
    word = random.choice(words)

    #add each letter from word to an array
    word_letters = []
    for i in word:
        word_letters.append(i)

def take_a_guess(t_attempts, t_results, t_label1, t_entry):
    global attempts, game_complete
    user_entry = t_entry.get()
    winner = True
    word_status = str()
    attempts -= 1

    if game_complete:
        if user_entry == "yes":
            init_game()
            results = ''
        else:
            results = 'Enter yes to play again!'
    elif len(user_entry) != 1:
        results = "You must enter 1 letter!"
        attempts += 1
    elif user_entry in guesses:
        results = "You already guessed " + user_entry
        attempts += 1
    else:
        if user_entry in word_letters:
            attempts += 1
            results = "Congrats! You guessed " + user_entry + "!"
        else:
            results = "Wrong letter!"
        guesses.append(user_entry)

    for i in word_letters:
        if i in guesses:
            word_status += i
        else:
            word_status += "_ "
            winner = False

    if not game_complete:
        if winner:
            game_complete = True
            results = "You won!!"
            t_attempts.set("Play again?")
        elif not winner and attempts == 0:
            game_complete = True
            results = "You lost. The word was " + word + "."
            t_attempts.set("Play again?")
        else:
            t_attempts.set("You have " + str(attempts) + " guesses left.")
    t_results.set(results)
    t_label1.set("Guess the word: " + word_status)

init_game()
gui(word, attempts, take_a_guess)