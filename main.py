import pygame
import random
import sys
from rock import Rock
from paper import Paper
from scissors import Scissors
from const import Const

screen = pygame.display.set_mode((Const.cellNumber *Const.cellSize, Const.cellNumber *Const.cellSize)) 
clock = pygame.time.Clock()

class Main:
    def __init__(self):
        self.papers = []
        self.rocks = []
        self.scissors = []

    def drawElements(self):
        for i in range(10):
            paper = Paper()
            paper.xBeginning = 5
            paper.yBeggining = 5
            self.papers.append(paper)
        for x in range(10):
            rock = Rock()
            rock.xBeginning = 20
            rock.yBeginning = 15
            self.rocks.append(rock)
        for x in range(10):
            scissor = Scissors()
            scissor.xBeginning = 10
            scissor.yBeginning = 20
            self.scissors.append(scissor)


        

main = Main()

main.drawElements()

while True:                                  
    for event in pygame.event.get():          #pygame.event - interaktujer z eventami, .get() - bierze eventy z kolejki
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()                        #gdyby to na gorze sie rypnelo, to reszte wylaczy

    screen.fill((75, 180, 113))


    for paper in main.papers:
        paper.drawPerson(screen)
        paper.randomPos()
    for rock in main.rocks:
        rock.drawPerson(screen)
        rock.randomPos()
    for scissor in main.scissors:
        scissor.drawPerson(screen)
        scissor.randomPos()



    pygame.display.update()                     #wrzxuca na ekran to, co my rysujem,y na tzw. sufrace - buforze ekranu
    clock.tick(5)                             #liczy czas co 60fps - gdyby nie to to na roznych kompach lecialoby szybciej lub woniei