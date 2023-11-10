# ()
# 5
#[ ]


import pygame

pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sprite_sheet_idle = pygame.image.load('asset\\red hood\\idle sheet-Sheet.png')

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit