# ()
# 5
# []
# !

import pygame
import pytmx
import pyscroll
from Class.player import Player 

class Game:

    def __init__(self):
        
        #creation de l'ecran d'acceuil

        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('fight !')
        ico = pygame.image.load('fight.png')
        pygame.display.set_icon(ico)

        self.scrrec = self.window.get_rect()
        self.largeurW, self.hauteurW = self.scrrec[2]/4, self.scrrec[3]/4
        print(self.largeurW, self.hauteurW)

        # Lecteur de musique 

        musique = pygame.mixer.Sound('sound\\musique\\Princess_Mushroom.ogg')
        musique.play()

        # chargement de la map

        # map = 'map\\arena1.tmx'
        # tmx_data = pytmx.util_pygame.load_pygame('map\\arena0.tmx')
        # map_data = pyscroll.data.TiledMapData(tmx_data)
        # map_layer = pyscroll.orthographic.BufferedRenderer(map_data, t)

        # self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

        # map_layer.zoom = 0.1

        #self.player1 = Player()
        #self.player1.add(self.group)

            # gravity

        self.surface_Y = self.hauteurW

        self.player1 = Player((252, 255, 55 ) ,self.hauteurW ,self.largeurW ,self.surface_Y ,self.window)
        self.player2 = Player((55, 255, 76 ) ,self.hauteurW ,self.largeurW ,self.surface_Y ,self.window)



    def run(self):

        clock = pygame.time.Clock()

        #boucle du jeux

        running = True

        while running:

            # self.group.draw(self.window)
            
            if pygame.key.get_pressed()[pygame.K_z]:
                self.player1.move_up(1)

            if pygame.key.get_pressed()[pygame.K_s]:


                self.player1.move_down(1)
                
            if pygame.key.get_pressed()[pygame.K_q]:
                self.player1.move_left(1)

            if pygame.key.get_pressed()[pygame.K_d]:
                self.player1.move_right(1)

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.player1.jumping = True
    
            # jump

            if self.player1.jumping:
                self.player1.jump(self.surface_Y)

                """
                self.Player1 = JUMPING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
                self.window.blit(JUMPING_SURFACE, mario_rect)
            else:
                mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
                SCREEN.blit(STANDING_SURFACE, mario_rect)

                """

            self.player1.cube_player()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)
            pygame.display.flip()

            self.window.fill((0, 0, 0))

        pygame.quit()