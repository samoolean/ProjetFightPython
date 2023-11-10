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
        #pygame.display.set_icon('ico.png')
        self.scrrec = self.window.get_rect()

        # chargement de la map

        tmx_data = pytmx.load_pygame('map\\arena1.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.window.get_size())

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1 )

        #self.player1 = Player()
        #self.player1.add(self.group)

    def run(self):

            clock = pygame.time.Clock()

            #boucle du jeux

            running = True

            while running:

                self.group.draw(self.window)
                pygame.display.flip()
            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                clock.tick(60)

            pygame.quit()