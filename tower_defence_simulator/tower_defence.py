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


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.color = (255, 0, 0)
        self.speed = 2
        self.health = 100

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.speed


class Projectile:
    def __init__(self, x, y, target):
        self.x = x
        self.y = y
        self.target = target
        self.speed = 5
        self.damage = 10

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), 5)

    def move(self):
        dx = self.target.x - self.x
        dy = self.target.y - self.y
        dist = (dx**2 + dy**2)**0.5
        if dist > 0:
            self.x += self.speed * dx / dist
            self.y += self.speed * dy / dist
