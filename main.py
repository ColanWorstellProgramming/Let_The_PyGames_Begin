#!/usr/bin/env python3
import pygame
import spritesheet

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1920, 1080])
pygame.display.set_caption('CloudScape Chronicles: Nimbus and Cirrus Edition')

# Sprite Load
grass = pygame.image.load('sprites/Tilesets/tiles/new/grass.png').convert_alpha()
char = pygame.image.load('sprites/Characters/char.png').convert_alpha()
cloudModel3_4 = pygame.image.load('sprites/PNG/Clouds_white/Shape3/cloud4.png').convert_alpha()
cloudModel4_1 = pygame.image.load('sprites/PNG/Clouds_white/Shape4/cloud1.png').convert_alpha()

# Import
grassSheet = spritesheet.SpriteSheet(grass)
charSheet = spritesheet.SpriteSheet(char)
cloud3_4Sheet = spritesheet.SpriteSheet(cloudModel3_4)
cloud4_1Sheet = spritesheet.SpriteSheet(cloudModel4_1)

# Colors
Black = (0, 0, 0)
White = (255, 255, 255)
Light_Button = (170,170,170)
Dark_Button = (100,100,100)

# Window Width
width = screen.get_width()

# Window Hight
height = screen.get_height()

# Font
smallfont = pygame.font.Font('freesansbold.ttf', 35)

# Button Text
text = smallfont.render('Start' , True , White)

# Width of IMG, Hight of IMG, Starting Pixel X, Starting Pixel Y, Scale X, Scale Y, Background Color To Remove, Frame
bg = grassSheet.get_image(16, 16, 16, 16, 120, 67.5, Black)
bunny = charSheet.get_image(48, 48, 0, 0, 4, 4, Black)
cloud3_4 = cloud3_4Sheet.get_image(72, 51, 0, 0, 2, 2, Black)
cloud4_1 = cloud4_1Sheet.get_image(225, 137, 0, 0, 2, 2, Black)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Checks if mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:

            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()

    # Screen Background
    screen.fill((240, 226, 187))

    #Sprites

    # Image, Location On Screen
    screen.blit(bg, (0, 0))
    screen.blit(cloud3_4, (256, 512))
    screen.blit(cloud4_1, (64, -32))
    screen.blit(bunny, (1024, 64))

    # Defines Mouse
    mouse = pygame.mouse.get_pos()

    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen,Light_Button,[width/2,height/2,140,40])

    else:
        pygame.draw.rect(screen,Dark_Button,[width/2,height/2,140,40])


    # Start Button
    screen.blit(text , (width/2+50,height/2))

    #Update Display
    pygame.display.update()

pygame.quit()