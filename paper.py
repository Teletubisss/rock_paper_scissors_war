from person import Person
import pygame
from const import Const

class Paper(Person):
    color = pygame.image.load("images/paper.png").convert_alpha()
    color = pygame.transform.scale(color, (Const.cellSize, Const.cellSize))