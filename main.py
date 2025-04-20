import pygame
import random
from Person import Person
import sys


cellSize = 30
cellNumber = 30
screen = pygame.display.set_mode((cellNumber *cellSize, cellNumber *cellSize)) 
clock = pygame.time.Clock()



class Main:
    def __init__(self):
        self.person = Person()

    def drawElements(self):
        self.person.drawPerson()

main = Main()

while True:                                  
    for event in pygame.event.get():          #pygame.event - interaktujer z eventami, .get() - bierze eventy z kolejki
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()                        #gdyby to na gorze sie rypnelo, to reszte wylaczy

    screen.fill((75, 180, 113))

    main.drawElements()
    main.person.randomPos()

    pygame.display.update()                     #wrzxuca na ekran to, co my rysujem,y na tzw. sufrace - buforze ekranu
    clock.tick(5)                             #liczy czas co 60fps - gdyby nie to to na roznych kompach lecialoby szybciej lub woniei