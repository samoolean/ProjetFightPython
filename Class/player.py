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

    def __init__(self, color, x, y ,screen, name):

        self.color = color
        self.posx = x
        self.posy = y
        self.screen = screen
        self.jumping = False
        self.allowToDodge = True
        self.jump_height = 14
        self.y_velocity = self.jump_height
        self.Y_GRAVITY = 0.5
        self.x_velocity = 7
        self.floor = self.posy
        self.count_jump = 3
        self.box = Player.cube_player(self)
        self.life = 600
        self.players = []
        self.namep = name
        self.myself = Player.create_myself()

    def create_myself(self):

        myself = Player(self.color ,70 ,40,self.screen, self.namep)

    def cube_player(self):
    
        player1 = pygame.draw.rect(self.screen, self.color, (self.posx , self.posy, 50, 70))

        return player1
    
    def find_players(self):

        self.players = []
        
    def get_box(self):

        self.box.move(self.posx,self.floor)

    # movement player
    
    def move_up(self, y):

        self.posy -= y

    def move_down(self, y):

        if self.posy + y > self.floor :
            pass
        else:
            self.posy += y

    def move_left(self, x):

        self.posx -= x

    def move_right(self, x):

        self.posx += x

    def jump(self):

        print('im jumping')

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
        else: 
            print(self.posy ,self.floor )

    # life of player

    def take_damage(self, damage):

        self.life = self.life - damage
        if self.life <= 0 :
            self.kill_player()
        
    def kill_player(self):
        print("i'm dead")
        pass

    def attaque(self, attaque_type):

        # do attaque stuff

        """
        for a rectangle it's util tip's :
        
        rect2.center = (20,30) # for set the center of rect

        Rect(left, top, width, height) -> Rect
        Rect((left, top), (width, height)) -> Rect
        Rect(object) -> Rect
        
        dimension des persos : heigt 70, widht 50.

        """
     
        match attaque_type:
            case 1:
                print('spike_basic')
                hitbox =  pygame.draw.rect(self.screen, (255, 0, 0) ,(self.posx , self.posy + 70 + 20, 50, 20))
                if hitbox.colliderect(self.players[1].box):
                    self.players[1].take_damage(600)
                else:
                    pass

            case 2:
                print('down_light_attaque')
                hitbox1 =  pygame.draw.rect(self.screen, (255, 0, 0) ,(self.posx - 30, self.posy + 40, 25, 30))
                hitbox2 =  pygame.draw.rect(self.screen, (255, 0, 0) ,(self.posx + 55, self.posy + 40, 25, 30))
                if hitbox1.colliderect(self.players[1].box):
                    self.players[1].take_damage(600)
                else:
                    if hitbox2.colliderect(self.players[1].box):
                            self.players[1].take_damage(600)
                    else:
                        pass

            case _:
                return print('Weird move')
        
    def dodge(self):

        self.players.pop(0)

    def undo_dodge(self):

        self.players.append(self.myself)


