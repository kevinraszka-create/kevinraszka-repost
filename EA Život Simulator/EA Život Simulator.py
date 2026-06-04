import tkinter as tk
from tkinter import messagebox

koupeno_mluveni = False
koupeno_chodit = False


def koupit_mluveni():
    global koupeno_mluveni

    okno = tk.Tk()
    okno.title("EA Payment Gateway")
    okno.geometry("350x200")

    tk.Label(
        okno,
        text="Speech Pack DLC",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tk.Label(
        okno,
        text="Odemkne funkci mluvení\nCena: 2 €"
    ).pack()

    def zaplatit():
        global koupeno_mluveni
        koupeno_mluveni = True
        messagebox.showinfo(
            "Platba úspěšná",
            "Speech Pack DLC byl zakoupen!"
        )
        okno.destroy()

    tk.Button(
        okno,
        text="Koupit za 2 €",
        command=zaplatit
    ).pack(pady=20)

    okno.mainloop()


def koupit_chodit():
    global koupeno_chodit

    okno = tk.Tk()
    okno.title("EA Payment Gateway")
    okno.geometry("350x200")

    tk.Label(
        okno,
        text="Walking Pack DLC",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tk.Label(
        okno,
        text="Odemkne možnost chodit\nCena: 1 €"
    ).pack()

    def zaplatit():
        global koupeno_chodit
        koupeno_chodit = True
        messagebox.showinfo(
            "Platba úspěšná",
            "Walking Pack DLC byl zakoupen!"
        )
        okno.destroy()

    tk.Button(
        okno,
        text="Koupit za 1 €",
        command=zaplatit
    ).pack(pady=20)

    okno.mainloop()


def promluvit():
    if not koupeno_mluveni:
        print("Mluvení není odemčeno!")
        koupit_mluveni()
    else:
        print("Ahoj světe!")


def chodit():
    if not koupeno_chodit:
        print("Chodit není odemčeno!")
        koupit_chodit()
    else:
        print("Kráčíš po světě!")


def plakat():
    print("BÉÉÉÉÉÉÉ!")
    print("Cítíš se lépe po dobrém pláči.")


print("=== EA LIFE SIMULATOR ===")
print("Narodil ses!")
print("Narození je zdarma.")

while True:
    print("\n1. Promluvit")
    print("2. Chodit")
    print("3. Plakat")
    print("4. Konec")

    volba = input("> ")

    if volba == "1":
        promluvit()

    elif volba == "2":
        chodit()

    elif volba == "3":
        plakat()

    elif volba == "4":
        print("Hra ukončena. Díky za hraní!")
        break

    else:
        print("Neplatná volba. Zkus to znovu.")