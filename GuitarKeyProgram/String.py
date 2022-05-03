import pygame
BLACK = (0,0,0)

class String:

    def __init__(self,name,number):
        self.name = name
        self.number = number

    def draw(self, WIN):
        x1 = 79 + (self.number - 1) * 28.655
        x2 = 329 + (self.number - 1) * 28.655
        w = 6.5 - (self.number -1) * .655

        pygame.draw.rect(WIN, BLACK, (x1, 25, w, 722))
        pygame.draw.rect(WIN, BLACK, (x2, 25, w, 722))

