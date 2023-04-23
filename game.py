#!/usr/bin/python3
import pygame
import config
from player import Player
from game_state import GameState
import spritesheet
import gameWorld

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.object = []
        self.game_state = GameState.NONE
        self.map = []

    def set_up(self):
        print("do set up")
        player = Player(1, 1)
        self.player = player
        self.object.append(player)
        self.game_state = GameState.RUNNING

        self.load_map('maps/map1.txt')

    def update(self):
        print("update")
        self.handle_events()

        self.render_map(self.screen)

        # gameWorld.createWorld()

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

    def load_map(self, file_name):
        with open(file_name) as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map.append(tiles)

    def render_map(self, screen):
        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos * 60, y_pos * 60, 60, 60)
                screen.blit(image, rect)
                x_pos += 1
            y_pos += 1

map_tile_image = {
    # Non - Collision
    "G" : pygame.transform.scale(pygame.image.load("sprites/Slices/images/grassHills/grasshills_13.png"), (60, 60)), # Plain Grass

    # Collision
    "D" : pygame.transform.scale(pygame.image.load("sprites/Slices/images/fence/fences_15.png"), (60, 60)), #Left To Right Fence
    "Z" : pygame.transform.scale(pygame.image.load("sprites/Slices/images/fence/fences_02.png"), (60, 60)), #Top Left Fence
    "W" : pygame.transform.scale(pygame.image.load("sprites/Slices/images/fence/fences_04.png"), (60, 60)), #Top Right Fence
    "X" : pygame.transform.scale(pygame.image.load("sprites/Slices/images/fence/fences_12.png"), (60, 60)), #Bottom Right Fence
    "Y" : pygame.transform.scale(pygame.image.load("sprites/Slices/images/fence/fences_10.png"), (60, 60)), #Bottom Left Fence
    "V" : pygame.transform.scale(pygame.image.load("sprites/Slices/images/fence/fences_05.png"), (60, 60)), #Up To Down Fence
}