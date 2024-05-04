import pygame
from random import randint
import sys
import psycopg2
from config import host, user, password, db_name


conn = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = db_name
)
conn.autocommit = True

cursor = conn.cursor()
def createtable():
    sql = '''
        CREATE TABLE IF NOT EXISTS Snake(
        name CHAR(20),
        point INT
    )
    '''
    cursor.execute(sql)
createtable()
def auth(player):
    cursor.execute("SELECT name FROM Snake WHERE name = %s",(player,))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO Snake(name,point) values (%s, 0)", (player,))
    conn.commit()
player = input("your name: ")
auth(player)
cursor.execute("SELECT point FROM Snake WHERE name = %s", (player,))

pygame.init()

heigh = 600
width = 600

#screen
screen = pygame.display.set_mode((width,heigh))
pygame.display.set_caption("Snake Game")

#variables
score = 0
cell = 30
speed = 3
goal = 5
level = 1

#font
font = pygame.font.SysFont("verdana", 20)

heigh_cell = heigh // cell
width_cell = width // cell

#color palette
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)

#snake
snake = [(width_cell // 2, heigh_cell // 2)]
snake_dir = (0, 1)

#food
food = (randint(0, width_cell-1), randint(0, heigh_cell-1))

#background
def chess_grid():

    colors = [WHITE, GRAY]
    for i in range(width // cell):
        for j in range(heigh // cell):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * cell, j * cell, cell, cell))



clock = pygame.time.Clock()

done = False
game_over = False

#game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and snake_dir != (-1, 0):
        snake_dir = (1, 0)
    if keys[pygame.K_LEFT] and snake_dir != (1, 0):
        snake_dir = (-1, 0)
    if keys[pygame.K_UP] and snake_dir != (0, 1):
        snake_dir = (0, -1)
    if keys[pygame.K_DOWN] and snake_dir != (0,-1):
        snake_dir = (0, 1) 

    #adding the size
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)
    chess_grid()
    
    #screen info
    progress = font.render("Score: " + str(score), True, BLACK)
    screen.blit(progress,(10,10))
    lvl = font.render("Level: " + str(level), True, BLACK)
    screen.blit(lvl,(10, 30))
    
    #food collision
    if snake[0] == food:
        food = (randint(0, width_cell - 1), randint(0, heigh_cell - 1))
        score += 1
    else:
        snake.pop()

    #levelling up
    if score == goal:
        goal += 5
        speed += 2
        level += 1

    #border collision check
    if snake[0][0] < 0 or snake[0][0] > width_cell - 1 or snake[0][1] < 0 or snake[0][1] > heigh_cell - 1:
        done = True
    
    #self collision
    if len(snake) != len(set(snake)):
        done = True

    #drawing the snake
    pygame.draw.rect(screen, BLACK, (snake[0][0] * cell, snake[0][1] * cell, cell, cell))
    for segment in snake[1:]:
        pygame.draw.rect(screen, RED, (segment[0] * cell, segment[1] * cell, cell, cell))

    #drawing the snake
    pygame.draw.rect(screen, RED, (food[0] * cell, food[1] * cell, cell, cell))

    pygame.display.flip()
    clock.tick(speed)

    cursor.execute("SELECT point FROM Snake WHERE name = %s", (player,))
    if score > int(cursor.fetchone()[0]):
        cursor.execute("UPDATE Snake SET point = %s WHERE name = %s",(score,player))
        

    
    