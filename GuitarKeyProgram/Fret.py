import pygame
SILVER = (132, 132, 132)
BONE = (176, 149, 76)

class Fret:

    def __init__(self,num):
        self.num = num

    def draw(self,WIN):
        x = 76 if self.num < 13 else 326
        y = 75 + self.num * 60
        h = 7 if self.num > 0 else 12
        color = SILVER if self.num > 0 else BONE
        pygame.draw.rect(WIN, color, (x, y, 150, h))