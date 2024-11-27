import random
import tkinter as tk
from idlelib.configdialog import font_sample_text
from tkinter import ttk
import ttkbootstrap as ttk

def start():
    print("Welcome to Hangman!")
    print("Choose a theme!")
    print("Technology, Animals, Food")
    theme = input().lower()

    words = []
    if theme == "animals":
        file = open("animals.txt", "r")
    elif theme == "technology":
        file = open("technology.txt", "r")
    elif theme == "food":
        file = open("food.txt", "r")
    else:
        print("Invalid theme! Theme is technology!")
        file = open("technology.txt", "r")
    for i in file:
        words.append(i.replace('\n', ''))

    word = random.choice(words)

    word_array = []
    for i in word:
        word_array.append(i)

    guesses = []
    attempts = 7

    while attempts > 0:
        attempts -= 1
        winner = True
        print("Guess the word: ")
        for i in word_array:
            if i in guesses:
                print(i, end = "")
            else:
                print("_", end = "")
                winner = False
        print()
        if winner:
            print("You won!!")
            break
        print("Enter a letter:")
        user_letter = input().lower()
        if len(user_letter) != 1:
            print("You must enter 1 letter!")
            attempts += 1
        elif user_letter in guesses:
            print("You already guessed " + user_letter)
            attempts += 1
        else:
            if user_letter in word_array:
                attempts += 1
            guesses.append(user_letter)
    if not winner:
        print("You lost. The word was", word + ".")

    print("Play again? y/n")
    play_again = input()
    if play_again == "y":
        start()
    else:
        window.destroy()
    
window = ttk.Window(themename = 'journal')
window.title('Hangman')
window.geometry('500x500')

label1 = ttk.Label(window, text="Guess the word: ")
label1.grid(column=0, row=0, padx=5, pady=5)

label2 = ttk.Label(window, text="You have " + " guesses left.")
label2.grid(column=0, row=1, padx=5, pady=5)

entry1 = ttk.Entry(window)
entry1.grid(column=1, row=1, padx=5, pady=5)

button1 = ttk.Button(window, text = 'ENTER')
button1.grid(column=2, row=1, padx=5, pady=5)

window.mainloop()