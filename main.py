#!/usr/bin/env python3
import pygame
import spritesheet
import random
import gameWorld
import config
from game import Game
from game_state import GameState

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1920, 1080])

pygame.display.set_caption('CloudScape Chronicles: Nimbus and Cirrus Edition')

# Sprite Load
grass = pygame.image.load('sprites/Tilesets/tiles/new/grass.png').convert_alpha()
play = pygame.image.load('sprites/play.png').convert_alpha()
char = pygame.image.load('sprites/Characters/char.png').convert_alpha()
cloudModel3_4 = pygame.image.load('sprites/PNG/Clouds_white/Shape3/cloud4.png').convert_alpha()
HillsSprite = pygame.image.load('sprites/Tilesets/tiles/new/grasshills.png').convert_alpha()
GrassSprite = pygame.image.load('sprites/Tilesets/tiles/new/grasshills.png').convert_alpha()
TitleSprite = pygame.image.load('sprites/title.png').convert_alpha()

# Import
grassSheet = spritesheet.SpriteSheet(grass)
charSheet = spritesheet.SpriteSheet(char)
cloud3_4Sheet = spritesheet.SpriteSheet(cloudModel3_4)
playButton = spritesheet.SpriteSheet(play)
HillsImg = spritesheet.SpriteSheet(HillsSprite)
GrassImg = spritesheet.SpriteSheet(GrassSprite)
TitleImg = spritesheet.SpriteSheet(TitleSprite)

# Colors
Black = (0, 0, 0)
White = (255, 255, 255)
Light_Button = (170,170,170)
Dark_Button = (100,100,100)

# Window Width
width = screen.get_width()

# Window Hight
height = screen.get_height()

# Width of IMG, Hight of IMG, Starting Pixel X, Starting Pixel Y, Scale X, Scale Y, Background Color To Remove, Frame
bg = grassSheet.get_image(16, 16, 16, 16, 120, 67.5, Black)
bunny = charSheet.get_image(48, 48, 0, 0, 4, 4, Black)
cloud3_4 = cloud3_4Sheet.get_image(72, 51, 0, 0, 2, 2, Black)
ply = playButton.get_image(28, 18, 0, 0, 10, 10, Black)
hills = HillsImg.get_image(47, 47, 0, 0, 6, 6, Black)
hillsLeft = HillsImg.get_image(47/3, 47, 0, 0, 6, 6, Black)
hillsMid = HillsImg.get_image(47/3, 47, 47/3, 0, 6, 6, Black)
hillsRight = HillsImg.get_image(47/3, 47, ((50*2)/3), 0, 6, 6, Black)
GrassTexture = GrassImg.get_image(16, 16, 0, 80, 4, 4, Black)
TitleTop = TitleImg.get_image(59, 7, 23, 17, 10, 10, White)
TitleBottom = TitleImg.get_image(59, 7, 23, 25, 10, 10, White)

# Screen Background
screen.fill((240, 226, 187))

#Sprites

#Background
screen.blit(bg, (0, 0))

#Grass
j = 1
y = 1
for j in range (900):
    for y in range (30):
        if j % 3 == 0 and y % 2 == 0 and random.uniform(0,1) >= 0.3:
            screen.blit(GrassTexture, (j * (64 * random.uniform(0,1)), y * (64 * random.uniform(0,1))))
        y += 1
    j += 1

screen.blit(bunny, (((width-192)/2), ((height*2.25)/3)-146))
screen.blit(hillsLeft, (-32, -84))

# Length Hills
screen.blit(hillsMid, (1800, -84))

i = 0
while i < 19:
    screen.blit(hillsMid, (94 * i, 32))
    i += 1

screen.blit(hillsRight, (1780, 32))

i = 0
x = 1
while i < 20:
    screen.blit(hillsMid, (94 * i, -84))
    i += 1

screen.blit(hillsRight, (1880, -84))

screen.blit(cloud3_4, (((width-140)/2), ((height*2.25)/3)-246))

screen.blit(TitleTop, (32, 32))
screen.blit(TitleBottom, (700, 32))

#Update Display
pygame.display.update()

switch = False
created = False

while switch == False:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 810 <= mouse[0] <= 1100 and 780 <= mouse[1] <= 970:
                switch = True
                if created == False:
                    gameWorld.createWorld()
                    created = True

    # Defines Mouse
    if switch == False:
        mouse = pygame.mouse.get_pos()

        if 810 <= mouse[0] <= 1100 and 780 <= mouse[1] <= 970:
            pygame.draw.rect(screen,Light_Button,[(width-260)/2, 810, 260, 170])

        else:
            pygame.draw.rect(screen,Dark_Button,[(width-260)/2, 810, 260, 170])

        screen.blit(ply, ((width-280)/2, (height*2.25)/3))

    pygame.display.update()


#Taylor
clock = pygame.time.Clock()
game = Game(screen)
game.set_up()

while game.game_state == GameState.RUNNING:

    clock.tick(60)
    game.update()
    pygame.display.flip()
    pygame.display.update()

pygame.quit()
