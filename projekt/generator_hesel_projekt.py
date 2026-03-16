import random
import string

historie = []

def generate_password(length=12, mala_pismena=True, velka_pismena=True, cisla=True, specialni_znaky=True):
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
        print("Chyba: Musíte vybrat alespoň jeden typ znaků!")
        return None


