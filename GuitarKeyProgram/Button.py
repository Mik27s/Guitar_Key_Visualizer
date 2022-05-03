import pygame
BLACK = (0,0,0)
LIGHTYELLOW = (243, 247, 220)
BUFFER = 5
KEYSELECTFONT = pygame.font.SysFont("palatino", 100)
class Button:

    def __init__(self,x,y,label,action):
        self.label = label
        self.action = action
        self.x = x
        self.y = y

    def draw(self, WIN):
        pygame.draw.rect(WIN, BLACK, (self.x, self.y, 80, 80))
        pygame.draw.rect(WIN, LIGHTYELLOW, (self.x + BUFFER, self.y + BUFFER, 80, 80))
        label = KEYSELECTFONT.render(self.label, 1, BLACK)
        WIN.blit(label, (self.x + 10, self.y + 10))
    
    def click(self):
        self.action()