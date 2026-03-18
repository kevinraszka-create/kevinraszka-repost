import secrets # Bezpečné generování náhodných hodnot (vhodné pro hesla)
import string  # Obsahuje předdefinované sady znaků (písmena, čísla, symboly)

historie = []
def prompt_yes_no(prompt: str, default: bool = True) -> bool: # default=True znamená, že pokud uživatel nezadá žádnou odpověď, bude považována za "ano"
    """Prompt the user for a yes/no answer."""
    while True: # Opakuj, dokud nedostaneme platnou odpověď
        odpoved = input(f"{prompt} (ano/ne) [{'ano' if default else 'ne'}]: ").strip().lower() 
        if not odpoved:
            return default
        if odpoved in ["ano", "a", "yes", "y"]:
            return True
        if odpoved in ["ne", "n", "no"]:
            return False
        print("Neplatná odpověď, zkus to znovu.") # Pokud uživatel zadá něco jiného než "ano" nebo "ne", zobrazí se tato zpráva a program se zeptá znovu.
def prompt_int(prompt: str, min_value: int = None, max_value: int = None, default: int = None) -> int: # default=None znamená, že není žádná výchozí hodnota
    """Prompt the user for an integer within a specified range."""

    while True:
        odpoved = input(f"{prompt} [{default}]: ").strip()
        if not odpoved and default is not None:
            return default
        try: # Pokusíme se převést odpověď na celé číslo
            value = int(odpoved)
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value): 
                print(f"Hodnota musí být mezi {min_value} a {max_value}.")
                continue
            return value
        except ValueError:
            print("Neplatná hodnota, zkus to znovu.")

def generate_password( # Funkce pro generování hesla
    length: int = 12,
    mala_pismena: bool = True,
    velka_pismena: bool = True,
    cisla: bool = True,
    specialni_znaky: bool = True,
) -> str: # Vrací vygenerované heslo jako řetězec
    """Generate a password with the requested character sets."""
    characters = "" # Začínáme s prázdným řetězcem, do kterého budeme přidávat znaky podle výběru uživatele
    if mala_pismena:
        characters += string.ascii_lowercase
    if velka_pismena:
        characters += string.ascii_uppercase
    if cisla:
        characters += string.digits
    if specialni_znaky:
        characters += string.punctuation

    if not characters: # Pokud uživatel nevybral žádnou sadu znaků, nemůžeme vygenerovat heslo, takže vyhodíme chybu
        raise ValueError("Musíš vybrat alespoň jednu sadu znaků.")

    return "".join(secrets.choice(characters) for _ in range(length)) # Vygenerujeme heslo tím, že náhodně vybíráme znaky z vytvořeného řetězce "characters" a spojíme je do jednoho řetězce pomocí "".join()


def main() -> None:
    print("=== Generátor hesel ===")

    while True: # Hlavní smyčka programu, která umožňuje uživateli generovat více hesel, dokud se nerozhodne ukončit program
        mala = prompt_yes_no("Chceš malá písmena?")
        velka = prompt_yes_no("Chceš velká písmena?")
        cisla = prompt_yes_no("Chceš čísla?")
        znaky = prompt_yes_no("Chceš speciální znaky?")
        delka = prompt_int("Zadej délku hesla", min_value=4, max_value=256, default=16)

        heslo = generate_password( # Vygenerujeme heslo pomocí zadaných parametrů
            length=delka,
            mala_pismena=mala,
            velka_pismena=velka,
            cisla=cisla,
            specialni_znaky=znaky,
        )
        print(f"Vygenerované heslo: {heslo}") # Zobrazíme vygenerované heslo uživateli
        historie.append(heslo)
        if not prompt_yes_no("Chceš vygenerovat další heslo?", default=False):
            break

if __name__ == "__main__": # Pokud je tento skript spuštěn přímo (ne importován jako modul), zavolá se funkce main()
    main()
    

