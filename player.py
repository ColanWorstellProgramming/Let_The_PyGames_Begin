#!/usr/bin/python3

import pygame
import config
import spritesheet

class Player:
    def __init__(self, x_position, y_position):
        print('player created')
        self.position = [x_position, y_position]
        self.image = pygame.image.load('sprites/Characters/bunny.png')
        self.image = pygame.transform.scale(self.image, (160, 160))
        self.image.set_colorkey((255, 255, 255))
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)

    def update(self):
        print("player updated")

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def update_position(self, x_change, y_change):
        self.position[0] += x_change
        self.position[1] += y_change
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)
