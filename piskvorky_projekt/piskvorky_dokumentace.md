Dokumentace projektu
Název projektu

Piškvorky v Pythonu (Pygame verze)

Popis a cíl projektu

Cílem projektu bylo vytvořit jednoduchou počítačovou hru Piškvorky (Gomoku) pro dva hráče s grafickým rozhraním. Program je napsán v jazyce Python a využívá knihovnu Pygame pro vykreslování herního pole a zpracování vstupů od uživatele.

Hra umožňuje dvěma hráčům střídat se v pokládání kamenů na hrací plochu. Cílem je vytvořit souvislou řadu pěti kamenů (vodorovně, svisle nebo diagonálně).

Popis funkcionality programu

Program obsahuje následující funkce:

Vykreslení herního pole o velikosti 15 × 15 polí
Ovládání pomocí myši (kliknutí do pole)
Střídání dvou hráčů:
hráč 1 (červený kámen)
hráč 2 (modrý kámen)
Kontrola platnosti tahu (nelze hrát na obsazené pole)
Automatická kontrola výhry po každém tahu
Vypsání vítěze do konzole
Automatické restartování hry po výhře
Technická část
Použité knihovny
pygame – knihovna pro tvorbu her, zajišťuje:
vykreslování grafiky
práci s oknem aplikace
zpracování vstupů (myš, události)
Algoritmy
Kontrola výhry

Program používá algoritmus, který prochází celé herní pole a kontroluje, zda existuje 5 stejných symbolů za sebou.

Kontrolují se 4 směry:

horizontální (→)
vertikální (↓)
diagonální (↘)
diagonální (↙)

Pro kontrolu se používá funkce all(), která ověřuje, že všech 5 polí obsahuje stejného hráče.

Datové struktury

Herní plocha je reprezentována jako dvourozměrné pole (seznam seznamů):

0 = prázdné pole
1 = hráč 1
2 = hráč 2

Tato struktura umožňuje snadný přístup k jednotlivým políčkům pomocí souřadnic [y][x].

Herní logika
Hráč provede tah kliknutím myši
Souřadnice kliknutí se převedou na pozici v mřížce
Pokud je pole volné, uloží se tah hráče
Po každém tahu se spustí kontrola výhry
Pokud některý hráč vyhraje:
vypíše se výsledek
herní pole se resetuje
Grafické zpracování
Každé pole má velikost 40 × 40 pixelů
Herní kameny jsou vykresleny jako kruhy:
červený pro hráče 1
modrý pro hráče 2
Mřížka je vykreslena pomocí čar
Okno aplikace se průběžně obnovuje (60 FPS)
Závěr

Projekt splňuje zadání – implementuje funkční hru Piškvorky s grafickým rozhraním. Program demonstruje práci s knihovnou Pygame, základní herní logiku a použití dvourozměrných datových struktur.

Kdybys chtěl, můžu ti to ještě upravit třeba víc „školně“ (kratší verze / bodově), nebo přidat titulní stranu