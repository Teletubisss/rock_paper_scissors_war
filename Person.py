import pygame
import random

cellSize = 30
cellNumber = 30
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
            lambda pos: pos + 2,  # dodaje 2       #lambda parametr(y): parametr(y) z dzialaniem - lambda arguments : expression
            lambda pos: pos,      # nic nie robi
            lambda pos: pos - 1   # odejmuje 1
        ]

        self.xBeginning = random.choice(actions)(self.xBeginning)   #wybieramy random lambde(parametr)
        self.yBeginning = random.choice(actions)(self.yBeginning)
