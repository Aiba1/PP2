import pygame
from random import randint

pygame.init()

heigh = 600
width = 400

screen = pygame.display.set_mode((width,heigh))

#images
image_back = pygame.image.load(r"C:\Users\Aibar\Desktop\pp2\practice\lab8\racer\AnimatedStreet.png")
image_player = pygame.image.load(r"C:\Users\Aibar\Desktop\pp2\practice\lab8\racer\Player.png")
image_enemy = pygame.image.load(r"C:\Users\Aibar\Desktop\pp2\practice\lab8\racer\Enemy.png")
image_coin = pygame.image.load(r"C:\Users\Aibar\Desktop\pp2\practice\lab8\racer\coin.png").convert_alpha()
image_coin = pygame.transform.smoothscale(image_coin,(30,30))

#sound
pygame.mixer.Sound(r"C:\Users\Aibar\Desktop\pp2\practice\lab8\racer\background.wav").play(loops=-1)
audio_crash =pygame.mixer.Sound(r"C:\Users\Aibar\Desktop\pp2\practice\lab8\racer\crash.wav")

#variables
score = 0
speed_player = 10
speed_enemy = 5
speed_coin = 5
tncoins = 10
level = 1

#color
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#font
font = pygame.font.SysFont("verdana", 20)
font_big = pygame.font.SysFont("verdana", 30)
progress = font.render("Score: " + str(score), True, BLACK)

#object classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, heigh - 50)
    def move(self):
        keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if keys[pygame.K_LEFT]:
                self.rect.move_ip(-speed_player, 0)
        if self.rect.right < width:
            if keys[pygame.K_RIGHT]:
                self.rect.move_ip(speed_player, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.rect.center = (randint(50,width-50), 0)
    def move(self):
        self.rect.move_ip(0, speed_enemy)
        if self.rect.top >= heigh:
            self.rect.center = (randint(50,width-50), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin
        self.rect = self.image.get_rect()
        self.rect.center = (randint(30, width - 30), 0)
    def move(self):
        self.rect.move_ip(0, speed_coin)
        if self.rect.top >= heigh:
            self.rect.center = (randint(30, width - 30), 0)
    def points(self):
        global score
        self.rect.center = (randint(30, width - 30), 0)
        score += randint(0,10)



P = Player()
E = Enemy()
C = Coin()

#groups
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites.add(P)
all_sprites.add(E)
all_sprites.add(C)
enemies.add(E)
coins.add(C)

#clock
clock = pygame.time.Clock()
FPS = 60

done = False
game_over = False

#game loop
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #texts on screen
    progress = font.render("Score: " + str(score), True, BLACK)
    result = font_big.render("Game_over  Result = " + str(score), True, BLUE)
    result1 = font_big.render("Press space", True, BLUE)
    lvl = font.render("Level" + str(level), True, BLACK)

    if not game_over:
        screen.blit(image_back, (0, 0))


        screen.blit(progress,(10, 10))
        screen.blit(lvl, (10, 30))

        #blitting the objects
        for entity in all_sprites:
            entity.move()
            screen.blit(entity.image, entity.rect)

        #checking for collision
        if pygame.sprite.spritecollideany(P, enemies):
            screen.fill(RED)
            screen.blit(result,(20, heigh // 2))
            screen.blit(result1,(20, (heigh // 2) + 30))
            for entity in all_sprites:
                entity.kill()
            game_over = True
            
        #collision with coins
        if pygame.sprite.spritecollideany(P, coins):
            for entity in coins:
                entity.points()
            if score == tncoins:
                tncoins += 10
                speed_enemy += 5
                level += 1
    #game over screen
    else:
        screen.fill(RED)
        screen.blit(result,(20, heigh // 2))
        screen.blit(result1,(20, (heigh // 2) + 30))

        P.rect.center = (width // 2, heigh - 50)
        E.rect.center = (randint(50, width - 50), 0)
        C.rect.center = (randint(30, width - 30), 0)
        
        for entity in all_sprites:
            entity.kill()

        all_sprites.add(P)
        all_sprites.add(E)
        all_sprites.add(C)
        enemies.add(E)
        coins.add(C)

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_over = False
            score = 0

    pygame.display.flip()
    clock.tick(FPS)
    
    
