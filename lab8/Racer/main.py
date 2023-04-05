import pygame
import random

#MAIN VALUE OF SPEED OF OBJECTS
dx = 10


#DEFINING THE CLASS OF COINS
class Coin(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        super().__init__()
        #STANDARD PART FOR SPRITE DEFINITION
        self.image = img
        self.rect = self.image.get_rect()
        #MAKING OBJECTS APPEAR ON SPECIAL LINES OF THE ROAD
        self.positions = {0: (225, -64), 1: (350, -64), 2: (475, -64), 3: (600, -64)}
        self.pos = pos
        self.rect.center = self.positions[self.pos]
        self.dx = dx
        #ADDING AN OBJECT TO APPROPRIATE SPRITE GROUPS
        all_sprites.add(self)
        coins.add(self)
    
    def update(self):
        #CHANGING SPRITES' POSITION. IF IT GETS UNDER THE SCREEN, THEN IT DISAPPEARS
        self.rect.center = (self.rect.center[0], self.rect.center[1] + self.dx)
        if self.rect.center[1] >= 625:
            self.kill()


#DEFINING CAR CLASS
class Car(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        super().__init__()
        #ROTATING CARS, SO WE HAVE 2 DIRECTIONS OF OTHER CAR MOTIONS
        if pos < 2:
            self.image = pygame.transform.rotate(img, 180)
        else:
            self.image = img
        self.rect = self.image.get_rect()
        self.positions = {0: (225, -64), 1: (350, -64), 2: (475, -64), 3: (600, -64)}
        self.pos = pos
        self.rect.center = self.positions[self.pos]
        self.dx = dx
        #ADDING AN OBJECT TO APPROPRIATE GROUP
        all_sprites.add(self)
        cars.add(self)
    
    def update(self):
        #CHANGINS SPRITES POSITION. IF IT GETS UNDER THE SCREEN, THEN IT DISAPPEARS
        self.rect.center = (self.rect.center[0], self.rect.center[1] + self.dx)
        if self.rect.center[1] >= 625:
            self.kill()


#DEFINING PLAYER CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (225, 550)
        self.positions = {0: (225, 550), 1: (350, 550), 2: (475, 550), 3: (600, 550)}
        self.index = 2
        all_sprites.add(self)
    
    def update(self):
        #BASICALLY PLAYER IS ONLY ABLE TO CHANGE ROAD LINE
        self.rect.center = self.positions[self.index]


#FUNCTION SPAWNS CARS IN SOME PERIOD OF TIME
def spawn_cars():
    global last_spawn
    if len(cars) < 3:
        now = pygame.time.get_ticks()
        choose = [0, 1, 2, 3]
        if (now - last_spawn) / 1000  >= 0.5:
            new_car = Car(player_sprite, random.choice(choose))
            last_spawn = now


#FUNCTION SPAWNS COINS IN SOME PERIOD OF TIME
def spawn_coins():
    global last_coin_spawn
    if len(coins) < 3:
        now = pygame.time.get_ticks()
        choose = [0, 1, 2, 3]
        if (now - last_coin_spawn) / 1000  >= 0.5:
            new_coin = Coin(coin_pic, random.choice(choose))
            last_coin_spawn = now


#INITIALIZING MAIN GAME SETTINGS
pygame.init()
screen = pygame.display.set_mode((835, 600))
clock = pygame.time.Clock()
FPS = 60
SCORE = 0
game = True


#CREATING SPRITE GROUPS REQUIRED
all_sprites = pygame.sprite.Group()
cars = pygame.sprite.Group()
coins = pygame.sprite.Group()


#LOADING REQUIRED PICTURES
player_sprite = pygame.image.load('car.png')
background = pygame.image.load('background.png')
coin_pic = pygame.image.load('binance.png')


#SPAWNING OBJECTS OF EACH CLASS
pl = Player(player_sprite)
new_car = Car(player_sprite, 1)
coin = Coin(coin_pic, 2)
last_coin_spawn = pygame.time.get_ticks()
last_spawn = pygame.time.get_ticks()


#LOADING AND CREATING A FONT
font = pygame.font.Font('ShootingStar-Bold.otf', 30)


#VARIABLES REQUIRED TO MAKE ROAD MOVE
x_bg = 0
dx = 10


#GAME LOOP
while game:
    #GOING THROUGH ALL EVENTS
    for event in pygame.event.get():
        #QUITING GAME
        if event.type == pygame.QUIT:
            game = False
        #MAKING A PLAYER'S CAR MOVE TO OTHER ROAD LINE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pl.index = max(0, pl.index - 1)
            if event.key == pygame.K_RIGHT:
                pl.index = min(3, pl.index + 1)
    #REQUIRED, SO OBJECTS DO NOT LEAVE TRACE AFTERS THEMSELF
    screen.fill((255, 255, 255))

    
    #MOVING THE BACKGROUND SO ILLUSION OF MOVEMENT IS CREATED
    x_loop = x_bg % 600
    screen.blit(background, (0, x_loop - 600))
    if x_loop < 600:
        screen.blit(background, (0, x_loop))
    x_bg += dx

    
    #SHOWING SCORE
    score_title = font.render('SCORE: {}'.format(SCORE), True, 'BLACK')
    screen.blit(score_title, (700, 0))

    
    #SPAWNING OBJECTS, IF NECESSARY
    spawn_cars()
    spawn_coins()


    #UPDATING AND DRAWING ALL SPRITES
    all_sprites.update()
    all_sprites.draw(screen)

    
    #PLAYER HITS A CAR, THEN GAME STOPS
    hit_player = pygame.sprite.spritecollide(pl, cars, True)
    if hit_player:
        game = False
    
    
    #PLAYER GETS A COIN, AND THEN THE SCORE IS UPDATED
    collect_coins = pygame.sprite.spritecollide(pl, coins, True)
    for i in collect_coins:
        SCORE += 1
    
    
    #COINS THAT SPAWN INSIDE OTHER CARS WILL DISAPPEAR
    other_collect_coins = pygame.sprite.groupcollide(coins, cars, True, False)

    
    #PYGAME REQUIREMENT FOR A PROPER WORK
    clock.tick(FPS)
    pygame.display.update()
    pygame.display.flip()


pygame.quit()