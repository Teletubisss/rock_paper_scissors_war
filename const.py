import pygame

class Const:
    cellSize = 30
    cellNumber = 30
    screen = pygame.display.set_mode((cellNumber *cellSize, cellNumber *cellSize)) 
    clock = pygame.time.Clock()