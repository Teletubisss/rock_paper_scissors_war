from person import Person
import pygame
from const import Const

class Rock(Person):
    color = pygame.image.load("images/rock.jpg").convert_alpha()
    color = pygame.transform.scale(color, (Const.cellSize, Const.cellSize))