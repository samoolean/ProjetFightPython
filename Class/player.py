# ()
# 5
# []
# !
# < >

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

    def __init__(self, color, x, y ,screen):

        self.color = color
        self.posx = x
        self.posy = y
        self.screen = screen
        self.jumping = False
        self.jump_height = 14
        self.y_velocity = self.jump_height
        self.Y_GRAVITY = 0.5
        self.x_velocity = 7
        self.floor = self.posy
        self.count_jump = 3
        self.box = Player.cube_player(self)

    def cube_player(self):
    
        player1 = pygame.draw.rect(self.screen, self.color, (self.posx , self.posy, 50, 70))

        return player1
    
    def get_box(self):

        self.box.move(self.posx,self.floor)

    # movement player
    
    def move_up(self, y):

        self.posy -= y

    def move_down(self, y):

        if self.posy + y > self.floor :
            print( 'I cant get down ', self.posy)
        else:
            self.posy += y

    def move_left(self, x):

        self.posx -= x

    def move_right(self, x):

        self.posx += x

    def jump(self):
        
        self.posy -= self. y_velocity
        self.y_velocity -= self.Y_GRAVITY
        if self.y_velocity < -self.jump_height:
            self.jumping = False
            self.y_velocity = self.jump_height

    def fastfall(self):
        
        """

        if self.posy > self.floor :
            self.Y_GRAVITY = 2
            if self.posy < self.floor :
                self.Y_GRAVITY = 0.5

        """
        if self.posy < self.floor :
            self.y_velocity -= 1
            if self.posy > self.floor :
                self.y_velocity = self.jump_height
            print('5')
        else: print(self.posy ,self.floor )
        