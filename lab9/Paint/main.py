from turtle import circle
import pygame


#INITIALIZING THE GAME
pygame.init()


#DEFINING MAIN COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


#ADDING MAIN VARIABLES FOR DRAWING MODES
ERASER = False
RECTANGLE = False
CIRCLE = False
RIGHT_TRIANGLE = False
EQUILATERAL_TRIANGLE = False
RHOMBUS = False
REGIMES = [RECTANGLE, CIRCLE, RIGHT_TRIANGLE, EQUILATERAL_TRIANGLE, RHOMBUS]


#DEFINING BACKGROUND COLOR AND AN OPERATING COLOR(RED BY DEFAULT)
BACKGROUND_COLOR = BLACK
CURRENT_COLOR = RED


#DEFINING WINDOW SETTINGS
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


#INITIALIZING MAIN OBJECTS FOR GAME
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
game_over = False


#DEFINE VARIABLES prev AND cur THAT ARE USED TO DRAW, AND FILLING SCREEN WITH BACKGROUND COLOR
prev, cur = None, None
screen.fill(BACKGROUND_COLOR)


#MAIN LOOP
while not game_over:
    for event in pygame.event.get():
        #FINISHING THE GAME
        if event.type == pygame.QUIT:
            game_over = True
        #FIXATING POSITION WHEN THE MOUSE WAS CLICKED
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
        #TRACKING MOUSE POSITION AND DRAWING
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
            if prev:
                #ERASER AND LINE DRAWING
                if ERASER:
                    pygame.draw.line(screen, BACKGROUND_COLOR, prev, cur, 20)
                    prev = cur
                elif not RECTANGLE and not CIRCLE and not RIGHT_TRIANGLE and not EQUILATERAL_TRIANGLE and not RHOMBUS:
                    pygame.draw.line(screen, CURRENT_COLOR, prev, cur, 1)
                    prev = cur
        #STOP MOUSE TRACK AND DRAW OBJECTS IF IT IS CURRENT MODE
        if event.type == pygame.MOUSEBUTTONUP:
            #DRAWING RECTANGLE
            if RECTANGLE:
                new_cur = pygame.mouse.get_pos()
                width = abs(new_cur[0] - prev[0])
                height = abs(new_cur[1] - prev[1])
                coords = [min(prev[0], new_cur[0]), min(prev[1], new_cur[1])]
                pygame.draw.rect(screen, CURRENT_COLOR, tuple(coords + [width, height]))
                prev = new_cur
            #DRAWING CIRCLE(ELLIPSE IN FACT)
            if CIRCLE:
                new_cur = pygame.mouse.get_pos()
                width = abs(new_cur[0] - prev[0])
                height = abs(new_cur[1] - prev[1])
                coords = [min(prev[0], new_cur[0]), min(prev[1], new_cur[1])]
                pygame.draw.ellipse(screen, CURRENT_COLOR, tuple(coords + [width, height]))
                prev = new_cur
            #Drawing right triangle
            if RIGHT_TRIANGLE:
                new_cur = pygame.mouse.get_pos()
                coords = [prev]
                coords.append((prev[0], new_cur[1]))
                coords.append(new_cur)
                pygame.draw.polygon(screen, CURRENT_COLOR, coords)
                prev = new_cur
            #Drawing equilateral triangle
            if EQUILATERAL_TRIANGLE:
                new_cur = pygame.mouse.get_pos()
                coords = [prev]
                coords.append((new_cur[0], prev[1]))
                coords.append(((min(new_cur[0], prev[0]) + abs(new_cur[0] - prev[0]) // 2), new_cur[1]))
                pygame.draw.polygon(screen, CURRENT_COLOR, coords)
                prev = new_cur
            #Drawing rhombus
            if RHOMBUS:
                new_cur = pygame.mouse.get_pos()
                coords = [(prev[0], (prev[1] + new_cur[1]) // 2)]
                coords.append(((prev[0] + new_cur[0]) // 2, new_cur[1]))
                coords.append((new_cur[0], (prev[1] + new_cur[1]) // 2))
                coords.append(((prev[0] + new_cur[0]) // 2, prev[1]))
                pygame.draw.polygon(screen, CURRENT_COLOR, coords)
                prev = new_cur
            #STOP MOUSE TRACK IF MODE WAS LINE OR ERASER
            else:
                prev = None
        #SWITCING MODES OF DRAWING VIA KEYBOARD
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                RECTANGLE = not RECTANGLE
                ERASER = False
                RIGHT_TRIANGLE = False
                EQUILATERAL_TRIANGLE = False
                CIRCLE = False
                RHOMBUS = False
                prev = None
            if event.key == pygame.K_2:
                CIRCLE = not CIRCLE
                ERASER = False
                RECTANGLE = False
                EQUILATERAL_TRIANGLE = False
                RIGHT_TRIANGLE = False
                RHOMBUS = False
                prev = None
            if event.key == pygame.K_3:
                ERASER = False
                RECTANGLE = False
                CIRCLE = False
                EQUILATERAL_TRIANGLE = False
                RIGHT_TRIANGLE = not RIGHT_TRIANGLE
                RHOMBUS = False
                prev = None
            if event.key == pygame.K_4:
                ERASER = False
                RECTANGLE = False
                CIRCLE = False
                RIGHT_TRIANGLE = False
                EQUILATERAL_TRIANGLE = not EQUILATERAL_TRIANGLE
                RHOMBUS = False
                prev = None
            if event.key == pygame.K_5:
                ERASER = False
                RECTANGLE = False
                CIRCLE = False
                RIGHT_TRIANGLE = False
                EQUILATERAL_TRIANGLE = False
                RHOMBUS = not RHOMBUS
                prev = None
            if event.key == pygame.K_e:
                ERASER = True
                RECTANGLE = False
                CIRCLE = False
                RIGHT_TRIANGLE = False
                EQUILATERAL_TRIANGLE = False
                RHOMBUS = False
    
    #CHANGING CURRENT COLOR VIA KEYBOARD BY FIRST LETTER OF A COLORS DEFINED
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_r]:
        CURRENT_COLOR = RED
        ERASER = False
    if pressed[pygame.K_w]:
        CURRENT_COLOR = WHITE
        ERASER = False
    if pressed[pygame.K_g]:
        CURRENT_COLOR = GREEN
        ERASER = False
    if pressed[pygame.K_b]:
        CURRENT_COLOR = BLUE
        ERASER = False

    
    #PYGAME NECESSITY
    pygame.display.flip()
    clock.tick(30)


pygame.quit()