from person import Person
import pygame
from const import Const

class Rock(Person):
    color = pygame.image.load("images/rock.png").convert_alpha()
    color = pygame.transform.scale(color, (Const.cellSize * 15, Const.cellSize * 15))