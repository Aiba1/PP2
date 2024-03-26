import pygame

pygame.init()
clock = pygame.time.Clock()

# SCREEN--------------------------------------------
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("hanging around")

# OTHERS----------------------------------------------
blue = (0, 0, 255)
x = 500
y = 400

# LOOP-----------------------------------------------
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 25:
        x -= 20
    elif keys[pygame.K_RIGHT] and x < 975:  
        x += 20
    elif keys[pygame.K_UP] and y > 25:
        y -= 20
    elif keys[pygame.K_DOWN] and y < 775:  
        y += 20

    screen.fill((0, 0, 0)) 
    pygame.draw.circle(screen, blue, (x, y), 25)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()