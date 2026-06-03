import tkinter as tk
from tkinter import messagebox

koupeno_mluveni = False


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


def promluvit():
    if not koupeno_mluveni:
        print("Mluvení není odemčeno!")
        koupit_mluveni()
    else:
        print("Ahoj světe!")


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
        print("Walking DLC není zakoupeno.")

    elif volba == "3":
        print("BÉÉÉÉÉÉÉ!")

    elif volba == "4":
        break