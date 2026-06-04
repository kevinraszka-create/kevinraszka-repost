Název projektu: EA Life Simulator

Popis a cíl projektu:
EA Life Simulator je jednoduchý program napsaný v jazyce Python, který paroduje systém DLC a mikrotransakcí ve videohrách. Uživatel ovládá postavu, která se po narození může pokoušet vykonávat různé činnosti. Některé činnosti jsou uzamčeny a je potřeba je nejprve „zakoupit“. Cílem projektu je procvičit práci s funkcemi, podmínkami, cykly, proměnnými a tvorbou jednoduchého grafického rozhraní.

Popis funkcionality programu:
Po spuštění programu se zobrazí menu s několika možnostmi. Uživatel může zvolit mluvení, chůzi, pláč nebo ukončení programu. Mluvení a chůze jsou na začátku uzamčené. Pokud se je uživatel pokusí použít, otevře se okno simulující nákup DLC. Po potvrzení nákupu se daná funkce odemkne a lze ji používat. Funkce pláče je dostupná zdarma a pouze vypisuje text do konzole. Program běží v cyklu, dokud uživatel nezvolí ukončení.

Technická část:
Program je vytvořen v Pythonu a využívá knihovnu Tkinter pro tvorbu grafických oken a dialogů. K ukládání informací o zakoupených DLC používá logické proměnné typu Boolean. Program využívá funkce pro oddělení jednotlivých částí logiky, podmínky pro kontrolu odemčených funkcí a nekonečný cyklus pro opakované zobrazování menu. Součástí programu jsou také události spojené s klikáním na tlačítka v grafickém rozhraní. Program nevyužívá žádné externí API, databázi ani vlastní složité datové struktury.