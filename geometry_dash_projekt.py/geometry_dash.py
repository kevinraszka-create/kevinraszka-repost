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

class Spike:
    def __init__(self, x):
        self.x = x
        self.y = SCREEN_HEIGHT - 50
        self.width = 30
        self.height = 50
        self.speed = 5

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        # Draw a simple spike (triangle)
        points = [(self.x, self.y), (self.x + self.width//2, self.y - self.height), (self.x + self.width, self.y)]
        pygame.draw.polygon(screen, RED, points)

    def off_screen(self):
        return self.x + self.width < 0

def check_collision(cube, spike):
    cube_rect = pygame.Rect(cube.x, cube.y, cube.width, cube.height)
    spike_rect = pygame.Rect(spike.x, spike.y - spike.height, spike.width, spike.height)
    return cube_rect.colliderect(spike_rect)

def main():
    cube = Cube()
    spikes = []
    score = 0
    font = pygame.font.Font(None, 36)

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cube.jump()

        # Update cube
        cube.update()

        # Add new spikes
        if random.randint(1, 100) < 3:  # 3% chance each frame
            spikes.append(Spike(SCREEN_WIDTH))

        # Update and draw spikes
        for spike in spikes[:]:
            spike.update()
            spike.draw(screen)
            if spike.off_screen():
                spikes.remove(spike)
                score += 1
            elif check_collision(cube, spike):
                running = False  # Game over

        # Draw cube
        cube.draw(screen)

        # Draw score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    # Game over screen
    screen.fill(WHITE)
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, BLACK)
    screen.blit(game_over_text, (SCREEN_WIDTH//2 - 200, SCREEN_HEIGHT//2))
    restart_text = font.render("Press R to restart or Q to quit", True, BLACK)
    screen.blit(restart_text, (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2 + 50))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()  # Restart
                if event.key == pygame.K_q:
                    waiting = False

    pygame.quit()

if __name__ == "__main__":
    main()
