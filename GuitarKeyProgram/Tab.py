import pygame
BLACK = (0,0,0)
ORANGE = (237, 89, 14)

class Tab:

    def __init__(self,string,fret,name):
        self.string = string
        self.fret = fret
        self.name = name

    def draw(self,WIN):
        y = 52 + (self.fret * 60)
        x = 82 if self.fret < 13 else 332
        x += (self.string - 1) * 27.655
        pygame.draw.circle(WIN, BLACK, (x, y), 10)
        pygame.draw.circle(WIN, ORANGE, (x + 1, y + 1), 8)
