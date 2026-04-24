Dokumentace projektu
Název projektu
Klikací hra (Clicker Game)

Popis a cíl projektu
Jednoduchá klikací hra vytvořená v Pygame, kde hráči klikáním na červené tlačítko zvyšují skóre. Cílem je dosáhnout různých mezníků (100, 500, 1000, 5000, 10000 kliků), které odemykají achievementy. Hra slouží jako zábavný projekt pro naučení základy Pygame a event-driven programování.

Popis funkcionality programu
Hlavní okno: 800x600 pixelů s červeným tlačítkem uprostřed (100x100 px).

Klikání: Levým tlačítkem myši na tlačítko zvyšuje skóre o 1.

Achievementy: Automaticky se odemykají při dosažení přesných mezníků a zobrazují se pod skóre.

Zobrazení: Skóre nahoře, odemčené achievementy pod ním v seznamu.

Ukončení: Zavřením okna.

Hra běží v nekonečné smyčce, aktualizuje se 60 FPS díky pygame.display.flip().

Technická část
Použité knihovny:

pygame: Hlavní knihovna pro grafiku, eventy, vykreslování a správu okna.

sys: Pro sys.exit() při ukončení.

Datové struktury:

score: Integer pro aktuální počet kliků (inicializováno na 0).

achievements: List tuple (threshold: int, name: str) definující mezníky.

unlocked_achievements: List stringů pro uložené odemčené achievementy (zabrání duplicitám).

Algoritmy a logika:

Detekce kliku: button_rect.collidepoint(event.pos) kontroluje kolize s tlačítkem.

Kontrola achievementů: Lineární procházení listu achievements; pokud score == threshold a achievement není odemčený, přidá se do unlocked_achievements.

Vykreslování: pygame.Rect pro tlačítko, pygame.font.SysFont pro text, dynamické pozicování achievementů pomocí proměnné achievement_y.

Hlavní smyčka:

Zpracování eventů (QUIT, MOUSEBUTTONDOWN).

Vyčištění obrazovky (screen.fill(WHITE)).

Vykreslení tlačítka, skóre a achievementů.

Aktualizace displeje (pygame.display.flip()).

Kód je efektivní pro jednoduchou hru, bez externích API nebo složitých algoritmů.