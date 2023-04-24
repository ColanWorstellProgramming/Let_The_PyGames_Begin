#!/usr/bin/python3
import pygame
from player import Player
from game_state import GameState
import gameWorld
from passable import Passable, impassable, Path, Interactive
import random, math
import config
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.object = []
        self.game_state = GameState.NONE
        self.map = []
        self.camera = [0, 0]
        self.flip = 1
        self.flap = 0

    def set_up(self):
        print("do set up")
        player = Player(250, 540)
        self.player = player
        self.object.append(player)
        self.game_state = GameState.RUNNING

        self.load_map('maps/map1.txt')

    def update(self):

        if self.getFlap() == 0:
            player = Player(32 * config.SCALE, 32 * config.SCALE)
            player.render(self.screen, self.camera)
            self.setFlap(1)

        if self.getFlip() == 1:
            self.handle_events()
            gameWorld.createWorld()
            self.render_map(self.screen)

            for object in self.object:
                object.render(self.screen, self.camera)

        if self.getFlip() == 2:

            fade = pygame.Surface((1920, 1080))
            fade.fill((0,0,0))
            for alpha in range(0, 100):
                fade.set_alpha(alpha)
                self.screen.blit(fade, (0,0))
                pygame.display.update()

            self.setFlip(-1)

            gameWorld.createFight()

    def handle_events(self):
        movement = 60
        x=0
        y=0
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    elif event.key == pygame.K_w:
                        y -= movement
                        self.move_unit(self.player, [x, y])
                    elif event.key == pygame.K_s:
                        y += movement
                        self.move_unit(self.player, [x, y])
                    elif event.key == pygame.K_a:
                        x -= movement
                        self.move_unit(self.player, [x, y])
                    elif event.key == pygame.K_d:
                        x += movement
                        self.move_unit(self.player, [x, y])

    def load_map(self, file_name):
        with open(file_name) as map_file:
            for line in map_file:
                bytcodes = line.split()
                self.map.append(bytcodes)

    def render_map(self, screen):
        self.determine_camera()

        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos * 60 * config.SCALE - (self.camera[0] * 60 * config.SCALE), y_pos * 60 * config.SCALE - (self.camera[1] * 60 * config.SCALE), 60 * config.SCALE, 60 * config.SCALE)
                screen.blit(image, rect)
                x_pos += 1
            y_pos += 1

    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        new_X = (int(new_position[0] + 50)  * config.SCALE / (60 * config.SCALE))
        new_Y = (int(new_position[1] + 60)  * config.SCALE / (60 * config.SCALE))

        print(new_X)
        print(new_Y)

        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                if (tile in Passable and x_pos == new_X and y_pos == new_Y):
                    unit.update_position(new_position)
                    if (random.randrange(30) >= 29 and tile not in Path and tile not in Interactive):
                        #Event's ###############################################################################
                        print("Event Triggered")
                        #self.setFlip(2)
                x_pos += 1
            y_pos += 1

    def determine_camera(self):
        new_Y = (int(self.player.position[1] + (60 * config.SCALE)) / (60 * config.SCALE))

        max_y_position = 4.5
        y_position = new_Y - 2

        if y_position <= max_y_position and y_position >= 0:
            self.camera[1] = y_position * config.SCALE
        elif y_position < 0:
            self.camera[1] = 0
        elif y_position < 0:
            self.camera[1] = max_y_position

        new_X = (int(self.player.position[0] + (50 * config.SCALE)) / (60 * config.SCALE))

        max_x_position = 8
        x_position = new_X - 4

        if x_position <= max_x_position and x_position >= 0:
            self.camera[0] = x_position * config.SCALE
        elif x_position < 0:
            self.camera[0] = 0
        elif x_position < 0:
            self.camera[0] = max_x_position

    def getFlip(self):
        return self.flip

    def setFlip(self, x):
        self.flip = x

    def getFlap(self):
        return self.flap

    def setFlap(self, x):
        self.flap = x

map_tile_image = {
    # Non - Collision
    #Grass Non Interactive
    "G1" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_13.png"), (60 * config.SCALE, 60 * config.SCALE)), # Plain Grass
    "G2" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_01.png"), (60 * config.SCALE, 60 * config.SCALE)), # Top Left
    "G3" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_02.png"), (60 * config.SCALE, 60 * config.SCALE)), # Top Middle
    "G4" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_03.png"), (60 * config.SCALE, 60 * config.SCALE)), # Top Right
    "G5" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_12.png"), (60 * config.SCALE, 60 * config.SCALE)), # Left Middle
    "G6" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_14.png"), (60 * config.SCALE, 60 * config.SCALE)), # Right Middle
    "G7" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_23.png"), (60 * config.SCALE, 60 * config.SCALE)), # Bottom Left
    "G8" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_24.png"), (60 * config.SCALE, 60 * config.SCALE)), # Bottom Middle
    "G9" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_25.png"), (60 * config.SCALE, 60 * config.SCALE)), # Bottom Right
    "G0" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_56.png"), (60 * config.SCALE, 60 * config.SCALE)), # Grown Grass

    #Grass Interactive
    "g1" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_13.png"), (60 * config.SCALE, 60 * config.SCALE)), # Plain Grass
    "g2" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_01.png"), (60 * config.SCALE, 60 * config.SCALE)), # Top Left
    "g3" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_02.png"), (60 * config.SCALE, 60 * config.SCALE)), # Top Middle
    "g4" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_03.png"), (60 * config.SCALE, 60 * config.SCALE)), # Top Right
    "g5" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_12.png"), (60 * config.SCALE, 60 * config.SCALE)), # Left Middle
    "g6" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_14.png"), (60 * config.SCALE, 60 * config.SCALE)), # Right Middle
    "g7" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_23.png"), (60 * config.SCALE, 60 * config.SCALE)), # Bottom Left
    "g8" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_24.png"), (60 * config.SCALE, 60 * config.SCALE)), # Bottom Middle
    "g9" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_25.png"), (60 * config.SCALE, 60 * config.SCALE)), # Bottom Right
    "g0" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_56.png"), (60 * config.SCALE, 60 * config.SCALE)), # Grown Grass

    #Grass Corners
    "C1" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_05.png"), (60 * config.SCALE, 60 * config.SCALE)), # Top Left Corner Curve
    "C2" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_06.png"), (60 * config.SCALE, 60 * config.SCALE)), # Top Strait (Right Bottom Corner Curve)
    "C3" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_07.png"), (60 * config.SCALE, 60 * config.SCALE)), # Top Strait (Left Bottom Corner Curve)
    "C4" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_08.png"), (60 * config.SCALE, 60 * config.SCALE)), # Top Right Corner Curve
    "C5" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_16.png"), (60 * config.SCALE, 60 * config.SCALE)), # Left Strait (Right Bottom Corner Curve)
    "C6" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_17.png"), (60 * config.SCALE, 60 * config.SCALE)), # In Land (Right Bottom Corner Curve)
    "C7" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_18.png"), (60 * config.SCALE, 60 * config.SCALE)), # In Land (Left Bottom Corner Curve)
    "C8" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_19.png"), (60 * config.SCALE, 60 * config.SCALE)), # Right Strait (Right Bottom Corner Curve)
    "C9" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_27.png"), (60 * config.SCALE, 60 * config.SCALE)), # Left Strait (Right Top Corner Curve)
    "C0" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_28.png"), (60 * config.SCALE, 60 * config.SCALE)), # In Land (Right Top Corner Curve)
    "c1" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_29.png"), (60 * config.SCALE, 60 * config.SCALE)), # In Land (Left Top Corner Curve)
    "c2" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_30.png"), (60 * config.SCALE, 60 * config.SCALE)), # Right Strait (Right Top Corner Curve)
    "c3" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_38.png"), (60 * config.SCALE, 60 * config.SCALE)), # Bottom Left Corner Curve
    "c4" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_39.png"), (60 * config.SCALE, 60 * config.SCALE)), # Bottom Strait (Right Top Corner Curve)
    "c5" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_40.png"), (60 * config.SCALE, 60 * config.SCALE)), # Bottom Strait (Left Top Corner Curve)
    "c6" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_41.png"), (60 * config.SCALE, 60 * config.SCALE)), # Bottom Right Corner Curve

    #Dirt Path Non Interactive
    "P1" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_26.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Left Dirt Path
    "P2" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_27.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Middle Dirt Path
    "P3" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_28.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Right Dirt Path
    "P4" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_34.png"), (60 * config.SCALE, 60 * config.SCALE)), #Middle Left Dirt Path
    "P5" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_35.png"), (60 * config.SCALE, 60 * config.SCALE)), #Middle Middle Dirt Path
    "P6" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_36.png"), (60 * config.SCALE, 60 * config.SCALE)), #Middle Right Dirt Path
    "P7" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_42.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Left Dirt Path
    "P8" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_43.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Middle Dirt Path
    "P9" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_44.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Right Dirt Path
    "p1" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_37.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Left Corner
    "p2" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_38.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Right Corner
    "p3" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_45.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Left Corner
    "p4" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_46.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Right Corner

    #Dirt Path Interactive
    "U1" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_26.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Left Dirt Path
    "U2" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_27.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Middle Dirt Path
    "U3" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_28.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Right Dirt Path
    "U4" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_34.png"), (60 * config.SCALE, 60 * config.SCALE)), #Middle Left Dirt Path
    "U5" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_35.png"), (60 * config.SCALE, 60 * config.SCALE)), #Middle Middle Dirt Path
    "U6" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_36.png"), (60 * config.SCALE, 60 * config.SCALE)), #Middle Right Dirt Path
    "U7" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_42.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Left Dirt Path
    "U8" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_43.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Middle Dirt Path
    "U9" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_44.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Right Dirt Path
    "u1" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_37.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Left Corner
    "u2" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_38.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Right Corner
    "u3" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_45.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Left Corner
    "u4" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_46.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Right Corner

    #Pathing
    "L1" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_01.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Up To Down Path
    "L2" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_05.png"), (60 * config.SCALE, 60 * config.SCALE)), #Mid Up To Down Path
    "L3" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_09.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Up To Down Path
    "L4" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_14.png"), (60 * config.SCALE, 60 * config.SCALE)), #Left Left To Right Path
    "L5" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_15.png"), (60 * config.SCALE, 60 * config.SCALE)), #Mid Left To Right Path
    "L6" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_16.png"), (60 * config.SCALE, 60 * config.SCALE)), #Right Left To Right Path
    "L7" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_06.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom To Right Path
    "L8" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_07.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom To Left Path
    "L9" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_10.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top To Right Path
    "L0" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_11.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top To Left Path

    # Collision
    #Fences
    "F1" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_02.png"), (60 * config.SCALE, 60 * config.SCALE)), #Right Bottom Fence
    "F2" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_04.png"), (60 * config.SCALE, 60 * config.SCALE)), #Left Bottom Fence
    "F3" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_10.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Left Fence
    "F4" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_12.png"), (60 * config.SCALE, 60 * config.SCALE)), #Left Top Fence
    "F5" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_15.png"), (60 * config.SCALE, 60 * config.SCALE)), #Left Right Fence
    "F6" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_05.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Bottom Fence
    "F7" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_01.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Fence
    "F8" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_03.png"), (60 * config.SCALE, 60 * config.SCALE)), #Left Bottom Right Fence
    "F9" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_06.png"), (60 * config.SCALE, 60 * config.SCALE)), #Right Top Bottom Fence
    "F0" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_07.png"), (60 * config.SCALE, 60 * config.SCALE)), #All Fence
    "f1" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_08.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Left Bottom Fence
    "f2" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_09.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Fence
    "f3" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_11.png"), (60 * config.SCALE, 60 * config.SCALE)), #Left Right Top Fence
    "f4" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_13.png"), (60 * config.SCALE, 60 * config.SCALE)), #Single Fence
    "f5" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_14.png"), (60 * config.SCALE, 60 * config.SCALE)), #Right Fence
    "f6" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_16.png"), (60 * config.SCALE, 60 * config.SCALE)), #Left Fence

    #Thick Tree
    "T1" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_02.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Left Tree
    "T2" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_03.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Right Tree
    "T3" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_11.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Left Tree
    "T4" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_12.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Right Tree

    #Thin Tree
    "T5" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_01.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Tree
    "T6" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_10.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Tree

    #Apple Tree
    "T7" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_04.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Left Tree
    "T8" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_05.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Right Tree
    "T9" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_13.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Left Tree
    "T0" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_14.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Right Tree

    #Bushes
    "B1" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_28.png"), (60 * config.SCALE, 60 * config.SCALE)), #Berry Bush
    "B2" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_29.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bush

    #Stumps
    "B3" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_22.png"), (60 * config.SCALE, 60 * config.SCALE)), #Thin Stump
    "B4" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_23.png"), (60 * config.SCALE, 60 * config.SCALE)), #Stump

    #Flowers
    "B5" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_26.png"), (60 * config.SCALE, 60 * config.SCALE)), #Yellow
    "B6" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_35.png"), (60 * config.SCALE, 60 * config.SCALE)), #Red
    "B7" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_33.png"), (60 * config.SCALE, 60 * config.SCALE)), #Blue
    "B8" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_27.png"), (60 * config.SCALE, 60 * config.SCALE)), #Sunflower Top
    "B9" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_36.png"), (60 * config.SCALE, 60 * config.SCALE)), #Sunflower Bottom

    #Rocks
    "y1" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_42.png"), (60 * config.SCALE, 60 * config.SCALE)), #Rock
    "y2" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_43.png"), (60 * config.SCALE, 60 * config.SCALE)), #Pebble

    #Shrooms
    "S1" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_06.png"), (60 * config.SCALE, 60 * config.SCALE)), #Red Shrooms
    "S2" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_09.png"), (60 * config.SCALE, 60 * config.SCALE)), #Purple Shrooms

    #Fruit
    "S3" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_21.png"), (60 * config.SCALE, 60 * config.SCALE)), #Apple
    "S4" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_32.png"), (60 * config.SCALE, 60 * config.SCALE)), #Berry

    #House
    "H1" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_08.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Left House
    "H2" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_10.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Right House
    "H3" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_24.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Left House
    "H4" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_22.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Right House
    "H5" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_09.png"), (60 * config.SCALE, 60 * config.SCALE)), #Left To Right House
    "H6" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_15.png"), (60 * config.SCALE, 60 * config.SCALE)), #Up To Down Left House
    "H7" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_17.png"), (60 * config.SCALE, 60 * config.SCALE)), #Up To Down Right House
    "H8" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_02.png"), (60 * config.SCALE, 60 * config.SCALE)), #Window House

    #Doors
    "D1" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_04.png"), (60 * config.SCALE, 60 * config.SCALE)), #Gate Door
    #Collision On For "D2 Only"
    "D2" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_11.png"), (60 * config.SCALE, 60 * config.SCALE)), #Closed Door
    "D3" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_18.png"), (60 * config.SCALE, 60 * config.SCALE)), #Open Door
    "D4" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_25.png"), (60 * config.SCALE, 60 * config.SCALE)), #Cracked Door

    #Roof
    "R1" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_05.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Left Roof
    "R2" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_07.png"), (60 * config.SCALE, 60 * config.SCALE)), #Top Right Roof
    "R3" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_33.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Left Roof
    "R4" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_35.png"), (60 * config.SCALE, 60 * config.SCALE)), #Bottom Right Roof
    "R5" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_06.png"), (60 * config.SCALE, 60 * config.SCALE)), #Left To Right Top Roof
    "R6" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_34.png"), (60 * config.SCALE, 60 * config.SCALE)), #Left To Right Bottom Roof
    "R7" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_12.png"), (60 * config.SCALE, 60 * config.SCALE)), #Up To Down Left Top Roof
    "R8" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_19.png"), (60 * config.SCALE, 60 * config.SCALE)), #Up To Down Left Middle Roof
    "R9" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_26.png"), (60 * config.SCALE, 60 * config.SCALE)), #Up To Down Left Bottom Roof
    "R0" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_14.png"), (60 * config.SCALE, 60 * config.SCALE)), #Up To Down Right Top Roof
    "r1" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_21.png"), (60 * config.SCALE, 60 * config.SCALE)), #Up To Down Right Middle Roof
    "r2" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_28.png"), (60 * config.SCALE, 60 * config.SCALE)), #Up To Down Right Bottom Roof
    "r3" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_13.png"), (60 * config.SCALE, 60 * config.SCALE)), #Mid Top
    "r4" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_20.png"), (60 * config.SCALE, 60 * config.SCALE)), #Mid Mid
    "r5" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_27.png"), (60 * config.SCALE, 60 * config.SCALE)), #Mid Bottom

    #Water
    "W1" : pygame.transform.scale(pygame.image.load("sprites/Slices/water/Water_01.png"), (60 * config.SCALE, 60 * config.SCALE)), #Far Left Water
    "W2" : pygame.transform.scale(pygame.image.load("sprites/Slices/water/Water_02.png"), (60 * config.SCALE, 60 * config.SCALE)), #Left Water
    "W3" : pygame.transform.scale(pygame.image.load("sprites/Slices/water/Water_03.png"), (60 * config.SCALE, 60 * config.SCALE)), #Right Water
    "W4" : pygame.transform.scale(pygame.image.load("sprites/Slices/water/Water_04.png"), (60 * config.SCALE, 60 * config.SCALE)), #Far Right Water

}
