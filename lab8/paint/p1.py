import pygame

pygame.init()

heigh = 800
width = 800

#color palette
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)
prevX = 0
prevY = 0
currX = 0
currY = 0
done = False
LMB = False


def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

screen = pygame.display.set_mode((width,heigh))
base_layer = pygame.Surface((width, heigh))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMB = True
            prevX = event.pos[0]
            prevY = event.pos[1]
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
            currX = event.pos[0]
            currY = event.pos[1]
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMB = False
            pygame.draw.rect(screen,RED,calculate_rect(prevX, prevY, currX, currY), 2)
            base_layer.blit(screen,(0, 0))
    if LMB:
        screen.blit(base_layer, (0, 0))
        pygame.draw.rect(screen, RED,calculate_rect(prevX, prevY, currX, currY), 2)
    pygame.display.flip()