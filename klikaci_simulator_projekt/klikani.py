import pygame
import sys

pygame.init()

# okno
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Klikací hra")

# barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# font
font = pygame.font.SysFont(None, 48)

# klikaci tlacitko
button_rect = pygame.Rect(width // 2 - 50, height // 2 - 50, 100, 100)

# skore
score = 0

# hlavni smycka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                score += 1
