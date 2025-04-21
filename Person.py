import pygame
import random

cellSize = 15
cellNumber = 40
screen = pygame.display.set_mode((cellNumber *cellSize, cellNumber *cellSize)) 
clock = pygame.time.Clock()

class Person:
    def __init__(self):
        self.xBeginning = 5
        self.yBeginning = 10

    def drawPerson(self):
        personRect = pygame.Rect(self.xBeginning * cellSize, self.yBeginning * cellSize, cellSize, cellSize)
        pygame.draw.rect(screen, (255, 0, 0), personRect)

    def randomPos(self):
        actions = [
            lambda pos: pos + 1,  # dodaje 2       lambda parametr(y): parametr(y) z dzialaniem - lambda arguments : expression
            lambda pos: pos,      # nic nie robi
            lambda pos: pos - 1   # odejmuje 1
        ]


        newX = random.choice(actions)(self.xBeginning)    #wybieramy random lambde(parametr)
        newY = random.choice(actions)(self.yBeginning)

        if 0 <= newX < cellNumber:   #jezeli bedzie w ekranie - potem jak przemnozymy przy rysowaniu przez cellSize
            self.xBeginning = newX

        if 0 <= newY < cellNumber:
            self.yBeginning = newY
