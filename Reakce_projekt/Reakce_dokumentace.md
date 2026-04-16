okumentace projektu: Reaction Game
Název projektu

Reaction Game

Popis a cíl projektu

Reaction Game je jednoduchá počítačová hra vytvořená v programovacím jazyce Python s využitím knihovny Pygame. Cílem projektu je vytvořit aplikaci, která dokáže měřit reakční čas uživatele na vizuální podnět.

Hlavním cílem hry je otestovat rychlost reakce hráče a zároveň slouží jako ukázka základních principů vývoje her, jako je práce s herní smyčkou, časováním a uživatelským vstupem.

Popis funkcionality programu

Po spuštění programu se zobrazí černé herní okno. Po náhodně zvoleném časovém intervalu v rozmezí 1 až 8 sekund se obrazovka změní na červenou barvu. Tento okamžik signalizuje hráči, že má co nejrychleji reagovat.

Hráč reaguje stisknutím klávesy Enter. Jakmile je klávesa stisknuta, program zaznamená čas reakce, obrazovka se změní na zelenou a zobrazí se naměřený reakční čas v milisekundách.

Program běží v nepřetržité smyčce, která zajišťuje aktualizaci stavu hry, zpracování vstupů a vykreslování grafiky.

Technická část
Použité knihovny
pygame – slouží k vytvoření herního okna, vykreslování grafiky, zpracování vstupů z klávesnice a práci s časem
random – používá se pro generování náhodného časového intervalu před změnou barvy
sys – umožňuje korektní ukončení programu
Algoritmy a logika programu

Program využívá jednoduchý časový algoritmus založený na porovnání aktuálního času s časem uloženým při spuštění programu. Náhodný časový interval určuje, kdy dojde ke změně stavu z čekání na reakci.

Reakční čas je vypočítán jako rozdíl mezi časem, kdy se obrazovka změnila na červenou, a časem, kdy hráč stiskl klávesu Enter.

Herní smyčka

Základem programu je nekonečná smyčka, která běží po celou dobu aplikace. V každé iteraci smyčky dochází k:

zpracování událostí (např. stisk klávesy nebo zavření okna),
aktualizaci herního stavu,
vykreslení aktuálního stavu na obrazovku.
Stavové proměnné

Program využívá několik proměnných pro řízení průběhu hry:

proměnná určující, zda již došlo ke změně na červenou barvu,
proměnná indikující, zda hráč již reagoval,
proměnné pro ukládání časových hodnot potřebných pro výpočet reakční doby.
Vykreslování

Grafika je vykreslována pomocí funkce pro vyplnění obrazovky barvou. Program používá tři základní barvy:

černá (výchozí stav),
červená (čekání na reakci),
zelená (zobrazení výsledku).

Text s výsledkem je vykreslen pomocí fontu dostupného v knihovně Pygame.