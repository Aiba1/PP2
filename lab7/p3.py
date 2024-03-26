import pygame
import random
import os

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

# SONGS-------------------------------------------------
path = "/Users/aiymtursynbekova/Desktop/pp2/musics"
path1 = "/Users/aiymtursynbekova/Desktop/pp2/pictures"
pygame.mixer.music.load(os.path.join(path, "Past Lives.mp3"))
pygame.mixer.music.load(os.path.join(path, "OAO.mp3"))
pygame.mixer.music.load(os.path.join(path, "Perfect.mp3"))
pygame.mixer.music.load(os.path.join(path, "Runaway.mp3"))
pygame.mixer.music.load(os.path.join(path, "CD.mp3"))

# PICTURES-------------------------------------------------
pimg = pygame.image.load((os.path.join(path1, "p.jpeg")))
plimg = pygame.image.load((os.path.join(path1, "pl.jpeg")))
oaoimg = pygame.image.load((os.path.join(path1, "oao.jpeg")))
cdimg = pygame.image.load((os.path.join(path1, "cd.png")))
rimg = pygame.image.load((os.path.join(path1, "r.jpeg")))

# SCREEN
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Player")

# EVENTS-------------------------------------------------
song_end = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(song_end)

# -------------------------------------------------
songs = ["Past Lives.mp3", "OAO.mp3", "Perfect.mp3", "Runaway.mp3", "CD.mp3"]
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
pygame.mixer.music.load(os.path.join(path, cs))
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
            pygame.mixer.music.load(os.path.join(path, cs))
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
                pygame.mixer.music.load(os.path.join(path, cs))
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                cs = previous_song
                pygame.mixer.music.load(os.path.join(path, cs))
                pygame.mixer.music.play()
                
    pygame.display.flip()
    
    clock.tick(60)
                
pygame.quit()