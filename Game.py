# ()
# 5
#

import pygame
from Class.player import Player 

#creation de l'ecran d'acceuil

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
scrrec = window.get_rect()



class game:

    def run(self):

            clock = pygame.time.Clock()

            #boucle du jeux

            running = True

            while running:

                pygame.display.flip()

            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                clock.tick(60)

            pygame.quit()