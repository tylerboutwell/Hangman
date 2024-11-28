import random
import tkinter as tk
from logging import exception

import ttkbootstrap as ttk

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

def gui():
    window = ttk.Window(themename = 'journal')
    window.title('Hangman')
    window.geometry('500x500')

    label1_var = tk.StringVar(master=window)
    label1_var.set("Guess the word: " + "_ " * len(word))
    label1 = ttk.Label(window, textvariable=label1_var)
    label1.grid(column=0, row=0, padx=5, pady=5)

    attempt_var = tk.StringVar(master = window)
    attempt_var.set("You have " + str(attempts) + " guesses left.")
    label2 = ttk.Label(window, textvariable = attempt_var)
    label2.grid(column=0, row=1, padx=5, pady=5)

    guess_user = tk.StringVar(master = window)
    entry1 = ttk.Entry(window, textvariable = guess_user)
    entry1.grid(column=1, row=1, padx=5, pady=5)

    button1 = ttk.Button(window, text = 'ENTER', command =  lambda: take_a_guess(attempt_var, results_var, label1_var, entry1))
    button1.grid(column=2, row=1, padx=5, pady=5)

    results_var = tk.StringVar(master = window)
    results_label = ttk.Label(window, textvariable = results_var)
    results_label.grid(column=0, row=2, padx=5, pady=5)

    window.mainloop()

gui()