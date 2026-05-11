Projekt: Simulace rulety v Pythonu
1. Popis a cíl projektu

Tento projekt představuje jednoduchou objektově orientovanou implementaci kasinové hry ruleta v jazyce Python. Cílem je vytvořit přehledný a rozšiřitelný model hry, který umožňuje simulovat základní principy sázení a vyhodnocování výsledků.

Projekt je primárně určen:

pro výukové účely (OOP, práce s třídami, validace vstupů),
pro demonstraci pravděpodobnostních systémů,
jako základ pro další rozšíření (např. složitější sázky, více hráčů, GUI).
2. Funkcionalita programu

Program implementuje základní herní smyčku rulety, ve které hráč:

Zadá výši sázky
Zvolí typ sázky:
konkrétní číslo (tzv. straight bet)
barvu (red, black)
sudost (even) nebo lichost (odd)
Proběhne otočení rulety (spin)
Vyhodnotí se výhra nebo prohra
Aktualizuje se hráčův zůstatek (bank)
Hlavní funkce:
 Generování náhodného čísla (spin rulety)
 Správa bankrollu (vklad, výplata)
 Vyhodnocení sázek
 Uchovávání historie hodů a barev
 Interaktivní textové rozhraní
3. Struktura programu
Třída Roulette

Hlavní logika hry je zapouzdřena v třídě Roulette.

Atributy:
bet_type – typ sázky (výchozí: 'straight')
wheel – typ rulety (American nebo European)
bank – aktuální zůstatek hráče
rolls – historie padlých čísel
colors – historie barev
Statické množiny:
red – červená čísla
black – černá čísla
odd – lichá čísla
even – sudá čísla
Metody:
spin()
Simuluje otočení rulety
Vrací náhodné číslo
Ukládá historii hodů
_color(roll)
Určuje barvu čísla (červená, černá, zelená)
place_bet(amount)
Validuje sázku
Odečítá částku z banku
resolve_bet(amount, choice, roll)
Vyhodnocuje výsledek sázky
Vypočítá výplatu:
 číslo: 36× sázka
 barva / sudost / lichost: 2× sázka
get_roll_display(roll)
Převádí číslo 37 na '00' (americká ruleta)
Hlavní smyčka (__main__)
Interaktivní vstup od uživatele
Opakuje hru, dokud má hráč peníze
Ošetřuje chyby (ValueError)
4. Technická část
Použité knihovny
random
generování náhodných čísel (randint)
simulace náhody v ruletě
Algoritmy a logika
Generování výsledku
Americká ruleta:
čísla 0–36 + 00 (reprezentováno jako 37)
Evropská ruleta:
čísla 0–36
Vyhodnocení sázek
Porovnání hodnot:
přímé (roll == choice)
množinové (roll in množina)
Barvy určovány pomocí množin (set)
Datové struktury
Množiny (set)
efektivní kontrola příslušnosti (O(1))
použity pro:
barvy
sudost/lichost
Seznamy (list)
ukládání historie hodů (rolls)
ukládání historie barev (colors)
Ošetření chyb
Neplatná sázka → ValueError
Nedostatek prostředků → ValueError
Neznámý typ sázky → ValueError
Možná rozšíření
další typy sázek (tucety, sloupce)
grafické rozhraní (Tkinter, PyQt)
více hráčů
statistiky a analýza výsledků
ukládání historie do souboru/databáze
5. Shrnutí

Projekt představuje jednoduchou, ale dobře strukturovanou simulaci rulety. Využívá principy objektově orientovaného programování, efektivní datové struktury a základní práci s náhodností. Díky své modularitě je vhodný pro další rozvoj a experimentování.