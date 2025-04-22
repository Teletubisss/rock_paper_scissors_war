from person import Person
import pygame
from const import Const

class Scissors(Person):
    color = pygame.image.load("images/scissors.jpg").convert_alpha()
    color = pygame.transform.scale(color, (Const.cellSize, Const.cellSize))
