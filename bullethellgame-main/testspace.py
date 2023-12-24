import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

# Set background
background = pygame.image.load('background/backgroundgame1.png')

# Set the title of the window
pygame.display.set_caption("My Game")

# Define the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set the font
font = pygame.font.SysFont('cambria', 32)
fire_mode_test1 = font.render('Fire Mode : 1', True, white)
fire_mode_test2 = font.render('Fire Mode : 2', True, white)
fire_mode_rect = (50, 1027)
score = 0
score_text = font.render('Score:' + str(score), True, white)
score_rect = (1700, 1027)
game_over_text = font.render('Game Over', True, white)

# Set the clock
clock = pygame.time.Clock()

# Define the sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('graphics/p2_0.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cooldown_count = 0
        self.fire_mode = 0
        self.tab_cooldown = 10

    def cooldown(self):
        if self.cooldown_count >= 20:
            self.cooldown_count = 0
        elif self.cooldown_count > 0:
            self.cooldown_count += 1
        if self.tab_cooldown < 10:
            self.tab_cooldown += 1

    def update(self):
        self.cooldown()

# Define the bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('bullets/bullet1v2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 10
        if self.rect.y < 0:
            self.kill()

class Bullet2Up(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('bullets/bulletupv2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 5
        if self.rect.y < 0:
            self.kill()

class Bullet2Right(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('bullets/bulletrightv2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 5
        self.rect.x += 5
        if self.rect.y < 0:
            self.kill()

class Bullet2Left(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('bullets/bulletleftv2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 5
        self.rect.x -= 5
        if self.rect.y < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('graphics/monster1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.facing = random.choice(['left', 'right'])
        self.x_change = 0
        self.y_change = 0
        self.movement_loop = 0
        self.max_travel = 10

    def movement(self):
        if self.facing == 'left':
            self.x_change -= 4
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = 'right'
        if self.facing == 'right':
            self.x_change += 4
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = 'left'

    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


class Boss1_Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('graphics/boss1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.facing = random.choice(['left', 'right'])
        self.facingy = random.choice(['up', 'down'])
        self.x_change = 0
        self.y_change = 0
        self.movement_loop = 0
        self.movement_loopy = 0
        self.max_travel = random.randint(250, 300)
        self.hp = 1000
        self.cooldown = 0
        self.alive = True

    def movement(self):
        if self.facing == 'left':
            self.x_change -= 4
            self.movement_loop -= 1
            if self.rect.x <= 100:
                self.facing = 'right'
            elif self.movement_loop <= -self.max_travel:
                self.facing = random.choice(['left', 'right'])
                self.facingy = random.choice(['up', 'down'])
        if self.facing == 'right':
            self.x_change += 4
            self.movement_loop += 1
            if self.rect.x >= 1820:
                self.facing = 'left'
            elif self.movement_loop >= self.max_travel:
                self.facing = random.choice(['left', 'right'])
                self.facingy = random.choice(['up', 'down'])
        if self.facingy == 'up':
            self.y_change -= 4
            self.movement_loopy -= 1
            if self.rect.y <= 25:
                self.facingy = 'down'
            elif self.movement_loopy <= -self.max_travel:
                self.facingy = random.choice(['up', 'down'])
                self.facing = random.choice(['left', 'right'])
        if self.facingy == 'down':
            self.y_change += 4
            self.movement_loopy += 1
            if self.rect.y >= 380:
                self.facingy = 'up'
            elif self.movement_loopy >= self.max_travel:
                self.facingy = random.choice(['up', 'down'])
                self.facing = random.choice(['left', 'right'])


    def boss_cooldown(self):
        if self.cooldown >= 0:
            self.cooldown += 1
            if self.cooldown >= 40:
                self.cooldown = 0

    def update(self):
        self.boss_cooldown()
        self.movement()
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

        if pygame.sprite.groupcollide(bullet1_group, boss1_group, True, False):
            self.hp -= 50
        if pygame.sprite.groupcollide(bullet2_group, boss1_group, True, False):
            self.hp -= 25
        if self.hp <= 0:
            self.alive = False
            self.kill()


class Boss1_Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('graphics/boss1proj/boss1proj.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += 3
        if self.rect.y > 1180:
            self.kill()

# Create the sprite group and the bullet group
sprite_group = pygame.sprite.Group()
bullet1_group = pygame.sprite.Group()
bullet2_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
boss1_group = pygame.sprite.Group()
boss1_proj_group = pygame.sprite.Group()

# Add the sprite to the sprite group
level = 1
testx = 100
deadboss = 0
dummy = 0
player = Player(947, 999)
boss1 = Boss1_Enemy(540, 50)
enemies = []
def spawn_enemies(x, y, z):
    if z > 0:
        spawn_enemies(x + 50, y, z - 1)
    enemies.append(Enemy(x, y))

spawn_enemies(100, 50, 35)

sprite_group.add(enemies)
player_group.add(player)


def restart():
    sprite_group.add(enemies)
    if len(player_group) == 0:
        player_group.add(player)
    if len(boss1_group) == 1:
        boss1.kill()


# Set the game loop
running = True
while running:
    print(boss1.facing)
    print(boss1.facingy)
    print(boss1.rect.x)
    print(boss1.rect.y)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Move the sprite based on the keys pressed
    if keys[pygame.K_a]:
        player.rect.x -= 5
    if keys[pygame.K_d]:
        player.rect.x += 5
    if keys[pygame.K_w] and player.rect.y >= 540:
        player.rect.y -= 5
    if keys[pygame.K_s]:
        player.rect.y += 5

    #restart
    if keys[pygame.K_r]:
        restart()
        level = 1
        score = 0

    # change fire mode
    if keys[pygame.K_TAB] and player.tab_cooldown == 10:
        if player.fire_mode == 0:
            player.fire_mode = 1
            player.tab_cooldown = 0
        elif player.fire_mode == 1:
            player.fire_mode = 0
            player.tab_cooldown = 0

    # Shoot a bullet when the space bar is pressed
    if (keys[pygame.K_SPACE] and player.cooldown_count == 0 and player.fire_mode == 0):
        bullet = Bullet(player.rect.x, player.rect.y-15)
        player.cooldown_count = 1
        bullet1_group.add(bullet)
    elif (keys[pygame.K_SPACE] and player.cooldown_count == 0 and player.fire_mode == 1):
        bullet2up = Bullet2Up(player.rect.x, player.rect.y-5)
        bullet2right = Bullet2Right(player.rect.x, player.rect.y-5)
        bullet2left = Bullet2Left(player.rect.x, player.rect.y-5)
        player.cooldown_count = 1
        bullet2_group.add(bullet2up, bullet2right, bullet2left)

    # Update the sprite and the bullet groups
    sprite_group.update()
    bullet1_group.update()
    bullet2_group.update()
    player.update()
    boss1_group.update()
    boss1_proj_group.update()

    # Boss Proj
    if boss1.cooldown == 0 and len(boss1_group) == 1:
        boss1proj = Boss1_Bullet(boss1.rect.x, boss1.rect.y+10)
        boss1_proj_group.add(boss1proj)

    # Check for collisions between the bullet group and the sprite group
    collisions = pygame.sprite.groupcollide(sprite_group, bullet1_group, False, True)
    for sprite, bullets in collisions.items():
        sprite.kill()
        score += 1
        score_text = font.render('Score:' + str(score), True, white)

    collisions2 = pygame.sprite.groupcollide(sprite_group, bullet2_group, False, True)
    for sprite, bullets in collisions2.items():
        sprite.kill()
        score += 1
        score_text = font.render('Score:' + str(score), True, white)

    if pygame.sprite.groupcollide(boss1_proj_group, player_group, False, True):
        player.kill()

    # Clear the screen
    screen.fill(black)
    screen.blit(background, (0, 0))

    # Draw the sprite and the bullet groups
    player_group.draw(screen)
    sprite_group.draw(screen)
    bullet1_group.draw(screen)
    bullet2_group.draw(screen)
    boss1_group.draw(screen)
    boss1_proj_group.draw(screen)

    # Draw text
    if player.fire_mode == 0:
        screen.blit(fire_mode_test1, fire_mode_rect)
    elif player.fire_mode == 1:
        screen.blit(fire_mode_test2, fire_mode_rect)
    screen.blit(score_text, score_rect)

    # Move to next level
    if len(sprite_group) == 0 and level == 1:
        level += 1
        boss1_group.add(boss1)

    if not boss1.alive and level == 2:
        score += 1000
        level += 1
        score_text = font.render('Score:' + str(score), True, white)

    if len(player_group) == 0:
        screen.blit(game_over_text, (910, 540))


    # Update the display
    pygame.display.flip()

    # Set the FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
