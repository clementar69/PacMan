# ARCHIMBAUD Clément
#archimbaud.clement.dh@gmail.com
#Main du Jeu PacMan en Python V3.8
#V0.1

from Pacman import Pacman
import core
import pygame
#from Creeps import Creeps
#rom Enemie import Enemie

def setup():
    core.WINDOW_SIZE = [1200,800]              # taille de l'écran
    core.fps = 60                              #rafraîchissement de l'écran
    core.memory("Pacman", Pacman())            #crée une variable Pacman qui reprend la class Pacman
    core.memory("score",0)                     # crée une variable score qui est =  0



def run ():
    core.cleanScreen()
    core.memory("Pacman").draw()               #pour dessiner Pacman
    core.memory("Pacman").deplacement()        #pour faire bouger Pacman

 #   core.memory("TableauDeCreeps", [])
  #  for i in range(100):
   #     core.memory("TableauDeCreeps").append(Creeps())


#Score
    myFont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myFont.render("Score :" + str(core.memory("score")), False, (255, 0, 0))
    core.screen.blit(textsurface, (core.WINDOW_SIZE[0] / 2 - -400, core.WINDOW_SIZE[1] / 2 + -400))


if __name__=="__main__":                 # obligatoire , ce qui permet de lire le setup et le run
    core.main(setup,run)