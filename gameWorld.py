import pygame
import spritesheet
from player import Player
import random
from game import *

inGame = pygame.display.set_mode([1920, 1080])
fightScene = pygame.display.set_mode([1920, 1080])

random.seed(5)
rn = random.uniform(0,1)
rn2 = random.uniform(0,1)
rn3 = random.uniform(0,1)

def createWorld():
    # Sprites
    grass = pygame.image.load('sprites/Tilesets/tiles/new/grass.png').convert_alpha()
    grassSheet = spritesheet.SpriteSheet(grass)
    bg = grassSheet.get_image(16, 16, 16, 16, 120, 67.5, (0, 0, 0))

    inGame.blit(bg, (0, 0))

    #Grass - use only for slide show errors bloopers

    GrassSprite = pygame.image.load('sprites/Tilesets/tiles/new/grasshills.png').convert_alpha()
    GrassImg = spritesheet.SpriteSheet(GrassSprite)
    GrassTexture = GrassImg.get_image(16, 16, 0, 80, 4, 4, (0, 0, 0))

def createFight():
    BG = pygame.image.load('sprites/bg/backdrop.png').convert_alpha()
    inGame.blit(BG, (0, 0))

    GrassSprite = pygame.image.load('sprites/Tilesets/tiles/new/grasshills.png').convert_alpha()
    GrassImg = spritesheet.SpriteSheet(GrassSprite)
    GrassTexture = GrassImg.get_image(48, 48, 0, 0, 4, 4, (0, 0, 0))

    inGame.blit(GrassTexture, (448, 600))
    inGame.blit(GrassTexture, (1280, 600))

    cloudModel3_4 = pygame.image.load('sprites/Characters/Cloud.png').convert_alpha()
    cloud3_4Sheet = spritesheet.SpriteSheet(cloudModel3_4)
    cloud3_4 = cloud3_4Sheet.get_image(47, 30, 0, 0, 2.8, 2.8, (0, 0, 0))

    inGame.blit(cloud3_4, (1310, 645))

    char = pygame.image.load('sprites/Characters/char.png').convert_alpha()
    charSheet = spritesheet.SpriteSheet(char)
    bunny = charSheet.get_image(48, 48, 0, 0, 4, 4, (0, 0, 0))

    inGame.blit(bunny, (448, 580))
    pygame.display.update()
