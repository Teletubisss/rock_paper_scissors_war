import pygame
import sys
from rock import Rock
from paper import Paper
from scissors import Scissors
from const import Const


class Main:
    def __init__(self):
        self.papers = []
        self.rocks = []
        self.scissors = []


    def drawElements(self):
        for i in range(50):
            paper = Paper()
            paper.xBeginning = 56
            paper.yBeginning = 112
            self.papers.append(paper)
        for x in range(50):
            rock = Rock()
            rock.xBeginning = 169
            rock.yBeginning = 112
            self.rocks.append(rock)
        for x in range(50):
            scissor = Scissors()
            scissor.xBeginning = 112
            scissor.yBeginning = 37
            self.scissors.append(scissor)


    def checkCollision(self):
        rocks_to_remove = []
        for rock in self.rocks:
            for paper in self.papers:
                if rock.getPos() == paper.getPos():
                    rocks_to_remove.append(rock)
        for rock in rocks_to_remove:
            if rock in self.rocks:  # sprawdzamy, czy nadal jest
                self.rocks.remove(rock)

        papers_to_remove = []
        for paper in self.papers:
            for scissor in self.scissors:
                if paper.getPos() == scissor.getPos():
                    papers_to_remove.append(paper)
        for paper in papers_to_remove:
            if paper in self.papers:
                self.papers.remove(paper)

        scissors_to_remove = []
        for scissor in self.scissors:
            for rock in self.rocks:
                if scissor.getPos() == rock.getPos():
                    scissors_to_remove.append(scissor)
        for scissor in scissors_to_remove:
            if scissor in self.scissors:
                self.scissors.remove(scissor)




        

main = Main()

main.drawElements()
pygame.init()

while True:                                  
    for event in pygame.event.get():          #pygame.event - interaktujer z eventami, .get() - bierze eventy z kolejki
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()                        #gdyby to na gorze sie rypnelo, to reszte wylaczy

# Zamiast fill:
    Const.screen.blit(pygame.transform.scale(
        pygame.image.load("images/bg.jpg").convert(),
        (Const.cellSize * Const.cellNumber * 1.5, Const.cellSize * Const.cellNumber)
    ), (0, 0))



    for paper in main.papers:
        paper.drawPerson()
        paper.randomPos()
    for rock in main.rocks:
        rock.drawPerson()
        rock.randomPos()
    for scissor in main.scissors:
        scissor.drawPerson()
        scissor.randomPos()

    main.checkCollision()

    pygame.display.update()                     #wrzxuca na ekran to, co my rysujem,y na tzw. sufrace - buforze ekranu
    Const.clock.tick(20)                             #liczy czas co 60fps - gdyby nie to to na roznych kompach lecialoby szybciej lub woniei