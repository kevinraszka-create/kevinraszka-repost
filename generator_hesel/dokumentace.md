Název projektu
Generátor bezpečných hesel (CLI aplikace)

Popis a cíl projektu
Cílem projektu je vytvořit jednoduchou konzolovou aplikaci pro generování bezpečných hesel na základě uživatelských preferencí.
Aplikace je určena pro běžné uživatele i vývojáře, kteří potřebují rychle vytvořit silná a náhodná hesla.


Funkcionalita programu
Program umožňuje uživateli:

zvolit typy znaků (malá/velká písmena, čísla, speciální znaky)

nastavit délku hesla v definovaném rozsahu

generovat kryptograficky bezpečné heslo

opakovaně vytvářet nová hesla v jednom běhu programu

ukládat historii vygenerovaných hesel během běhu aplikace

Technická část


Použité knihovny:
secrets – kryptograficky bezpečné generování náhodných znaků

string – předdefinované množiny znaků

Algoritmus generování:

Dynamické sestavení množiny znaků dle vstupu uživatele

Náhodný výběr znaků pomocí secrets.choice()

Sestavení hesla pomocí iterace o požadované délce


Validace vstupů:
Ověření typu odpovědi (ano/ne)

Kontrola číselného rozsahu pro délku hesla

Ošetření neplatných vstupů pomocí opakovaného dotazu

Datové struktury:

Seznam (list) pro ukládání historie hesel

Architektura:

Modulární struktura (oddělené funkce pro vstup, validaci a generování)

Hlavní řídicí smyčka v main()