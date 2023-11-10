# ()
# 5
#[ ]


import pygame

pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sprite_sheet_idle = pygame.image.load('asset\\red hood\\idle sheet-Sheet.png')
        self.image = self.get_image(0,0)
        self.rect = self.image.get_rect()

    def get_image(self, x, y):
        image = pygame.Surface([80, 32])
        image.blit(self.sprite_sheet_idle,(0, 0), (x, y, 80, 32))
        
        return image