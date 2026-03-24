import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Geometry Dash - Cube Jumper")

# Clock for controlling frame rate
clock = pygame.time.Clock()

class Cube:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT - 100
        self.width = 50
        self.height = 50
        self.velocity = 0
        self.is_jumping = False
        self.jump_power = -15
        self.gravity = 0.8

    def jump(self):
        if not self.is_jumping:
            self.velocity = self.jump_power
            self.is_jumping = True

    def update(self):
        # Apply gravity
        self.velocity += self.gravity
        self.y += self.velocity

        # Ground collision
        if self.y >= SCREEN_HEIGHT - 100:
            self.y = SCREEN_HEIGHT - 100
            self.velocity = 0
            self.is_jumping = False

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
class Obstacle:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = SCREEN_HEIGHT - 100
        self.width = 50
        self.height = 50
        self.speed = 5

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
def main():
    cube = Cube()
    obstacles = []
    score = 0
    font = pygame.font.SysFont(None, 36)

    running = True
    while running:
        clock.tick(60)  # 60 frames per second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cube.jump()
        # Update cube and obstacles\    cube.update()
        for obstacle in obstacles:
            obstacle.update()
            if obstacle.x + obstacle.width < 0:
                obstacles.remove(obstacle)
                score += 1
            if (cube.x < obstacle.x + obstacle.width and
                cube.x + cube.width > obstacle.x and
                cube.y < obstacle.y + obstacle.height and
                cube.y + cube.height > obstacle.y):
                running = False  # Game over

