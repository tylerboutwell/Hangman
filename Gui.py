import tkinter as tk
import ttkbootstrap as ttk

def gui(word, attempts, take_a_guess):
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