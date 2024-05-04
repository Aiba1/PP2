import pygame
import random
import os

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()



pl = r"C:\Users\Aibar\Desktop\pp2\musics\Past Lives.mp3"
oa = r"C:\Users\Aibar\Desktop\pp2\musics\OAO.mp3"
pe = r"C:\Users\Aibar\Desktop\pp2\musics\Perfect.mp3"
ru = r"C:\Users\Aibar\Desktop\pp2\musics\Runaway.mp3"
cd = r"C:\Users\Aibar\Desktop\pp2\musics\CD.mp3"


# PICTURES-------------------------------------------------
pimg = pygame.image.load(r"C:\Users\Aibar\Desktop\pp2\pictures\sheeran.jpg")
plimg = pygame.image.load(r"C:\Users\Aibar\Desktop\pp2\pictures\photo_5242467503207208518_m.jpg")
oaoimg = pygame.image.load(r"C:\Users\Aibar\Desktop\pp2\pictures\adele.jpg")
cdimg = pygame.image.load(r"C:\Users\Aibar\Desktop\pp2\pictures\california.jpg")
rimg = pygame.image.load(r"C:\Users\Aibar\Desktop\pp2\pictures\sia.jpg")

# SCREEN
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Player")

# EVENTS-------------------------------------------------
song_end = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(song_end)

# -------------------------------------------------
songs = [pl, oa, pe, ru, cd]
pictures = [plimg, oaoimg, pimg, rimg, cdimg]

# Define song names corresponding to the pictures
song_names = ["Past Lives", "OAO", "Perfect", "Runaway", "CD"]

def random_song():
    global songs
    return random.choice(songs)

def index(cs):
    return songs.index(cs)

cs = random_song()
previous_song = cs
pause = True

my_font = pygame.font.SysFont('Comic Sans MS', 30)

# firstsong-------------------------------------------
pygame.mixer.music.load(cs)
pygame.mixer.music.play()

# LOOP-------------------------------------------------
done = False
while not done:
    # Clear the screen
    screen.fill((0, 0, 0))
    
    screen.blit(pictures[index(cs)], (140, 200))
    
    # Render text above the picture
    text_surface = my_font.render(song_names[index(cs)], True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(250, 150))
    screen.blit(text_surface, text_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == song_end:
            previous_song = cs
            cs = random_song()
            pygame.mixer.music.load(cs)
            pygame.mixer.music.play()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pause:
                    pygame.mixer.music.pause()
                    pause = False
                else:
                    pygame.mixer.music.unpause()
                    pause = True
            elif event.key == pygame.K_RIGHT:
                previous_song = cs
                cs = random_song()
                pygame.mixer.music.load(cs)
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                cs = previous_song
                pygame.mixer.music.load(cs)
                pygame.mixer.music.play()
                
    pygame.display.flip()
    
    clock.tick(60)
                
pygame.quit()