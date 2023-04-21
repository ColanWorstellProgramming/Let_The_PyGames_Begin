import pygame
import spritesheet

def createWorld():
    # Sprites
    grass = pygame.image.load('sprites/Tilesets/tiles/new/grass.png').convert_alpha()
    grassSheet = spritesheet.SpriteSheet(grass)
    bg = grassSheet.get_image(16, 16, 16, 16, 120, 67.5, (0, 0, 0))

    inGame = pygame.display.set_mode([1920, 1080])
    inGame.blit(bg, (0, 0))

    pygame.display.update()
