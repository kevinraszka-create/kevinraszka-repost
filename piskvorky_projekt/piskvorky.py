import pygame
class Piskvorky:
    def __init__(self, sirka, vyska):
        self.sirka = sirka
        self.vyska = vyska
        self.platno = [[0 for _ in range(sirka)] for _ in range(vyska)]
        self.hrac = 1

    def tah(self, x, y):
        if self.platno[y][x] == 0:
            self.platno[y][x] = self.hrac
            if self.hrac == 1:
                self.hrac = 2
            else:
                self.hrac = 1
            return True
        return False

    def kontrola_vyhry(self):
        for y in range(self.vyska):
            for x in range(self.sirka):
                if self.platno[y][x] != 0:
                    hrac = self.platno[y][x]
                    # Kontrola horizontálního směru
                    if x + 4 < self.sirka and all(self.platno[y][x+i] == hrac for i in range(5)):
                        return hrac
                    # Kontrola vertikálního směru
                    if y + 4 < self.vyska and all(self.platno[y+i][x] == hrac for i in range(5)):
                        return hrac
                    # Kontrola diagonálního směru (pravý dolů)
                    if x + 4 < self.sirka and y + 4 < self.vyska and all(self.platno[y+i][x+i] == hrac for i in range(5)):
                        return hrac
                    # Kontrola diagonálního směru (levý dolů)
                    if x - 4 >= 0 and y + 4 < self.vyska and all(self.platno[y+i][x-i] == hrac for i in range(5)):
                        return hrac
        return 0