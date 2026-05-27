Dokumentace projektu
Název projektu

Paid Calculator – grafická kalkulačka s platebním oknem

Popis a cíl projektu

Projekt „Paid Calculator“ je desktopová aplikace vytvořená v programovacím jazyce Python pomocí knihovny Tkinter. Jedná se o jednoduchou grafickou kalkulačku, která umožňuje uživateli zadávat matematické výrazy a následně je vypočítat.

Zajímavostí projektu je simulace platebního systému. Před zobrazením výsledku výpočtu musí uživatel vyplnit platební formulář obsahující číslo karty, datum expirace, CVV a jméno držitele karty.

Cílem projektu bylo vytvořit funkční grafickou aplikaci, naučit se pracovat s grafickým rozhraním v Pythonu, implementovat práci s tlačítky a formuláři a zároveň si vyzkoušet bezpečnější vyhodnocování matematických výrazů.

Popis funkcionality programu

Program funguje jako klasická kalkulačka s grafickým rozhraním. Uživatel může pomocí tlačítek zadávat čísla a matematické operace, například sčítání, odčítání, násobení a dělení. Zadaný výraz se průběžně zobrazuje v textovém poli.

Součástí aplikace je také tlačítko pro vymazání celého výrazu.

Po stisknutí tlačítka pro výpočet se neprovede okamžitě matematická operace, ale otevře se nové okno simulující platební formulář. Uživatel zde vyplní číslo platební karty, datum expirace, CVV kód a jméno držitele karty.

Program automaticky upravuje formát čísla karty tak, aby bylo rozdělené po čtyřech číslicích. Po potvrzení formuláře program vypočítá matematický výraz a zobrazí výsledek v informačním okně.

Aplikace zároveň obsahuje jednoduché ošetření chyb. Pokud uživatel zadá neplatný matematický výraz, program nespadne a zobrazí chybovou hlášku.

Technická část

Projekt byl vytvořen v programovacím jazyce Python 3.

Pro tvorbu grafického uživatelského rozhraní byla použita knihovna Tkinter, která je součástí základní instalace Pythonu. Pomocí této knihovny byla vytvořena hlavní okna aplikace, tlačítka, textová pole i dialogová okna.

Program využívá objektově orientované programování prostřednictvím třídy CalculatorApp, která obsahuje všechny hlavní funkce aplikace.

Pro ukládání matematického výrazu je použit textový řetězec, do kterého se postupně přidávají jednotlivé znaky podle stisknutých tlačítek.

Při formátování čísla platební karty program odstraňuje nečíselné znaky, omezuje délku vstupu a automaticky rozděluje číslo do skupin po čtyřech číslicích.

K výpočtu matematického výrazu je použita funkce eval(). Z bezpečnostních důvodů jsou zakázány vestavěné funkce Pythonu, aby nebylo možné spouštět nebezpečný kód.

Rozložení prvků v okně je vytvořeno pomocí mřížkového systému grid, který umožňuje automatické přizpůsobení velikosti jednotlivých prvků při změně velikosti okna.

Projekt nevyužívá žádné externí API ani databázi.