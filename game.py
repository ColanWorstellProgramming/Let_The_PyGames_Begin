#!/usr/bin/python3
import pygame
import config
from player import Player
from game_state import GameState

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
        self.screen.fill(config.BLACK)
        print("update")
        self.handle_events()
        
        for object in self.object:
            object.render(self.screen)
    
    def handle_events(self):
        x=0
        y=0
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                keys = pygame.key.get_pressed()

                if keys[pygame.K_w]:
                    y -= 1
                    self.player.update_position(x, y)
                if keys[pygame.K_s]:
                    y += 1
                    self.player.update_position(x, y)
                if keys[pygame.K_a]:
                    x -= 1
                    self.player.update_position(x, y)
                if keys[pygame.K_d]:
                    x += 1
                    self.player.update_position(x, y)
