import pygame
import sys

pygame.init()

# nastavení okna
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Reaction Game")

# hlavní smyčka hry
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # černá obrazovka