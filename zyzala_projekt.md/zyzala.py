import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (0, -1)  # Start moving up
    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = ((head_x + dir_x) % GRID_WIDTH, (head_y + dir_y) % GRID_HEIGHT)
        self.positions.insert(0, new_head)
        self.positions.pop()  # Remove tail
    def change_direction(self, new_direction):
        opposite_direction = (-self.direction[0], -self.direction[1])
        if new_direction != opposite_direction:
            self.direction = new_direction
# Snake settings
snake_pos = [300,200]
snake_size = 20
speed = 5
food_size = 20
width, height = 600, 400

# Direction
dx = 0
dy = 0

clock = pygame.time.Clock()

# Move snake
snake_pos[0] += dx
snake_pos[1] += dy

 # Draw
screen.fill(black)
pygame.draw.rect(screen, green, (snake_pos[0], snake_pos[1], snake_size, snake_size))
pygame.display.update()
clock.tick(60)

    # mimo while loop
food_pos = [random.randint(0, width - food_size), random.randint(0, height - food_size)]

    # ve while loop
snake_rect = pygame.Rect(snake_pos[0], snake_pos[1], snake_size, snake_size)
food_rect = pygame.Rect(food_pos[0], food_pos[1], food_size, food_size)

if snake_rect.colliderect(food_rect):
        food_pos = [random.randint(0, width - food_size), random.randint(0, height - food_size)]

    # Draw
screen.fill(black)
pygame.draw.rect(screen, green, snake_rect)
pygame.draw.rect(screen, red, food_rect)
pygame.display.update()
clock.tick(60)


    