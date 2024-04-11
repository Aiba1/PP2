import pygame
import datetime

pygame.init()
clock = pygame.time.Clock()

img_bg = pygame.image.load(r"C:\Users\Aibar\Desktop\pp2\practice\lab7\Image.jpg")

screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Mickey clock")

img_min = pygame.image.load(r"C:\Users\Aibar\Desktop\pp2\practice\lab7\nshan.png").convert_alpha()
img_sec = pygame.image.load(r"C:\Users\Aibar\Desktop\pp2\practice\lab7\nshan2.png").convert_alpha()
    
img_min = pygame.transform.scale(img_min, (50, 600))
img_sec = pygame.transform.scale(img_sec, (50, 600))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.blit(img_bg, (0,0))
    
    t = datetime.datetime.now()
    mnang = t.minute * 6
    scang = t.second * 6
    
    mnarr = pygame.transform.rotate(img_min, -mnang)
    scarr = pygame.transform.rotate(img_sec, -scang)
    
    screen.blit(mnarr, (400 - int(mnarr.get_width() / 2), 450 - int(mnarr.get_height() / 2)))
    screen.blit(scarr, (380  - int(scarr.get_width() / 2), 300 - int(scarr.get_height() / 2)))
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()