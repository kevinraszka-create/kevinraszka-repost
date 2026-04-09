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
    def reset(self):
        self.platno = [[0 for _ in range(self.sirka)] for _ in range(self.vyska)]
        self.hrac = 1
    def vykresli(self, obrazovka):
        obrazovka.fill((255, 255, 255))
        for y in range(self.vyska):
            for x in range(self.sirka):
                if self.platno[y][x] == 1:
                    pygame.draw.circle(obrazovka, (255, 0, 0), (x * 40 + 20, y * 40 + 20), 15)
                elif self.platno[y][x] == 2:
                    pygame.draw.circle(obrazovka, (0, 0, 255), (x * 40 + 20, y * 40 + 20), 15)
        for i in range(1, self.sirka):
            pygame.draw.line(obrazovka, (0, 0, 0), (i * 40, 0), (i * 40, self.vyska * 40), 1)
        for i in range(1, self.vyska):
            pygame.draw.line(obrazovka, (0, 0, 0), (0, i * 40), (self.sirka * 40, i * 40), 1)

            def main():
                pygame.init()
                sirka, vyska = 15, 15
                obrazovka = pygame.display.set_mode((sirka * 40, vyska * 40))
                pygame.display.set_caption("Piskvorky")
                clock = pygame.time.Clock()
                hra = Piskvorky(sirka, vyska)
                
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            x, y = event.pos
                            x //= 40
                            y //= 40
                            hra.tah(x, y)
                            vysledek = hra.kontrola_vyhry()
                            if vysledek != 0:
                                print(f"Hráč {vysledek} vyhrál!")
                                hra.reset()
                    
                    hra.vykresli(obrazovka)
                    pygame.display.flip()
                    clock.tick(60)
                
