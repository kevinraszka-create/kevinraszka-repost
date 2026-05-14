Dokumentace projektu Sudoku Generator

Název projektu je Sudoku Generator. Projekt je vytvořen v programovacím jazyce Python a slouží ke generování Sudoku tabulek různých obtížností. Cílem projektu je vytvořit jednoduchou aplikaci s grafickým rozhraním, která dokáže automaticky generovat nové Sudoku.

Program po spuštění zobrazí grafické okno, ve kterém si uživatel může vybrat obtížnost Sudoku. Na výběr jsou možnosti Easy, Medium a Hard. Po stisknutí tlačítka Generate Puzzle program vytvoří nové Sudoku a zobrazí ho v textovém poli.

Program nejprve vytvoří kompletně vyřešenou Sudoku tabulku. Poté odstraní určitý počet čísel podle zvolené obtížnosti. Lehčí obtížnost odstraní méně čísel a těžší obtížnost odstraní více čísel.

Projekt využívá knihovny random, tkinter a ttk. Knihovna random slouží pro náhodné míchání čísel a výběr políček, která budou odstraněna. Knihovna tkinter slouží pro vytvoření grafického uživatelského rozhraní. Modul ttk poskytuje modernější vzhled jednotlivých prvků GUI.

Hlavní algoritmus programu využívá backtracking. Tento algoritmus postupně zkouší vkládat čísla do prázdných políček Sudoku. Pokud číslo splňuje pravidla Sudoku, pokračuje dál. Pokud nastane konflikt, algoritmus se vrátí zpět a zkusí jiné číslo. Díky tomu je možné vytvořit správně vyřešenou Sudoku tabulku.

Sudoku tabulka je uložena jako dvourozměrný seznam o velikosti 9x9. Každé políčko obsahuje číslo od 1 do 9 nebo hodnotu 0, která představuje prázdné pole.

Program obsahuje několik funkcí. Funkce is_valid kontroluje, zda lze číslo vložit do určité pozice. Funkce solve řeší Sudoku pomocí backtracking algoritmu. Funkce generate_sudoku vytvoří kompletní Sudoku tabulku. Funkce remove_cells odstraní čísla podle obtížnosti. Funkce create_puzzle vytvoří výsledné Sudoku pro hráče. Funkce board_to_text převádí tabulku do textové podoby a funkce main spouští celé grafické rozhraní.

Projekt je jednoduchý, přehledný a vhodný pro procvičení práce s algoritmy, rekurzí a grafickým rozhraním v Pythonu. Do budoucna by bylo možné přidat například automatické řešení Sudoku, ukládání her nebo možnost ručního vyplňování tabulky.