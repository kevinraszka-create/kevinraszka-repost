import pygame
import sys
import random

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Reaction Game")

font = pygame.font.SysFont(None, 50)

wait_time = random.randint(1000, 8000)
start_time = pygame.time.get_ticks()

red = False
reaction_time = None
clicked = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if red and not clicked:
                    reaction_time = pygame.time.get_ticks() - red_time
                    clicked = True

    current_time = pygame.time.get_ticks()

    # změna na červenou
    if not red and current_time - start_time > wait_time:
        red = True
        red_time = pygame.time.get_ticks()  # začátek měření

    # vykreslování
    if not red:
        screen.fill((0, 0, 0))

    elif red and not clicked:
        screen.fill((255, 0, 0))

    elif clicked:
        screen.fill((0, 255, 0))
        text = font.render(f"Reaction time: {reaction_time} ms", True, (0, 0, 0))
        screen.blit(text, (200, 250))

    pygame.display.flip()

pygame.quit()
sys.exit()  
0
