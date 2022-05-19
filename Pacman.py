# ARCHIMBAUD Clément
#archimbaud.clement.dh@gmail.com
#Code contenant la Class PacMan
#V0.1

from pygame import Vector2
import pygame
import core

class Pacman:
    def __init__(self):
        self.rayon = 50                                           #Definition des Caractéristiques du Pacman
        self.couleur = (255 , 100 , 0)
        self.position = Vector2(200 , 200)
        self.direction = Vector2(0, 0)

    def deplacement(self):                                          #pour faire bouger Pacman

        if core.getKeyPressList("z"):
            self.direction = Vector2(self.direction.x, -1)
        if core.getKeyPressList("s"):
            self.direction = Vector2(self.direction.x, 1)
        if core.getKeyPressList("q"):
            self.direction = Vector2(-1, self.direction.y)
        if core.getKeyPressList("d"):
            self.direction = Vector2(1, self.direction.y)

    def draw(self):                                                 #pour dessiner Pacman
        core.Draw.circle(self.couleur, self.position, self.rayon)