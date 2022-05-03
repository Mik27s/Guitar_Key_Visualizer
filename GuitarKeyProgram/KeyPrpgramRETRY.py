#Guitar Key Visualizer Code
from cgitb import text
from pickle import TRUE
from tkinter import OFF
from tracemalloc import start, stop
import pygame
from pygame.locals import *
import os
pygame.init()

#DISPLAY SIZE
WIDTH, HEIGHT = 1050, 775
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guitar Key Visualizer")

CHICKEN = pygame.image.load(
    os.path.join('Test', 'HandCursorRedo.png'))
CHICKEN = pygame.transform.scale(CHICKEN, (129, 100))

#COLORS and Vari
DARKBLUE = (18, 112, 138)
BLACK = (0,0,0)
ORANGE = (237, 89, 14)
BONE = (176, 149, 76)
SILVER = (132, 132, 132)
WHITE = (255, 255, 255)
LIGHTYELLOW = (243, 247, 220)
CENTERED = (-40, -13)
FPS = 144



def draw_window():
    WIN.fill(DARKBLUE)
    #WIN.blit(GUITAR_FRETBOARD_IMAGE, (12.5,12.5))
    #Draw Background
    pygame.draw.rect(WIN, (LIGHTYELLOW), (8, 8, 500, 750))
    dotWidthChange = 27
    stringWidth = 6.5
    stringWide = 6.5
    STRINGVARIED = 28
    OFFSET = 0
    OFFSET2 = 0
    OFFSET3 = 0
    OFFSET4 = 0
    OFFSET5 = 0
    PLUSINDEX = 250
    BUFFER = 5
    FRETFONT = pygame.font.SysFont("palatino", 35)
    TITLEFONT = pygame.font.SysFont("Goudy Stout", 18)
    KEYSELECTFONT = pygame.font.SysFont("palatino", 100)
    

    # 0-12 frets and strings
    #Frets
    for i in range(75 ,736, 60):
        pygame.draw.rect(WIN, (SILVER), (76, i, 150, 7))

    #Strings
    for i in range(79, 220, STRINGVARIED):
        pygame.draw.rect(WIN, (BLACK), (i, 25, stringWidth, 722))
        stringWidth -= .655
    

    #Dot Inlays
    for x in range(170 ,600, 120):
        pygame.draw.circle(WIN, (BLACK), (152, x), 8)

    for x in range (122, 200, 55):
        pygame.draw.circle(WIN, (BLACK), (x, 710), 8)

    #Nut
    pygame.draw.rect(WIN, (BONE), (76, 16, 150, 12))

    #0-12 fret nested loop dot draw
    for x in range(82, 220, dotWidthChange + OFFSET):

        pygame.draw.circle(WIN, (BLACK), (x + OFFSET, 21), 10)
        pygame.draw.circle(WIN, (ORANGE), (x + OFFSET, 21), 8)
        OFFSET += .655

    for x in range(82, 220, dotWidthChange + OFFSET2):
        for y in range(52 ,725, 60):
            
            pygame.draw.circle(WIN, (BLACK), (x + OFFSET2, y), 10)
            pygame.draw.circle(WIN, (ORANGE), (x + OFFSET2, y), 8)
        OFFSET2 += .655

    
    ###----------------------------------------------------------------------------------------------------
    # 12-24 frets and strings
    #Frets
    for i in range(20 ,736, 60):
        pygame.draw.rect(WIN, (SILVER), (76 + PLUSINDEX, i, 150, 7))

    #Strings
    for i in range(79 + PLUSINDEX, 220 + PLUSINDEX, STRINGVARIED):
        pygame.draw.rect(WIN, (BLACK), (i, 27, stringWide, 715))
        stringWide -= .655
    
    #Dot Inlays
    for x in range(170 ,600, 120):
        pygame.draw.circle(WIN, (BLACK), (152 + PLUSINDEX, x + 60), 8)

    for x in range(373 ,452, 55):
        pygame.draw.circle(WIN, (BLACK), (x, 52), 8)

    #12-24 fret nested loop dot draw
    for x in range(82 + PLUSINDEX, 220 + PLUSINDEX, dotWidthChange + OFFSET4):
        for y in range(52 ,725, 60):
            
            pygame.draw.circle(WIN, (BLACK), (x + OFFSET4, y), 10)
            pygame.draw.circle(WIN, (ORANGE), (x + OFFSET4, y), 8)
        OFFSET4 += .655

    #Textboxes for frets
    numArray = ["1","2","3","4","5","6","7","8","9","10","11","12"]
    numArray3 = ["12","13","14","15","16","17","18","19","20","21","22","23"]
    Count = 0
    Count2 = 0
    Count3 = 0
    Count4 = 0

    for y in range(40, 720, 60):
        label = FRETFONT.render(numArray[Count], 1, (0,0,0))
        text_rect = label.get_rect()
        text_rect.right = 60
        text_rect.top = y
        WIN.blit(label, text_rect)
        Count += 1
    
    for x in range(40, 725, 60):
        label = FRETFONT.render(numArray3[Count3], 1, (0,0,0))
        WIN.blit(label, (35 + PLUSINDEX, x))
        Count3 += 1

    #Cursor
    ROT = 0
    MX, MY = pygame.mouse.get_pos()
    #print(MX, MY)
    
    LOC = [MX, MY]

    WIN.blit(pygame.transform.rotate(CHICKEN, ROT), 
    (LOC[0] + CENTERED[0], LOC[1] + CENTERED[1]))

    pygame.mouse.get_pos(1)
    pygame.mouse.set_visible(0)
    
    ###-----------------------------------------------------------------------------------------------------------

    #GAME TEXT and BUTTON BOXES
    KeyNameArray = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
    for x in range(535, 1055, 130):
        for y in range(80, 470, 130):

            pygame.draw.rect(WIN, BLACK, (x, y, 80, 80))
            pygame.draw.rect(WIN, LIGHTYELLOW, (x + BUFFER, y + BUFFER, 80, 80))
            label = KEYSELECTFONT.render(KeyNameArray[Count4], 1, (0,0,0))
            WIN.blit(label, (x + 10, y + 10))
            Count4 += 1

    pygame.draw.rect(WIN, BLACK, (545, 15, 450, 45))
    pygame.draw.rect(WIN, LIGHTYELLOW, (550, 20, 450, 45))
    label = TITLEFONT.render("Guitar Key Visualizer", 1 , BLACK)
    WIN.blit(label, (557, 25))
    Count4 = 0
    
    
    pygame.display.update()

    ###-----------------------------------------------------------------------------------------------------------


#MAIN CODE LOOP
def main():
    left_click = False
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0] == 1 and left_click == False:
                left_click = True
                print("clicked")
        if pygame.mouse.get_pressed()[0] == 0:
            left_click = False  
            
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()

#OLD CODE STORAGE
