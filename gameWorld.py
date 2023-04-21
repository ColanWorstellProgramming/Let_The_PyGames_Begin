import pygame
import spritesheet
from player import Player
import random

inGame = pygame.display.set_mode([1920, 1080])

random.seed(5)
rn = random.uniform(0,1)
rn2 = random.uniform(0,1)
rn3 = random.uniform(0,1)

def createPlayer():
    player = Player(48, 48)
    player.render(inGame)

def createWorld():
    # Sprites
    grass = pygame.image.load('sprites/Tilesets/tiles/new/grass.png').convert_alpha()
    grassSheet = spritesheet.SpriteSheet(grass)
    bg = grassSheet.get_image(16, 16, 16, 16, 120, 67.5, (0, 0, 0))

    inGame.blit(bg, (0, 0))

    #Grass

    GrassSprite = pygame.image.load('sprites/Tilesets/tiles/new/grasshills.png').convert_alpha()
    GrassImg = spritesheet.SpriteSheet(GrassSprite)
    GrassTexture = GrassImg.get_image(16, 16, 0, 80, 4, 4, (0, 0, 0))

    j = 1
    y = 1
    for j in range (70):
        for y in range (30):
            if j % 3 == 0 and y % 2 == 0 and rn >= 0.3:
                inGame.blit(GrassTexture, (j * (64 * rn2), y * (64 * rn3)))
            y += 1
        j += 1
