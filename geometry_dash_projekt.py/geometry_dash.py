import pygame
import random

# Inicializace Pygame
pygame.init()

# nastavení barev a rozměrů
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# nastavení okna
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Geometry Dash - Cube Jumper")

# Clock for controlling frame rate
clock = pygame.time.Clock()

class Cube: # Hlavní postava - kostka
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT - 100
        self.width = 50
        self.height = 50
        self.velocity = 0
        self.is_jumping = False
        self.jump_power = -15
        self.gravity = 0.8

    def jump(self): # Skok kostky
        if not self.is_jumping:
            self.velocity = self.jump_power
            self.is_jumping = True

    def update(self): # Aktualizace pozice kostky
        # potlačujeme gravitaci a aktualizujeme pozici
        self.velocity += self.gravity
        self.y += self.velocity

        # koukáme, jestli kostka nedosáhla země
        if self.y >= SCREEN_HEIGHT - 100:
            self.y = SCREEN_HEIGHT - 100
            self.velocity = 0
            self.is_jumping = False

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

class Obstacle: # Překážka - hroty
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = SCREEN_HEIGHT - 100
        self.width = 50
        self.height = 50
        self.speed = 5

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        # Spike (trojúhelník)
        pygame.draw.polygon(screen, RED, [
            (self.x, self.y + self.height),
            (self.x + self.width / 2, self.y),
            (self.x + self.width, self.y + self.height)
        ])

def main(): # Hlavní herní smyčka
    cube = Cube()
    obstacles = []
    score = 0
    font = pygame.font.SysFont(None, 36)

    running = True
    game_over = False

    while running: # Hlavní herní smyčka
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    cube.jump()

                if event.key == pygame.K_r and game_over:
                    cube = Cube()
                    obstacles = []
                    score = 0
                    game_over = False

        if not game_over:
            cube.update()

            # Check if cube fell below the screen
            if cube.y > SCREEN_HEIGHT:
                game_over = True

            for obstacle in obstacles[:]:
                obstacle.update()

                if obstacle.x + obstacle.width < 0:
                    obstacles.remove(obstacle)
                    score += 1

                if (cube.x < obstacle.x + obstacle.width and
                    cube.x + cube.width > obstacle.x and
                    cube.y < obstacle.y + obstacle.height and
                    cube.y + cube.height > obstacle.y):
                    game_over = True

            if random.randint(1, 60) == 1:
                obstacles.append(Obstacle())


        screen.fill(WHITE)
        cube.draw(screen)

        for obstacle in obstacles:
            obstacle.draw(screen)

        score_text = font.render(f"Score: {score}", True, BLACK) # Zobrazování skóre
        screen.blit(score_text, (10, 10))

        if game_over:
            game_over_text = font.render("GAME OVER - Press R to Restart", True, RED)
            screen.blit(game_over_text, (180, 180))

        pygame.display.flip()

# Spouštění hry
if __name__ == "__main__":
    main()
