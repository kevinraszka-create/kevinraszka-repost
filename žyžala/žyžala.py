import pygame
import random
from enum import Enum

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class SnakeGame:
    def __init__(self, width=640, height=480, grid_size=20):
        pygame.init()
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.reset()
    
    def reset(self):
        self.snake = [(self.width // (2 * self.grid_size), self.height // (2 * self.grid_size))]
        self.direction = Direction.RIGHT
        self.food = self.spawn_food()
        self.score = 0
    
    def spawn_food(self):
        while True:
            food = (random.randint(0, self.width // self.grid_size - 1),
                   random.randint(0, self.height // self.grid_size - 1))
            if food not in self.snake:
                return food
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != Direction.DOWN:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
                    self.direction = Direction.DOWN
                elif event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                    self.direction = Direction.RIGHT
        return True
    
    def update(self):
        head_x, head_y = self.snake[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        
        if (new_head[0] < 0 or new_head[0] >= self.width // self.grid_size or
            new_head[1] < 0 or new_head[1] >= self.height // self.grid_size or
            new_head in self.snake):
            return False
        
        self.snake.insert(0, new_head)
        
        if new_head == self.food:
            self.score += 10
            self.food = self.spawn_food()
        else:
            self.snake.pop()
        
        return True
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        
        for segment in self.snake:
            rect = pygame.Rect(segment[0] * self.grid_size, segment[1] * self.grid_size,
                             self.grid_size - 2, self.grid_size - 2)
            pygame.draw.rect(self.screen, (0, 255, 0), rect)
        
        food_rect = pygame.Rect(self.food[0] * self.grid_size, self.food[1] * self.grid_size,
                               self.grid_size - 2, self.grid_size - 2)
        pygame.draw.rect(self.screen, (255, 0, 0), food_rect)
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            running = self.handle_input()
            running = self.update() and running
            self.draw()
            self.clock.tick(10)
        
        pygame.quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()