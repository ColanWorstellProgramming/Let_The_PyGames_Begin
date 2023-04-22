import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    # Width of IMG, Hight of IMG, Starting Pixel X, Starting Pixel Y, Scale X, Scale Y, Background Color To Remove, Frame
    def get_image(self, x, y, imgX, imgY, scaleX, scaleY, color):
        image = pygame.Surface((x, y)).convert_alpha()
        image.blit(self.sheet, (0, 0), (imgX, imgY, x, y))
        image = pygame.transform.scale(image, (x * scaleX, y * scaleY))
        image.set_colorkey(color)

        return image
