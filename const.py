import pygame

class Const:
    cellSize = 5
    cellNumber = 150
    screen = pygame.display.set_mode((cellNumber *cellSize * 1.5, cellNumber *cellSize)) 
    clock = pygame.time.Clock()
