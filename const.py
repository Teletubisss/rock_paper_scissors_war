import pygame

class Const:
    cellSize = 5
    cellNumber = 200
    screen = pygame.display.set_mode((cellNumber *cellSize, cellNumber *cellSize)) 
    clock = pygame.time.Clock()
    