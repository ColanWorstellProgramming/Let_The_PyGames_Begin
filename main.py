#!/usr/bin/env python3
import pygame
import spritesheet
import random
import config
from game import Game
from game_state import GameState


## -------------------------------- Pygame Init Class

class PyGame:
    def __init__(self):
        self.width = config.WIDTH
        self.height = config.HEIGHT
        self.title = config.TITLE
        self.screen = pygame.display.set_mode([self.width, self.height])

    def run(self):
        pygame.init()

        pygame.display.set_caption(self.title)

        mainMenu.buildMenu(self, self.getScreen())
        pygame.display.update()

        self.gameLoop(self.getScreen())

    def gameLoop(self, screen):

        play = pygame.image.load('sprites/play.png').convert_alpha()
        playButton = spritesheet.SpriteSheet(play)
        ply = playButton.get_image(28, 18, 0, 0, 10, 10, config.BLACK)

        switch = False
        created = False

        while switch == False:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 822 <= mouse[0] <= 1082 and 780 <= mouse[1] <= 952:
                        switch = True
                        if created == False:
                            #Taylor
                            clock = pygame.time.Clock()
                            game = Game(screen)
                            game.set_up()

                            while game.game_state == GameState.RUNNING:

                                clock.tick(config.CLOCK)
                                game.update()
                                pygame.display.flip()
                                pygame.display.update()
                            created = True

            # Defines Mouse
            if switch == False:
                mouse = pygame.mouse.get_pos()

                if 822 <= mouse[0] <= 1082 and 780 <= mouse[1] <= 952:
                    pygame.draw.rect(screen,config.LIGHT,[(config.WIDTH-260)/2, 810, 260, 170])

                else:
                    pygame.draw.rect(screen,config.DARK,[(config.WIDTH-260)/2, 810, 260, 170])

                screen.blit(ply, ((config.WIDTH-280)/2, (config.HEIGHT*2.25)/3))

            pygame.display.update()

    def getScreen(self):
        return self.screen

    def setScreen(self, x):
        self.screen = x

## -------------------------------- Build Main Menu Class

class mainMenu:
    def __init__(self) -> None:
        pass

    def buildMenu(self, screen):
        # Sprite Load
        grass = pygame.image.load('sprites/Tilesets/tiles/new/grass.png').convert_alpha()
        char = pygame.image.load('sprites/Characters/char.png').convert_alpha()
        cloudModel3_4 = pygame.image.load('sprites/Characters/Cloud.png').convert_alpha()
        HillsSprite = pygame.image.load('sprites/Tilesets/tiles/new/grasshills.png').convert_alpha()
        GrassSprite = pygame.image.load('sprites/Tilesets/tiles/new/grasshills.png').convert_alpha()
        TitleSprite = pygame.image.load('sprites/title.png').convert_alpha()

        # Import
        grassSheet = spritesheet.SpriteSheet(grass)
        charSheet = spritesheet.SpriteSheet(char)
        cloud3_4Sheet = spritesheet.SpriteSheet(cloudModel3_4)
        HillsImg = spritesheet.SpriteSheet(HillsSprite)
        GrassImg = spritesheet.SpriteSheet(GrassSprite)
        TitleImg = spritesheet.SpriteSheet(TitleSprite)

        # Width of IMG, Hight of IMG, Starting Pixel X, Starting Pixel Y, Scale X, Scale Y, Background Color To Remove, Frame
        bg = grassSheet.get_image(16, 16, 16, 16, 120, 67.5, config.BLACK)
        bunny = charSheet.get_image(48, 48, 0, 0, 4, 4, config.BLACK)
        cloud3_4 = cloud3_4Sheet.get_image(47, 30, 0, 0, 3, 3, config.BLACK)
        hillsLeft = HillsImg.get_image(47/3, 47, 0, 0, 6, 6, config.BLACK)
        hillsMid = HillsImg.get_image(47/3, 47, 47/3, 0, 6, 6, config.BLACK)
        hillsRight = HillsImg.get_image(47/3, 47, ((50*2)/3), 0, 6, 6, config.BLACK)
        GrassTexture = GrassImg.get_image(16, 16, 0, 80, 4, 4, config.BLACK)
        TitleTop = TitleImg.get_image(59, 7, 23, 17, 10, 10, config.WHITE)
        TitleBottom = TitleImg.get_image(59, 7, 23, 25, 10, 10, config.WHITE)

        # Screen Background
        screen.fill(config.SCREEN_FILL)

        #Background
        screen.blit(bg, (0, 0))

        j = 1
        y = 1
        for j in range (900):
            for y in range (30):
                if j % 3 == 0 and y % 2 == 0 and random.uniform(0,1) >= 0.3:
                    screen.blit(GrassTexture, (j * (64 * random.uniform(0,1)), y * (64 * random.uniform(0,1))))
                y += 1
            j += 1

        screen.blit(bunny, (((config.WIDTH-192)/2), ((config.HEIGHT*2.25)/3)-146))
        screen.blit(hillsLeft, (-32, -84))

        # Length Hills
        screen.blit(hillsMid, (1800, -84))

        i = 0
        while i < 19:
            screen.blit(hillsMid, (94 * i, 32))
            i += 1

        screen.blit(hillsRight, (1780, 32))

        i = 0
        while i < 20:
            screen.blit(hillsMid, (94 * i, -84))
            i += 1

        screen.blit(hillsRight, (1880, -84))

        screen.blit(cloud3_4, (1700, 32))

        screen.blit(TitleTop, (32, 32))
        screen.blit(TitleBottom, (700, 32))

## -------------------------------- PyGame Class Object

app = PyGame()
app.run() ## Start App

## --------------------------------
