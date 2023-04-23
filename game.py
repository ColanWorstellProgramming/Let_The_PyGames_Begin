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
        player = Player(25, 52)
        self.player = player
        self.object.append(player)
        self.game_state = GameState.RUNNING

        self.load_map('maps/map1.txt')

    def update(self):
        print("update")
        self.handle_events()

        gameWorld.createWorld()
        self.render_map(self.screen)

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
                bytcodes = line.split()
                self.map.append(bytcodes)

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
    #Grass
    "G1" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_13.png"), (60, 60)), # Plain Grass
    "G2" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_01.png"), (60, 60)), # Top Left
    "G3" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_02.png"), (60, 60)), # Top Middle
    "G4" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_03.png"), (60, 60)), # Top Right
    "G5" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_12.png"), (60, 60)), # Left Middle
    "G6" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_14.png"), (60, 60)), # Right Middle
    "G7" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_23.png"), (60, 60)), # Bottom Left
    "G8" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_24.png"), (60, 60)), # Bottom Middle
    "G9" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_25.png"), (60, 60)), # Bottom Right
    "G0" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_56.png"), (60, 60)), # Grown Grass

    #Grass Corners
    "C1" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_05.png"), (60, 60)), # Top Left Corner Curve
    "C2" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_06.png"), (60, 60)), # Top Strait (Right Bottom Corner Curve)
    "C3" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_07.png"), (60, 60)), # Top Strait (Left Bottom Corner Curve)
    "C4" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_08.png"), (60, 60)), # Top Right Corner Curve
    "C5" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_16.png"), (60, 60)), # Left Strait (Right Bottom Corner Curve)
    "C6" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_17.png"), (60, 60)), # In Land (Right Bottom Corner Curve)
    "C7" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_18.png"), (60, 60)), # In Land (Left Bottom Corner Curve)
    "C8" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_19.png"), (60, 60)), # Right Strait (Right Bottom Corner Curve)
    "C9" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_27.png"), (60, 60)), # Left Strait (Right Top Corner Curve)
    "C0" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_28.png"), (60, 60)), # In Land (Right Top Corner Curve)
    "c1" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_29.png"), (60, 60)), # In Land (Left Top Corner Curve)
    "c2" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_30.png"), (60, 60)), # Right Strait (Right Top Corner Curve)
    "c3" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_38.png"), (60, 60)), # Bottom Left Corner Curve
    "c4" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_39.png"), (60, 60)), # Bottom Strait (Right Top Corner Curve)
    "c5" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_40.png"), (60, 60)), # Bottom Strait (Left Top Corner Curve)
    "c6" : pygame.transform.scale(pygame.image.load("sprites/Slices/grassHills/grasshills_41.png"), (60, 60)), # Bottom Right Corner Curve

    #Dirt Path
    "P1" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_26.png"), (60, 60)), #Top Left Dirt Path
    "P2" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_27.png"), (60, 60)), #Top Middle Dirt Path
    "P3" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_28.png"), (60, 60)), #Top Right Dirt Path
    "P4" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_34.png"), (60, 60)), #Middle Left Dirt Path
    "P5" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_35.png"), (60, 60)), #Middle Middle Dirt Path
    "P6" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_36.png"), (60, 60)), #Middle Right Dirt Path
    "P7" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_42.png"), (60, 60)), #Bottom Left Dirt Path
    "P8" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_43.png"), (60, 60)), #Bottom Middle Dirt Path
    "P9" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_44.png"), (60, 60)), #Bottom Right Dirt Path
    "p1" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_37.png"), (60, 60)), #Top Left Corner
    "p2" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_38.png"), (60, 60)), #Top Right Corner
    "p3" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_45.png"), (60, 60)), #Bottom Left Corner
    "p4" : pygame.transform.scale(pygame.image.load("sprites/Slices/dirt/dirt_46.png"), (60, 60)), #Bottom Right Corner

    #Pathing
    "L1" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_01.png"), (60, 60)), #Top Up To Down Path
    "L2" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_05.png"), (60, 60)), #Mid Up To Down Path
    "L3" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_09.png"), (60, 60)), #Bottom Up To Down Path
    "L4" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_14.png"), (60, 60)), #Left Left To Right Path
    "L5" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_15.png"), (60, 60)), #Mid Left To Right Path
    "L6" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_16.png"), (60, 60)), #Right Left To Right Path
    "L7" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_06.png"), (60, 60)), #Bottom To Right Path
    "L8" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_07.png"), (60, 60)), #Bottom To Left Path
    "L9" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_10.png"), (60, 60)), #Top To Right Path
    "L0" : pygame.transform.scale(pygame.image.load("sprites/Slices/path/Paths_11.png"), (60, 60)), #Top To Left Path

    # Collision
    #Fences
    "F1" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_02.png"), (60, 60)), #Right Bottom Fence
    "F2" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_04.png"), (60, 60)), #Left Bottom Fence
    "F3" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_10.png"), (60, 60)), #Top Left Fence
    "F4" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_12.png"), (60, 60)), #Left Top Fence
    "F5" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_15.png"), (60, 60)), #Left Right Fence
    "F6" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_05.png"), (60, 60)), #Top Bottom Fence
    "F7" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_01.png"), (60, 60)), #Bottom Fence
    "F8" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_03.png"), (60, 60)), #Left Bottom Right Fence
    "F9" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_06.png"), (60, 60)), #Right Top Bottom Fence
    "F0" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_07.png"), (60, 60)), #All Fence
    "f1" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_08.png"), (60, 60)), #Top Left Bottom Fence
    "f2" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_09.png"), (60, 60)), #Top Fence
    "f3" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_11.png"), (60, 60)), #Left Right Top Fence
    "f4" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_13.png"), (60, 60)), #Single Fence
    "f5" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_14.png"), (60, 60)), #Right Fence
    "f6" : pygame.transform.scale(pygame.image.load("sprites/Slices/fence/fences_16.png"), (60, 60)), #Left Fence

    #Thick Tree
    "T1" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_02.png"), (60, 60)), #Top Left Tree
    "T2" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_03.png"), (60, 60)), #Top Right Tree
    "T3" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_11.png"), (60, 60)), #Bottom Left Tree
    "T4" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_12.png"), (60, 60)), #Bottom Right Tree

    #Thin Tree
    "T5" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_01.png"), (60, 60)), #Top Tree
    "T6" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_10.png"), (60, 60)), #Bottom Tree

    #Apple Tree
    "T7" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_04.png"), (60, 60)), #Top Left Tree
    "T8" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_05.png"), (60, 60)), #Top Right Tree
    "T9" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_13.png"), (60, 60)), #Bottom Left Tree
    "T0" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_14.png"), (60, 60)), #Bottom Right Tree

    #Bushes
    "B1" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_28.png"), (60, 60)), #Berry Bush
    "B2" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_29.png"), (60, 60)), #Bush

    #Stumps
    "B3" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_22.png"), (60, 60)), #Thin Stump
    "B4" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_23.png"), (60, 60)), #Stump

    #Flowers
    "B5" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_26.png"), (60, 60)), #Yellow
    "B6" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_35.png"), (60, 60)), #Red
    "B7" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_33.png"), (60, 60)), #Blue
    "B8" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_27.png"), (60, 60)), #Sunflower Top
    "B9" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_36.png"), (60, 60)), #Sunflower Bottom

    #Rocks
    "y1" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_42.png"), (60, 60)), #Rock
    "y2" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_43.png"), (60, 60)), #Pebble

    #Shrooms
    "S1" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_06.png"), (60, 60)), #Red Shrooms
    "S2" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_09.png"), (60, 60)), #Purple Shrooms

    #Fruit
    "S3" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_21.png"), (60, 60)), #Apple
    "S4" : pygame.transform.scale(pygame.image.load("sprites/Slices/trees/trees_32.png"), (60, 60)), #Berry

    #House
    "H1" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_08.png"), (60, 60)), #Top Left House
    "H2" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_10.png"), (60, 60)), #Top Right House
    "H3" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_24.png"), (60, 60)), #Bottom Left House
    "H4" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_22.png"), (60, 60)), #Bottom Right House
    "H5" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_09.png"), (60, 60)), #Left To Right House
    "H6" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_15.png"), (60, 60)), #Up To Down Left House
    "H7" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_17.png"), (60, 60)), #Up To Down Right House
    "H8" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_02.png"), (60, 60)), #Window House

    #Doors
    "D1" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_04.png"), (60, 60)), #Gate Door
    #Collision On For "D2 Only"
    "D2" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_11.png"), (60, 60)), #Closed Door
    "D3" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_18.png"), (60, 60)), #Open Door
    "D4" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_25.png"), (60, 60)), #Cracked Door

    #Roof
    "R1" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_05.png"), (60, 60)), #Top Left Roof
    "R2" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_07.png"), (60, 60)), #Top Right Roof
    "R3" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_33.png"), (60, 60)), #Bottom Left Roof
    "R4" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_35.png"), (60, 60)), #Bottom Right Roof
    "R5" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_06.png"), (60, 60)), #Left To Right Top Roof
    "R6" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_34.png"), (60, 60)), #Left To Right Bottom Roof
    "R7" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_12.png"), (60, 60)), #Up To Down Left Top Roof
    "R8" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_19.png"), (60, 60)), #Up To Down Left Middle Roof
    "R9" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_26.png"), (60, 60)), #Up To Down Left Bottom Roof
    "R0" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_14.png"), (60, 60)), #Up To Down Right Top Roof
    "r1" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_21.png"), (60, 60)), #Up To Down Right Middle Roof
    "r2" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_28.png"), (60, 60)), #Up To Down Right Bottom Roof
    "r3" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_13.png"), (60, 60)), #Mid Top
    "r4" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_20.png"), (60, 60)), #Mid Mid
    "r5" : pygame.transform.scale(pygame.image.load("sprites/Slices/house/house_27.png"), (60, 60)), #Mid Bottom

    #Water
    "W1" : pygame.transform.scale(pygame.image.load("sprites/Slices/water/Water_01.png"), (60, 60)), #Far Left Water
    "W2" : pygame.transform.scale(pygame.image.load("sprites/Slices/water/Water_02.png"), (60, 60)), #Left Water
    "W3" : pygame.transform.scale(pygame.image.load("sprites/Slices/water/Water_03.png"), (60, 60)), #Right Water
    "W4" : pygame.transform.scale(pygame.image.load("sprites/Slices/water/Water_04.png"), (60, 60)), #Far Right Water

}
