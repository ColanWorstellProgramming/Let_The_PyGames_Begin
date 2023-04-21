#!/usr/bin/python3

import pygame
import config
from game import Game
from game_state import GameState

pygame.init()
screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("CloudScape Chronicles: Nimbus and Cirrus Edition")

clock = pygame.time.Clock()
game = Game(screen)
game.set_up()

while game.game_state == GameState.RUNNING:
    clock.tick(10)
    game.update()
    pygame.display.flip()
    
