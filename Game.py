import random
import tkinter as tk
from idlelib.configdialog import font_sample_text
from lib2to3.refactor import RefactoringTool
from tkinter import ttk
import ttkbootstrap as ttk


words = []

files = ["animals.txt", "technology.txt", "food.txt"]
file = open(random.choice(files))
for i in file:
    words.append(i.replace('\n', ''))

word = random.choice(words)

word_array = []
for i in word:
    word_array.append(i)

guesses = []
attempts = 7
results = ""
winner = True
def take_a_guess():
    global attempts, results, winner, guesses, word_array, guess_user, results_var
    attempts -= 1
    attempt_var.set("You have " + str(attempts) + " guesses left.")
    for i in word_array:
        if i in guesses:
            results += i
        else:
            results += "_"
            winner = False
    if winner:
        results = "You won!!"
    print("Enter a letter:")
    user_letter = guess_user.get()
    if len(user_letter) != 1:
        results = "You must enter 1 letter!"
        attempts += 1
    elif user_letter in guesses:
        results = "You already guessed " + user_letter
        attempts += 1
    else:
        if user_letter in word_array:
            attempts += 1
        guesses.append(user_letter)
    if not winner and attempts == 0:
        results = "You lost. The word was", word + "."
    results_var.set(results)

    
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

button1 = ttk.Button(window, text = 'ENTER', command =  take_a_guess)
button1.grid(column=2, row=1, padx=5, pady=5)

results_var = tk.StringVar(master = window)
results_label = ttk.Label(window, textvariable = results_var)
results_label.grid(column=0, row=2, padx=5, pady=5)

window.mainloop()