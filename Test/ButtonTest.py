import pygame, sys

"""class Button:
    def __init__(self,text,width,height,pos):"""


pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("ButtonTest")
clock = pygame.time.Clock()
TITLEFONT = pygame.font.SysFont("Ariel", 18)
LIGHTYELLOW = (243, 247, 220)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(LIGHTYELLOW)

    pygame.display.update()
    clock.tick(144)