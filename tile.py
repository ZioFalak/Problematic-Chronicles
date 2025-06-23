import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, image):
        super().__init__(groups)
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)