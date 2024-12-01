import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename = 'journal')

play_again_button = ttk.Button(window, text = 'Play Again')

def play_again_show():
    play_again_button.grid(column=0, row=3, padx=5, pady=5)
def play_again_hide():
    play_again_button.grid_forget()

def gui(word, attempts, take_a_guess):
    global play_again_button
    window.title('Hangman')
    window.geometry('800x200')
    window.iconbitmap('icons8_hangman_32_YBQ_icon.ico')
    window.resizable(False, False)

    label1_var = tk.StringVar(master=window)
    label1_var.set("Guess the word: " + "_ " * len(word))
    label1 = ttk.Label(window, textvariable=label1_var)
    label1.grid(column=0, row=0, padx=5, pady=5)

    attempt_var = tk.StringVar(master = window)
    attempt_var.set("You have " + str(attempts) + " guesses left.")
    label2 = ttk.Label(window, textvariable = attempt_var)
    label2.grid(column=1, row=0, padx=5, pady=5)

    input_frame = ttk.Frame(window)
    input_frame.grid(column=0, row=1, padx=5, pady=5, columnspan=2)


    button_a = ttk.Button(input_frame, text = 'A', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'a'))
    button_a.grid(column=0, row=0, padx=5, pady=5)

    button_b = ttk.Button(input_frame, text = 'B', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'b'))
    button_b.grid(column=1, row=0, padx=5, pady=5)

    button_c = ttk.Button(input_frame, text = 'C', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'c'))
    button_c.grid(column=2, row=0, padx=5, pady=5)

    button_d = ttk.Button(input_frame, text = 'D', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'd'))
    button_d.grid(column=3, row=0, padx=5, pady=5)

    button_e = ttk.Button(input_frame, text = 'E', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'e'))
    button_e.grid(column=4, row=0, padx=5, pady=5)

    button_f = ttk.Button(input_frame, text = 'F', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'f'))
    button_f.grid(column=5, row=0, padx=5, pady=5)

    button_g = ttk.Button(input_frame, text = 'G', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'g'))
    button_g.grid(column=6, row=0, padx=5, pady=5)

    button_h = ttk.Button(input_frame, text = 'H', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'h'))
    button_h.grid(column=7, row=0, padx=5, pady=5)

    button_i = ttk.Button(input_frame, text = 'I', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'i'))
    button_i.grid(column=8, row=0, padx=5, pady=5)

    button_j = ttk.Button(input_frame, text = 'J', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'j'))
    button_j.grid(column=9, row=0, padx=5, pady=5)

    button_k = ttk.Button(input_frame, text = 'K', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'k'))
    button_k.grid(column=10, row=0, padx=5, pady=5)

    button_l = ttk.Button(input_frame, text = 'L', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'l'))
    button_l.grid(column=11, row=0, padx=5, pady=5)

    button_m = ttk.Button(input_frame, text = 'M', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'm'))
    button_m.grid(column=12, row=0, padx=5, pady=5)

    button_n = ttk.Button(input_frame, text = 'N', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'n'))
    button_n.grid(column=0, row=1, padx=5, pady=5)

    button_o = ttk.Button(input_frame, text = 'O', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'o'))
    button_o.grid(column=1, row=1, padx=5, pady=5)

    button_p = ttk.Button(input_frame, text = 'P', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'p'))
    button_p.grid(column=2, row=1, padx=5, pady=5)

    button_q = ttk.Button(input_frame, text = 'Q', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'q'))
    button_q.grid(column=3, row=1, padx=5, pady=5)

    button_r = ttk.Button(input_frame, text = 'R', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'r'))
    button_r.grid(column=4, row=1, padx=5, pady=5)

    button_s = ttk.Button(input_frame, text = 'S', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 's'))
    button_s.grid(column=5, row=1, padx=5, pady=5)

    button_t = ttk.Button(input_frame, text = 'T', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 't'))
    button_t.grid(column=6, row=1, padx=5, pady=5)

    button_u = ttk.Button(input_frame, text = 'U', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'u'))
    button_u.grid(column=7, row=1, padx=5, pady=5)

    button_v = ttk.Button(input_frame, text = 'V', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'v'))
    button_v.grid(column=8, row=1, padx=5, pady=5)

    button_w = ttk.Button(input_frame, text = 'W', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'w'))
    button_w.grid(column=9, row=1, padx=5, pady=5)

    button_x = ttk.Button(input_frame, text = 'X', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'x'))
    button_x.grid(column=10, row=1, padx=5, pady=5)

    button_y = ttk.Button(input_frame, text = 'Y', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'y'))
    button_y.grid(column=11, row=1, padx=5, pady=5)

    button_z = ttk.Button(input_frame, text = 'Z', command= lambda: take_a_guess(attempt_var, results_var, label1_var, 'z'))
    button_z.grid(column=12, row=1, padx=5, pady=5)

    results_var = tk.StringVar(master = window)
    results_label = ttk.Label(window, textvariable = results_var)
    results_label.grid(column=0, row=2, padx=5, pady=5)

    play_again_button = ttk.Button(window, text='Play again?',
                                   command=lambda: take_a_guess(attempt_var, results_var, label1_var, 'yes'))

    window.mainloop()