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
        self.largeurW, self.hauteurW = self.scrrec[2]/2, self.scrrec[3]/4
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

        self.player1 = Player((252, 255, 55 ) ,self.hauteurW ,self.largeurW)

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

                self.player1.cube_player(self.window)
            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                clock.tick(60)
                pygame.display.flip()

                self.window.fill((0, 0, 0))

            pygame.quit()