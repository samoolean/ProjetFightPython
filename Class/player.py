# ()
# 5
#[ ]

import pygame

pygame.init()

class Player(pygame.sprite.Sprite):

    """

    def __init__(self):
        super().__init__()
        self.sprite_sheet_idle = pygame.image.load('asset\\red hood\\idle sheet-Sheet.png')
        self.image = self.get_image(0,0)
        self.rect = self.image.get_rect()

    def get_image(self, x, y):
        image = pygame.Surface([80, 32])
        image.blit(self.sprite_sheet_idle,(0, 0), (x, y, 80, 32))
        
        return image

    """
    # new layer

    """

        self.posx += x
        self.posy += y

        self.largeurW += 1
        self.hauteurW += 1

    """

    def __init__(self, color, x, y):

        self.color = color
        self.posx = x
        self.posy = y

    def cube_player(self ,screen):
    
        player1 = pygame.draw.rect(screen, self.color, (self.posx , self.posy, 50, 70))

        return player1
    
    def move_up(self, y):

        self.posy -= y

    def move_down(self, y):

        self.posy += y

    def move_left(self, x):

        self.posx -= x

    def move_right(self, x):

        self.posx += x

