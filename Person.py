import pygame
import random
from const import Const


class Person:
    def __init__(self):
        self.xBeginning = 0
        self.yBeginning = 0

    def drawPerson(self):
        personRect = pygame.Rect(self.xBeginning * Const.cellSize, self.yBeginning * Const.cellSize, Const.cellSize * 15, Const.cellSize * 15)
        Const.screen.blit(self.color, personRect)

    def randomPos(self):
        actions = [
            lambda pos: pos + 2,
            lambda pos: pos + 1,  # dodaje 2       lambda parametr(y): parametr(y) z dzialaniem - lambda arguments : expression
            lambda pos: pos,      # nic nie robi
            lambda pos: pos - 1,   # odejmuje 1
            lambda pos: pos - 2
        ]


        newX = random.choice(actions)(self.xBeginning)    #wybieramy random lambde(parametr)
        newY = random.choice(actions)(self.yBeginning)

        if 0 <= newX < Const.cellNumber * 1.5:   #jezeli bedzie w ekranie - potem jak przemnozymy przy rysowaniu przez cellSize
            self.xBeginning = newX

        if 0 <= newY < Const.cellNumber:
            self.yBeginning = newY

    def getPos(self):
        pos = (self.xBeginning, self.yBeginning)
        return pos
