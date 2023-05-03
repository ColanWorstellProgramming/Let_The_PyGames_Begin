#!/usr/bin/python3

import pygame
import config
import spritesheet

class Player:
    def __init__(self, x_position, y_position):
        print('player created')
        self.position = [x_position, y_position]
        self.image = pygame.image.load('sprites/Characters/bunny.png')
        self.image = pygame.transform.scale(self.image, (160 * config.SCALE, 160 * config.SCALE))
        self.image.set_colorkey((255, 255, 255))
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)

    def update(self):
        print("player updated")

    def update_position(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]

    def render(self, screen, camera):
        self.rect = pygame.Rect(self.position[0] * config.SCALE - (camera[0] * 60 * config.SCALE), self.position[1] * config.SCALE - (camera[1] * 60 * config.SCALE), config.SCALE, config.SCALE)
        screen.blit(self.image, self.rect)
