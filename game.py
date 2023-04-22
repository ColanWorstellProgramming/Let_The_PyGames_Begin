#!/usr/bin/python3
import pygame
import config
from player import Player
from game_state import GameState
import spritesheet
import gameWorld
from tiles import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.object = []
        self.game_state = GameState.NONE

    def set_up(self):
        print("do set up")
        player = Player(1, 1)
        self.player = player
        self.object.append(player)
        self.game_state = GameState.RUNNING

    def update(self):
        print("update")
        self.handle_events()

        # gameWorld.createWorld()

        # TileMap
        map = TileMap('sprites/tiles/Map_Tile Layer 1.csv', spritesheet)
        # Player.x_position,  Player.y_position = map.start_x, map.start_y
        map.draw_map(self.screen)

        for object in self.object:
            object.render(self.screen)

    def handle_events(self):
        movement = 0.2
        x=0
        y=0
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                keys = pygame.key.get_pressed()

                if keys[pygame.K_w]:
                    y -= movement
                    self.player.update_position(x, y)
                if keys[pygame.K_s]:
                    y += movement
                    self.player.update_position(x, y)
                if keys[pygame.K_a]:
                    x -= movement
                    self.player.update_position(x, y)
                if keys[pygame.K_d]:
                    x += movement
                    self.player.update_position(x, y)
