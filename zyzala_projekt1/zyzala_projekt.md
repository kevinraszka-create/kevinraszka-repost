# Snake Game

## Popis a cíl projektu
Projekt je jednoduchá arkádová hra Snake vytvořená v programovacím jazyce Python pomocí knihovny Pygame. 
Hráč ovládá hada, který se pohybuje po herním okně a sbírá potravu. Po snědení potravy se objeví nová 
na náhodném místě.

Cílem projektu je procvičit práci s grafickou knihovnou Pygame, práci s herní smyčkou, zpracování 
vstupu z klávesnice a detekci kolizí mezi objekty. Aplikace je určena především pro výukové účely 
a pro hráče, kteří si chtějí zahrát jednoduchou klasickou hru.

## Funkcionalita programu
Program se skládá z několika hlavních částí:

- vytvoření herního okna pomocí knihovny Pygame
- vykreslení hada jako zeleného čtverce
- generování potravy jako červeného čtverce
- ovládání hada pomocí kláves W, A, S, D
- detekce kolize mezi hadem a potravou
- náhodné generování nové potravy po snědení
- herní smyčka, která neustále aktualizuje obrazovku a pohyb hada

## Technická část

### Použité knihovny
Projekt využívá následující knihovny:

- **pygame** – slouží k vytvoření grafického okna, vykreslování objektů, zpracování vstupu z klávesnice a řízení herní smyčky
- **random** – používá se pro generování náhodné pozice potravy

### Datové struktury
Program využívá základní datové struktury Pythonu:

- **list (seznam)** – ukládá souřadnice hada a potravy

Příklad:
snake_pos = [300, 200]

food_pos = [random.randint(0, width - food_size), random.randint(0, height - food_size)]

### Algoritmy
Program využívá jednoduché algoritmy:

- **pohyb objektu** – změna pozice hada podle stisknuté klávesy
- **detekce kolize** – kontrola, zda se had dotýká potravy pomocí funkce `colliderect()`
- **generování náhodné pozice** – vytvoření nové pozice potravy pomocí `random.randint()`

### Herní smyčka
Hlavní část programu je nekonečná smyčka `while running`, která:

1. zpracovává vstupy z klávesnice
2. aktualizuje pozici hada
3. kontroluje kolize
4. překresluje herní obrazovku
5. řídí rychlost hry pomocí `clock.tick()`