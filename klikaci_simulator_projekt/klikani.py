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

# skore a achievementy
score = 0
achievements = [
    (100, "100 kliků"),
    (500, "500 kliků"),
    (1000, "1000 kliků"),
    (5000, "5000 kliků"),
    (10000, "10000 kliků"),
]
unlocked_achievements = []

# hlavni smycka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and button_rect.collidepoint(event.pos):
                score += 1
                for threshold, name in achievements:
                    if score == threshold and name not in unlocked_achievements:
                        unlocked_achievements.append(name)

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, button_rect)

    score_text = font.render(f"Skóre: {score}", True, BLACK)
    score_rect = score_text.get_rect(center=(width // 2, 50))
    screen.blit(score_text, score_rect)

    achievement_y = 110
    for achievement in unlocked_achievements:
        ach_text = font.render(f"Odemčeno: {achievement}", True, BLACK)
        ach_rect = ach_text.get_rect(center=(width // 2, achievement_y))
        screen.blit(ach_text, ach_rect)
        achievement_y += 40

    pygame.display.flip()

pygame.quit()
sys.exit()
