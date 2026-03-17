import secrets
import string

historie = []
def prompt_yes_no(prompt: str, default: bool = True) -> bool:
    """Prompt the user for a yes/no answer."""
    while True:
        odpoved = input(f"{prompt} (ano/ne) [{'ano' if default else 'ne'}]: ").strip().lower()
        if not odpoved:
            return default
        if odpoved in ["ano", "a", "yes", "y"]:
            return True
        if odpoved in ["ne", "n", "no"]:
            return False
        print("Neplatná odpověď, zkus to znovu.")
def prompt_int(prompt: str, min_value: int = None, max_value: int = None, default: int = None) -> int:

 
def generate_password(
    length: int = 12,
    mala_pismena: bool = True,
    velka_pismena: bool = True,
    cisla: bool = True,
    specialni_znaky: bool = True,
) -> str:
    """Generate a password with the requested character sets."""
    characters = ""
    if mala_pismena:
        characters += string.ascii_lowercase
    if velka_pismena:
        characters += string.ascii_uppercase
    if cisla:
        characters += string.digits
    if specialni_znaky:
        characters += string.punctuation

    if not characters:
        raise ValueError("Musíš vybrat alespoň jednu sadu znaků.")

    return "".join(secrets.choice(characters) for _ in range(length))


def main() -> None:
    print("=== Generátor hesel ===")

    while True:
        mala = prompt_yes_no("Chceš malá písmena?")
        velka = prompt_yes_no("Chceš velká písmena?")
        cisla = prompt_yes_no("Chceš čísla?")
        znaky = prompt_yes_no("Chceš speciální znaky?")
        delka = prompt_int("Zadej délku hesla", min_value=4, max_value=256, default=16)

        heslo = generate_password(
            length=delka,
            mala_pismena=mala,
            velka_pismena=velka,
            cisla=cisla,
            specialni_znaky=znaky,
        )
        print(f"Vygenerované heslo: {heslo}")
        historie.append(heslo)
    

