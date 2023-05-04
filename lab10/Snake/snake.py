import pygame
import random
import psycopg2 as ps





sql = '''
    INSERT INTO snake VALUES (DEFAULT,%s,%s) ;
'''

upd_sql = '''
UPDATE snake
SET score = %s
WHERE name = %s;
'''
print_sql = '''
SELECT name, score FROM snake
GROUP BY name, score
ORDER BY score DESC
'''


conn = ps.connect(host = 'localhost',
                  dbname = 'players',
                  user = 'postgres',
                  password = '1234',
                  port = '5432'
)

cur = conn.cursor()



#DEFINING DIRECTIONS FOR SNAKE
directions = {'UP': (0, -50),
              'DOWN': (0, 50),
              'LEFT': (-50, 0),
              'RIGHT': (50, 0)
             }


#CREATING POSSIBLE POSITIONS FOR FOOD TO SPAWN
positions = []
x, y = 25, 25
for i in range(20):
    x = 25 + 50 * i
    y = 25
    for i in range(16):
        positions.append((x, y))
        y += 50


#CREATING SPRITE GROUP
all_sprites = pygame.sprite.Group()
fruits = pygame.sprite.Group()


#DEFINING FRUIT CLASS WITH THE MAIN PROPERTIES
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.value = random.randint(1, 3)
        self.time = pygame.time.get_ticks()
        if self.value == 2:
            self.image.fill('GREEN')
        if self.value == 3:
            self.image.fill('RED')
        self.rect = self.image.get_rect()
        t = random.choice(positions)
        #AVOIDING SPAWNING OF A FRUIT ON A SNAKE
        while t in [i.rect.center for i in all_sprites]:
            t = random.choice(positions)
        self.rect.center = t
        all_sprites.add(self)
        fruits.add(self)

    def update(self):
        #DESTROYING FOOD IF IT HAS BEEN ON SCREEN TOO LONG
        now = pygame.time.get_ticks()
        if self.value == 1:
            if (now - self.time) // 1000 >= 7:
                self.kill()
                self = Fruit()
                self.time = now
        if self.value == 2:
            if (now - self.time) // 1000 >= 5:
                self.kill()
                self = Fruit()
                self.time = now
        if self.value == 3:
            if (now - self.time) // 1000 >= 3:
                self.kill()
                self = Fruit()
                self.time = now

test = Fruit()
    

#DEFINING BLOCK OF A SNAKES' BODY
class Block(pygame.sprite.Sprite):
    def __init__(self, coords, direction):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.dx, self.dy = directions[direction]
        all_sprites.add(self)
    
    
    def update(self):
        self.rect.center = (self.rect.center[0] + self.dx, self.rect.center[1] + self.dy)


#CREATING A SNAKE CLASS
class Snake:
    #INITIALIZING A SNAKE
    def __init__(self):
        self.body = [Block((425, 375), 'RIGHT'), Block((375, 375), 'RIGHT'), Block((325, 375), 'RIGHT')]
        self.turn = dict()

    
    def update(self):
        global running
        keystate = pygame.key.get_pressed()
        

        #CHECKING COLLISIONS WITH WALLS AND OTHER BLOCKS OF A BODY
        if self.body[0].rect.center[0] > 1000 or self.body[0].rect.center[0] < 0:
            running = False
            cur.execute(upd_sql,(SCORE, name))
            cur.execute(sql,(name,SCORE))
            for i in self.body:
                i.dx, i.dy = 0, 0
            return
        if self.body[0].rect.center[1] > 800 or self.body[0].rect.center[1] < 0:
            running = False
            cur.execute(upd_sql,(SCORE, name))
            cur.execute(sql,(name,SCORE))
            for i in self.body:
                i.dx, i.dy = 0, 0
            return
        if self.body[0].rect.center in [i.rect.center for i in self.body[1:]]:
            running = False
            cur.execute(upd_sql,(SCORE, name))
            cur.execute(sql,(name,SCORE))
            for i in self.body:
                i.dx, i.dy = 0, 0
            return
        

        #TURNS USING ARROW KEYS
        if keystate[pygame.K_DOWN] and self.body[0].dy == 0:
            self.turn[self.body[0].rect.center] = directions['DOWN']
        if keystate[pygame.K_UP] and self.body[0].dy == 0:
            self.turn[self.body[0].rect.center] = directions['UP']
        if keystate[pygame.K_LEFT] and self.body[0].dx == 0:
            self.turn[self.body[0].rect.center] = directions['LEFT']
        if keystate[pygame.K_RIGHT] and self.body[0].dx == 0:
            self.turn[self.body[0].rect.center] = directions['RIGHT']
        

        #UPDATING BODY DIRECTIONS(SO SNAKE TURNS PROPERPLY)
        for i in self.body:
            if i.rect.center in self.turn.keys():
                i.dx, i.dy = self.turn[i.rect.center]
                if i == self.body[-1]:
                    self.turn.pop(i.rect.center)

    #ADDING A BLOCK TO A SNAKE'S TAIL IN AN APPROPRIATE DIRECTION
    def add_block(self):
        if self.body[-1].dx == 50:
            coords = (self.body[-1].rect.center[0] - 50, self.body[-1].rect.center[1])
            direction = 'RIGHT'
        elif self.body[-1].dx == -50:
            coords = (self.body[-1].rect.center[0] + 50, self.body[-1].rect.center[1])
            direction = 'LEFT'
        elif self.body[-1].dy == 50:
            coords = (self.body[-1].rect.center[0], self.body[-1].rect.center[1] - 50)
            direction = 'DOWN'
        elif self.body[-1].dy == -50:
            coords = (self.body[-1].rect.center[0], self.body[-1].rect.center[1] + 50)
            direction = 'UP'
        self.body.append(Block(coords, direction))

pygame.init()
name = input("Enter your name:")
with conn.cursor() as cur:
        cur.execute("SELECT name FROM snake WHERE name=%s", (name,))
        result = cur.fetchone()
        
        if result is not None:
            # User exists, show current level
            name = result[0]
            cur.execute("SELECT score FROM snake WHERE name=%s ORDER BY name DESC LIMIT 1", (name,))
            result = cur.fetchone()
            
            if result is not None:
                score = result[0]
                print(f"Welcome back, {name}! Your score {score}.")
            else:
                print(f"Welcome back, {name}!")
        else:
            # User does not exist, create new user
            cur.execute("INSERT INTO snake (name, score) VALUES (%s, %s) RETURNING name", (name, 0))
            name = cur.fetchone()[0]
            print(f"Welcome, {name}!")
conn.commit()


#INITIALIZING MAIN GAME SETTINGS
WIDTH = 20 * 50
HEIGHT = 20 * 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60
running = True
main_menu_status = True
snake = Snake()



#LOADING AND CREATING FONTS
font_file = open('ShootingStar-Bold.otf')
font = pygame.font.Font(font_file, 100)
caption = font.render('Snake', True, (0, 0, 0))
score_title = pygame.font.Font(font_file, 30)


#DEFINING LEVEL, INITIAL SCORE, AND A SPEED OF A LEVEL
LEVEL_SPEED = (120, 20)
LEVEL = 1
SCORE = 0


#CHECKES IF THERE IS NO FOOD ON THE SCREEN
def spawn_food():
    if not fruits:
        new_fruit = Fruit()

#CHANGES SPEED IF PLAYER GOES TO AN ANOTHER LEVEL
def change_speed():
    global LEVEL_SPEED, LEVEL, SCORE
    LEVEL += 1
    LEVEL_SPEED = (max(0, LEVEL_SPEED[0] - 2), LEVEL_SPEED[1] + 2)


#MAIN MENU LOOP
def main_menu():
    global main_menu_status, running
    while main_menu_status:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                main_menu_status = False
                running = False
                continue
    
            key_state = pygame.key.get_pressed()
            if key_state[pygame.K_SPACE]:
                main_menu_status = False

        screen.fill((255, 255, 255))
        screen.blit(caption, (WIDTH // 2 - 100, HEIGHT // 2 - 75))


        pygame.display.flip()
        pygame.display.update()


main_menu()


#MAIN LOOP
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            cur.close()
            conn.close()
            exit()


    screen.fill((255, 255, 255))

    
    #SHOWING LEVEL AND SCORE
    level_caption = score_title.render('LEVEL: {}'.format(LEVEL), True, 'BLUE')
    score = score_title.render('SCORE: {}'.format(SCORE), True, 'BLUE')
    screen.blit(level_caption, (875, 0))
    screen.blit(score, (875, 50))


    #CHECKING EATEN FOOD AND UPDATING LENGTH OF SNAKE AND SCORE
    eat = pygame.sprite.spritecollide(snake.body[0], fruits, True)
    for i in eat:
        SCORE += i.value
        if not SCORE % 4:
            change_speed()
        for j in range(i.value):
            snake.add_block()
    

    spawn_food()

    #UPDATING ALL SPRITES AND DRAWING THEM
    snake.update()
    all_sprites.update()
    all_sprites.draw(screen)

    
    #SPEED OF A GAME
    pygame.time.delay(LEVEL_SPEED[0])
    clock.tick(LEVEL_SPEED[1])

    
    #REQUIRED FOR PYGAME
    pygame.display.flip()
    pygame.display.update()


print(SCORE)
pygame.quit()
conn.commit()