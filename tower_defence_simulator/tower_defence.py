import pygame
import random
import sys

# Nastavení velikosti okna
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Cena věže a odměna za zabití nepřítele
TOWER_COST = 50
ENEMY_REWARD = 10


class Tower:
    def __init__(self, x, y):
        # Pozice věže
        self.x = x
        self.y = y

        # Velikost věže
        self.width = 50
        self.height = 50

        # Barva věže
        self.color = (0, 255, 0)

        # Dosah střelby
        self.range = 120

        # Poškození
        self.damage = 10

        # Level věže
        self.level = 1

        # Cena upgradu
        self.upgrade_cost = 50

        # Rychlost střelby (ms)
        self.fire_rate = 1000

        # Čas posledního výstřelu
        self.last_shot = 0

    @property
    def rect(self):
        # Vrací obdélník věže (pro kolize a klikání)
        return pygame.Rect(self.x, self.y, self.width, self.height)

    @property
    def center(self):
        # Vrací střed věže (pro střely)
        return (self.x + self.width / 2, self.y + self.height / 2)

    def draw(self, screen):
        # Vykreslení věže
        pygame.draw.rect(screen, self.color, self.rect)

        # Vykreslení jejího dosahu (kruh)
        pygame.draw.circle(screen, (0, 200, 0),
                           (int(self.center[0]), int(self.center[1])),
                           self.range, 1)

    def in_range(self, enemy):
        # Zjistí, jestli je nepřítel v dosahu věže
        dx = enemy.x + enemy.width / 2 - self.center[0]
        dy = enemy.y + enemy.height / 2 - self.center[1]

        # Porovnání vzdálenosti (bez odmocniny kvůli výkonu)
        return dx * dx + dy * dy <= self.range * self.range

    def can_shoot(self):
        # Kontroluje, jestli už může znovu střílet
        return pygame.time.get_ticks() - self.last_shot >= self.fire_rate

    def shoot(self):
        # Nastaví čas posledního výstřelu
        self.last_shot = pygame.time.get_ticks()

    def upgrade(self):
        # Zvýšení levelu
        self.level += 1

        # Vylepšení statistik
        self.damage += 5
        self.range += 15
        self.fire_rate = max(300, self.fire_rate - 100)

        # Zvýšení ceny dalšího upgradu
        self.upgrade_cost += 50

        # Změna barvy (vizuální indikace upgradu)
        self.color = (
            max(0, self.color[0] - 20),
            min(255, self.color[1] + 10),
            self.color[2]
        )


class Enemy:
    def __init__(self, x, y):
        # Pozice nepřítele
        self.x = x
        self.y = y

        # Velikost
        self.width = 20
        self.height = 20

        # Barva
        self.color = (255, 0, 0)

        # Rychlost
        self.speed = 2

        # Životy
        self.health = 10

    @property
    def rect(self):
        # Obdélník nepřítele
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        # Vykreslení nepřítele
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        # Pohyb doprava
        self.x += self.speed


class Projectile:
    def __init__(self, x, y, target, damage):
        # Pozice střely (float kvůli přesnosti)
        self.x = float(x)
        self.y = float(y)

        # Cíl
        self.target = target

        # Rychlost střely
        self.speed = 6

        # Poškození
        self.damage = damage

    def draw(self, screen):
        # Vykreslení střely
        pygame.draw.circle(screen, (0, 0, 255),
                           (int(self.x), int(self.y)), 5)

    def move(self):
        # Pokud cíl neexistuje nebo je mrtvý → nedělej nic
        if not self.target or self.target.health <= 0:
            return

        # Směr k cíli
        dx = self.target.x + self.target.width / 2 - self.x
        dy = self.target.y + self.target.height / 2 - self.y

        # Vzdálenost
        dist = (dx**2 + dy**2)**0.5

        # Normalizovaný pohyb směrem k cíli
        if dist > 0:
            self.x += self.speed * dx / dist
            self.y += self.speed * dy / dist


def main():
    # Inicializace pygame
    pygame.init()

    # Vytvoření okna
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tower Defence Simulator')

    # Font
    font = pygame.font.Font(None, 24)

    # Clock pro FPS
    clock = pygame.time.Clock()

    # Herní objekty
    towers = [Tower(200, 250)]
    enemies = []
    projectiles = []

    # Peníze
    money = 150

    # Vybraná věž
    selected_tower = None

    # Timer spawnování nepřátel
    spawn_timer = 0

    # HLAVNÍ HERNÍ SMYČKA
    while True:
        # Omezení FPS + delta time
        dt = clock.tick(60)
        spawn_timer += dt

        # ZPRACOVÁNÍ EVENTŮ
        for event in pygame.event.get():

            # Zavření hry
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Kliknutí myši
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                selected_tower = None

                # Kontrola, jestli klikl na věž
                for tower in towers:
                    if tower.rect.collidepoint(mouse_pos):
                        selected_tower = tower
                        break
                else:
                    # Pokud ne → postaví novou věž
                    if money >= TOWER_COST:
                        towers.append(
                            Tower(mouse_pos[0] - 25, mouse_pos[1] - 25)
                        )
                        money -= TOWER_COST

            # Klávesy
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u and selected_tower:
                    # Upgrade věže
                    if money >= selected_tower.upgrade_cost:
                        money -= selected_tower.upgrade_cost
                        selected_tower.upgrade()

        # SPAWN ENEMY
        if spawn_timer >= 2000:
            spawn_timer = 0
            enemy_y = random.randint(50, SCREEN_HEIGHT - 70)
            enemies.append(Enemy(-30, enemy_y))

        # POHYB A LOGIKA ENEMY
        for enemy in list(enemies):
            enemy.move()

            # Pokud uteče z obrazovky → smaž
            if enemy.x > SCREEN_WIDTH:
                enemies.remove(enemy)

            # Pokud zemře → přidej peníze
            elif enemy.health <= 0:
                enemies.remove(enemy)
                money += ENEMY_REWARD

        # STŘELBA VĚŽÍ
        for tower in towers:
            if tower.can_shoot():
                for enemy in enemies:
                    if tower.in_range(enemy):
                        tower.shoot()

                        # Vytvoření střely
                        px, py = tower.center
                        projectiles.append(
                            Projectile(px, py, enemy, tower.damage)
                        )
                        break

        # POHYB STŘEL
        for projectile in list(projectiles):
            projectile.move()

            if projectile.target and projectile.target.health > 0:
                dx = projectile.target.x + projectile.target.width / 2 - projectile.x
                dy = projectile.target.y + projectile.target.height / 2 - projectile.y

                # Kolize střely s cílem
                if dx * dx + dy * dy < 16:
                    projectile.target.health -= projectile.damage
                    projectiles.remove(projectile)
            else:
                projectiles.remove(projectile)

        # VYKRESLOVÁNÍ
        screen.fill((30, 30, 30))

        # Věže
        for tower in towers:
            tower.draw(screen)

            # Zvýraznění vybrané věže
            if tower is selected_tower:
                pygame.draw.rect(screen, (255, 255, 0), tower.rect, 3)

        # Enemy
        for enemy in enemies:
            enemy.draw(screen)

        # Střely
        for projectile in projectiles:
            projectile.draw(screen)

        # UI – peníze
        money_text = font.render(f'Money: ${money}', True, (255, 255, 255))
        screen.blit(money_text, (10, 10))

        # Instrukce
        instructions = [
            'Click to place a tower ($50)',
            'Click a tower and press U to upgrade',
            'Selected tower upgrade cost: ' +
            (str(selected_tower.upgrade_cost) if selected_tower else 'N/A')
        ]

        for i, line in enumerate(instructions):
            screen.blit(font.render(line, True, (200, 200, 200)),
                        (10, 35 + i * 20))

        pygame.display.flip()


# Spuštění programu
if __name__ == '__main__':
    main()