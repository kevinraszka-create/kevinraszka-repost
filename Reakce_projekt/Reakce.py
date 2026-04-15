import pygame
import sys
import random

pygame.init()

# nastavení okna
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Reaction Game")

# náhodný čas (v milisekundách)
wait_time = random.randint(1000, 8000)
start_time = pygame.time.get_ticks()

red = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()

    # když uběhne náhodný čas → změna na červenou
    if not red and current_time - start_time > wait_time:
        red = True

