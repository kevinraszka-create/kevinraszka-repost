Dokumentace – Geometry Dash: Cube Jumper
Název projektu

Geometry Dash – Cube Jumper

Popis a cíl projektu

Jedná se o 2D endless runner hru inspirovanou Geometry Dash, kde hráč ovládá kostku, která musí skákat přes překážky ve formě hrotů (spikes).
Cíl projektu: vytvořit jednoduchou, zábavnou hru, kde hráč získává body za překonání překážek a snaží se přežít co nejdéle.

Popis funkcionality programu
Hráč ovládá kostku, která může skákat stiskem klávesy SPACE.
Překážky (spikes) se generují náhodně a pohybují se z pravé strany obrazovky doleva.
Hráč získává bod za každou překážku, která zmizí z obrazovky.

Hra končí, pokud:
kostka narazí do překážky, nebo
kostka spadne pod obrazovku.

Po skončení hry je možné restartovat stiskem klávesy R.
Skóre a stav hry jsou vizuálně zobrazeny na obrazovce.
Technická část
Použité knihovny
pygame – pro grafiku, zpracování vstupu, časování a vykreslování hry.

random – pro náhodné generování překážek a jejich rozestupu.
Algoritmy a logika
Gravitace a skok – fyzikální simulace pohybu kostky.
Kolizní detekce (AABB) – Axis-Aligned Bounding Box pro kontrolu kolize hráče s překážkou.

Endless runner logika – nekonečné generování překážek s postupně náhodným intervalem.
Skórování – každý objekt, který zmizí z obrazovky, zvyšuje skóre o 1 bod.

Datové struktury
Třída Cube – reprezentuje hráče, obsahuje atributy pozice, velikosti, rychlosti a stav skoku.

Třída Obstacle – reprezentuje překážky, obsahuje atributy pozice, velikosti a rychlosti pohybu.

Seznam obstacles – dynamický seznam všech aktuálně aktivních překážek na obrazovce.

Volání externího API
Nepoužívá se žádné externí API, vše je řešeno lokálně v rámci Pythonu a knihovny pygame.
