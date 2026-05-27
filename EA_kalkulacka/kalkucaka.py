
# Importuje knihovnu tkinter pro tvorbu grafického okna
import tkinter as tk  
# tkinter = základní GUI knihovna v Pythonu
# "as tk" znamená, že místo tkinter budeme psát jen tk

# Importuje messagebox pro vyskakovací okna
from tkinter import messagebox  
# messagebox slouží pro informační okna typu "Hotovo", "Chyba" atd.


# Vytvoření třídy kalkulačky
class CalculatorApp:
    # Konstruktor třídy
    def __init__(self, master):
        # Uloží hlavní okno aplikace
        self.master = master  
        # self = aktuální objekt
        # master = hlavní okno tkinteru

        # Nastaví název okna
        master.title("Paid Calculator")  
        # text v horní liště okna

        # Proměnná pro ukládání matematického výrazu
        self.expression = ""  
        # sem se ukládají čísla a operace které uživatel kliká


        # Vytvoření textového pole
        self.entry = tk.Entry(
            master,
            font=("Arial", 20),   # velikost a typ písma
            bd=5,                 # tloušťka rámečku
            relief='ridge',       # styl rámečku
            justify='right'       # text zarovnaný doprava
        )

        # Umístění textového pole do mřížky
        self.entry.grid(
            row=0,
            column=0,
            columnspan=4,  # zabere 4 sloupce
            padx=10,       # vnější mezera horizontálně
            pady=10,       # vnější mezera vertikálně
            sticky='nsew'  # roztáhne widget všemi směry
        )


        # Seznam tlačítek kalkulačky
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
        ]
        # Každá položka obsahuje:
        # ('text tlačítka', řádek, sloupec)


        # Smyčka pro vytvoření všech tlačítek
        for (text, r, c) in buttons:

            # Vytvoření tlačítka
            button = tk.Button(
                master,
                text=text,                 # text na tlačítku
                width=5,                  # šířka
                height=2,                 # výška
                font=("Arial", 18),       # font
                command=lambda t=text: self.on_button(t)
            )

            # lambda = anonymní funkce
            # po kliknutí zavolá on_button()

            # Umístění tlačítka
            button.grid(
                row=r,
                column=c,
                padx=5,
                pady=5,
                sticky='nsew'
            )


        # Tlačítko "="
        eq_button = tk.Button(
            master,
            text='=',
            width=5,
            height=2,
            font=("Arial", 18),
            command=self.ask_payment
        )
        # po kliknutí se otevře platební okno

        # Umístění "=" tlačítka
        eq_button.grid(
            row=5,
            column=0,
            columnspan=4,
            padx=5,
            pady=5,
            sticky='nsew'
        )


        # Nastavení pružnosti sloupců
        for i in range(4):
            master.columnconfigure(i, weight=1)
        # weight=1 znamená že se budou roztahovat

        # Nastavení pružnosti řádků
        for i in range(6):
            master.rowconfigure(i, weight=1)


    # Funkce po kliknutí na tlačítko
    def on_button(self, char):

        # Pokud je stisknuto C
        if char == 'C':

            # Vymaže výraz
            self.expression = ""

            # Vymaže obsah textového pole
            self.entry.delete(0, tk.END)

        else:
            # Přidá znak do výrazu
            self.expression += char

            # Vymaže aktuální obsah
            self.entry.delete(0, tk.END)

            # Vloží nový výraz
            self.entry.insert(0, self.expression)


    # Funkce která otevře platební okno
    def ask_payment(self):

        # Získá text z entry
        expr = self.entry.get().strip()

        # Pokud je výraz prázdný
        if not expr:
            return
            # ukončí funkci


        # Vytvoření nového okna
        pay_window = tk.Toplevel(self.master)
        # Toplevel = nové podokno

        # Název okna
        pay_window.title("Payment Required")

        # Velikost okna
        pay_window.geometry("360x260")


        # Popisky polí
        labels = [
            "Card Number",
            "Expiry Date",
            "CVV",
            "Name on Card"
        ]

        # Vytvoření StringVar proměnných
        self.card_vars = [tk.StringVar() for _ in labels]
        # StringVar = speciální tkinter proměnná


        # Funkce pro formátování čísla karty
        def format_card_number(*args):

            # Získá text
            raw = self.card_vars[0].get()

            # Nechá jen čísla
            digits = ''.join(ch for ch in raw if ch.isdigit())[:16]
            # [:16] = max 16 číslic

            # Rozdělí po 4 číslech
            formatted = '-'.join(
                digits[i:i+4]
                for i in range(0, len(digits), 4)
            )

            # Pokud je text jiný
            if raw != formatted:

                # nastaví nový formát
                self.card_vars[0].set(formatted)


        # Sleduje změny v poli čísla karty
        self.card_vars[0].trace_add(
            'write',
            format_card_number
        )
        # kdykoliv uživatel píše -> zavolá funkci


        # Smyčka pro vytvoření labelů a inputů
        for idx, label in enumerate(labels):

            # Textový popisek
            tk.Label(
                pay_window,
                text=label
            ).grid(
                row=idx,
                column=0,
                padx=10,
                pady=5,
                sticky='w'
            )

            # Textové pole
            tk.Entry(
                pay_window,
                textvariable=self.card_vars[idx],
                width=25
            ).grid(
                row=idx,
                column=1,
                padx=10,
                pady=5
            )


        # Funkce po kliknutí na Submit
        def submit_payment():

            # Spočítá výraz
            result = self.safe_eval(expr)

            # Zobrazí výsledek
            messagebox.showinfo(
                "Paid",
                f"Payment accepted. Result: {result}"
            )

            # Zavře platební okno
            pay_window.destroy()


        # Tlačítko submit
        tk.Button(
            pay_window,
            text="Submit",
            width=20,
            command=submit_payment
        ).grid(
            row=len(labels),
            column=0,
            columnspan=2,
            pady=15
        )


    # Funkce pro bezpečný výpočet
    def safe_eval(self, expr):

        try:
            # Vyhodnotí matematický výraz
            return str(eval(
                expr,
                {"__builtins__": None},
                {}
            ))

            # __builtins__ = None
            # zakáže přístup k nebezpečným funkcím

        except Exception:
            # Pokud vznikne chyba
            return "Error"



# Spustí program pouze pokud je soubor spuštěn přímo
if __name__ == "__main__":

    # Vytvoření hlavního okna
    root = tk.Tk()

    # Spuštění aplikace
    CalculatorApp(root)

    # Hlavní smyčka programu
    root.mainloop()
    # bez ní by se okno okamžitě zavřelo
