import random
import pygame

def play_random_sfx(sfx_list):
    channel1 = pygame.mixer.Channel(2)
    if sfx_list:
        volume=0.05
        random_sfx = random.choice(sfx_list)
        print(f"Playing: {random_sfx}")
        pygame.mixer.music.load(random_sfx)
        channel1.play(pygame.mixer.Sound(random_sfx), 0)
        channel1.set_volume(0.05)