import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Paid Calculator")
        self.expression = ""

        self.entry = tk.Entry(master, font=("Arial", 20), bd=5, relief='ridge', justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
        ]
        for (text, r, c) in buttons:
            button = tk.Button(master, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: self.on_button(t))
            button.grid(row=r, column=c, padx=5, pady=5, sticky='nsew')

        eq_button = tk.Button(master, text='=', width=5, height=2, font=("Arial", 18), command=self.ask_payment)
        eq_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

        for i in range(4):
            master.columnconfigure(i, weight=1)
        for i in range(6):
            master.rowconfigure(i, weight=1)

    def on_button(self, char):
        if char == 'C':
            self.expression = ""
            self.entry.delete(0, tk.END)
        else:
            self.expression += char
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)

    def ask_payment(self):
        expr = self.entry.get().strip()
        if not expr:
            return