# ()
# 5
#[]


import pygame

pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sprite_sheet = pygame.image.load('player.png')

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])