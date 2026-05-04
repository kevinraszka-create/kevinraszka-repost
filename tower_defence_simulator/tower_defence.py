import pygame
class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = (0, 255, 0)
        self.range = 100
        self.damage = 10

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def in_range(self, enemy):
        dx = enemy.x - self.x
        dy = enemy.y - self.y
        return dx * dx + dy * dy <= self.range * self.range
