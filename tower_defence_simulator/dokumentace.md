Dokumentace projektu
Název projektu

Tower Defence Simulator (Python + Pygame)

Popis a cíl projektu

Projekt „Tower Defence Simulator“ je jednoduchá 2D hra vytvořená v programovacím jazyce Python za použití knihovny Pygame. Hráč se snaží ubránit herní pole před nepřáteli pomocí obranných věží.

Cílem projektu je:

naučit se pracovat s knihovnou Pygame
pochopit princip herní smyčky
procvičit objektově orientované programování
vytvořit jednoduchou interaktivní hru
Popis funkcionality programu
Stavění věží

Hráč může kliknutím myši umístit věž na herní plochu. Každá věž stojí určité množství peněz, které se po jejím postavení odečtou.

Výběr a vylepšování věží

Kliknutím na věž ji hráč vybere. Pomocí klávesy může následně věž vylepšit. Vylepšení zvyšuje její schopnosti (např. poškození nebo dosah), ale zároveň stojí peníze.

Spawn nepřátel

Nepřátelé se pravidelně objevují na levé straně obrazovky a pohybují se směrem doprava.

Útok věží

Věže automaticky vyhledávají nepřátele ve svém dosahu. Pokud je nepřítel v dosahu, věž na něj začne útočit pomocí projektilů.

Projektily

Projektily se pohybují směrem k nepříteli. Po zásahu způsobí poškození a následně zmizí.

Odstraňování nepřátel

Pokud nepřítel ztratí všechny životy, je odstraněn ze hry a hráč za něj získá peníze.

Uživatelské rozhraní

Na obrazovce se zobrazuje:

aktuální množství peněz
instrukce pro ovládání
informace o ceně upgradu vybrané věže
Technická část
Použité knihovny
pygame – slouží pro vykreslování grafiky, práci s oknem a zpracování vstupů
random – používá se pro generování náhodných pozic nepřátel
sys – umožňuje správné ukončení programu
Použité algoritmy
Výpočet vzdálenosti mezi objekty pro určení, zda je nepřítel v dosahu věže
Pohyb projektilu směrem k cíli pomocí směrového vektoru
Jednoduchá detekce kolizí mezi projektily a nepřáteli
Časování akcí (např. rychlost střelby nebo spawn nepřátel)
Datové struktury

Program využívá základní datové struktury:

seznamy pro ukládání věží, nepřátel a projektilů
objekty (instance tříd) pro reprezentaci jednotlivých prvků hry
Objektově orientované programování

Program je navržen pomocí tříd:

Tower – reprezentuje věž
Enemy – reprezentuje nepřítele
Projectile – reprezentuje střelu

Každá třída obsahuje:

atributy (např. pozice, rychlost, životy)
metody (např. pohyb, vykreslení, útok)
Externí API

Program nevyužívá žádné externí API.