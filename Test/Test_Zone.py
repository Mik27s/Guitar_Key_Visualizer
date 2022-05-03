from logging import RootLogger
import pygame
import os

from pygame.locals import *

#DISPLAY SIZE
WIDTH, HEIGHT = 1025, 775
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guitar Key Visualizer")

#COLORS and Vari
DARKBLUE = (18, 112, 138)
BLACK = (0,0,0)
ORANGE = (237, 89, 14)
BONE = (176, 149, 76)
SILVER = (132, 132, 132)
WHITE = (255, 255, 255)
CENTERED = (-40, -13)
FPS = 144

CHICKEN = pygame.image.load(
    os.path.join('Test', 'HandCursorRedo.png'))
CHICKEN = pygame.transform.scale(CHICKEN, (129, 100))

def draw_window():
    WIN.fill(DARKBLUE)
    

    #Draw Background
    pygame.draw.rect(WIN, (WHITE), (8, 8, 500, 750))
    dotWidthChange = 27
    stringWidth = 6.5
    STRINGVARIED = 28
    

"""
class Button:
    def draw():
        #GAME TEXT and BUTTON BOXES
        TITLEFONT = pygame.font.SysFont("Goudy Stout", 18)
        BUFFER = 5
        KEYSELECTFONT = pygame.font.SysFont("palatino", 100)
        KeyNameArray = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
        pygame.draw.rect(WIN, BLACK, (545, 15, 450, 45))
        pygame.draw.rect(WIN, LIGHTYELLOW, (550, 20, 450, 45))
        label = TITLEFONT.render("Guitar Key Visualizer", 1 , BLACK)
        WIN.blit(label, (557, 25))
        Count4 = 0
        for x in range(535, 1055, 130):
            for y in range(80, 470, 130):

                pygame.draw.rect(WIN, BLACK, (x, y, 80, 80))
                pygame.draw.rect(WIN, LIGHTYELLOW, (x + BUFFER, y + BUFFER, 80, 80))
                label = KEYSELECTFONT.render(KeyNameArray[Count4], 1, (0,0,0))
                WIN.blit(label, (x + 10, y + 10))
                Count4 += 1

    ###-----------------------------------------------------------------------------------------------------------

button1 = Button()
#def draw(self):

#MAIN CODE LOOP

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
    
button1.draw()   
            
draw_window()


pygame.quit()
"""

    #Strings
    for i in range(79, 220, STRINGVARIED):
        
        """def string_interval_change(start,stop,stepiter):
            step = float(iter(.655))
            while start < stop:
                yield start
                start += next(step)
            
            for i in string_interval_change(0, 230[1,2,3,4,5,6]):"""
    
        pygame.draw.aaline(WIN, BLACK, (i, 27), (i, 747), blend=1)

    #Cursor
    MX, MY = pygame.mouse.get_pos()

    ROT = 0
    LOC = [MX, MY]

    WIN.blit(pygame.transform.rotate(CHICKEN, ROT), (LOC[0] + CENTERED[0], LOC[1] + CENTERED[1]))

    pygame.mouse.get_cursor()
    pygame.mouse.set_visible(0)

    

    pygame.display.update()
        
    

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()

"""
    #CIRCLES E (6th) String (0-12)
    pygame.draw.circle(WIN, (ORANGE), (83, 30), 8) # E
    pygame.draw.circle(WIN, (ORANGE), (83, 65), 8) # F
    pygame.draw.circle(WIN, (ORANGE), (83, 130), 8) # F# and Gb
    pygame.draw.circle(WIN, (ORANGE), (83, 195), 8) # G
    pygame.draw.circle(WIN, (ORANGE), (83, 260), 8) # G# and Ab
    pygame.draw.circle(WIN, (ORANGE), (83, 320), 8) # A
    pygame.draw.circle(WIN, (ORANGE), (83, 375), 8) # A# and Bb
    pygame.draw.circle(WIN, (ORANGE), (83, 435), 8) # B
    pygame.draw.circle(WIN, (ORANGE), (83, 495), 8) # C
    pygame.draw.circle(WIN, (ORANGE), (83, 550), 8) # C# and Db
    pygame.draw.circle(WIN, (ORANGE), (83, 605), 8) # D
    pygame.draw.circle(WIN, (ORANGE), (83, 655), 8) # D# and Eb
    pygame.draw.circle(WIN, (ORANGE), (83, 710), 8) # E

    #Circles A (5th) String (0-12)
    pygame.draw.circle(WIN, (ORANGE), (110, 30), 8) # A
    pygame.draw.circle(WIN, (ORANGE), (110, 65), 8) # A# and Bb
    pygame.draw.circle(WIN, (ORANGE), (110, 130), 8) # B
    pygame.draw.circle(WIN, (ORANGE), (110, 195), 8) # C
    pygame.draw.circle(WIN, (ORANGE), (110, 260), 8) # C# and Db
    pygame.draw.circle(WIN, (ORANGE), (110, 320), 8) # D
    pygame.draw.circle(WIN, (ORANGE), (110, 375), 8) # D# and Eb
    pygame.draw.circle(WIN, (ORANGE), (110, 435), 8) # E
    pygame.draw.circle(WIN, (ORANGE), (110, 495), 8) # F
    pygame.draw.circle(WIN, (ORANGE), (110, 550), 8) # F# and Gb
    pygame.draw.circle(WIN, (ORANGE), (110, 605), 8) # G
    pygame.draw.circle(WIN, (ORANGE), (110, 655), 8) # G# and Ab
    pygame.draw.circle(WIN, (ORANGE), (110, 710), 8) # A

    #Circles D (4th) String (0-12)
    pygame.draw.circle(WIN, (ORANGE), (138, 30), 8) # D
    pygame.draw.circle(WIN, (ORANGE), (138, 65), 8) # D# and Eb
    pygame.draw.circle(WIN, (ORANGE), (138, 130), 8) # E
    pygame.draw.circle(WIN, (ORANGE), (138, 195), 8) # F
    pygame.draw.circle(WIN, (ORANGE), (138, 260), 8) # F# and Gb
    pygame.draw.circle(WIN, (ORANGE), (138, 320), 8) # G
    pygame.draw.circle(WIN, (ORANGE), (138, 375), 8) # G# and Ab
    pygame.draw.circle(WIN, (ORANGE), (138, 435), 8) # A
    pygame.draw.circle(WIN, (ORANGE), (138, 495), 8) # A# and Bb
    pygame.draw.circle(WIN, (ORANGE), (138, 550), 8) # B
    pygame.draw.circle(WIN, (ORANGE), (138, 605), 8) # C
    pygame.draw.circle(WIN, (ORANGE), (138, 655), 8) # C# and Db
    pygame.draw.circle(WIN, (ORANGE), (138, 710), 8) # D

    #Circles G (3th) String (0-12)
    pygame.draw.circle(WIN, (ORANGE), (165, 30), 8) # G
    pygame.draw.circle(WIN, (ORANGE), (165, 65), 8) # G# and Ab
    pygame.draw.circle(WIN, (ORANGE), (165, 130), 8) # A
    pygame.draw.circle(WIN, (ORANGE), (165, 195), 8) # A# and Bb
    pygame.draw.circle(WIN, (ORANGE), (165, 260), 8) # B
    pygame.draw.circle(WIN, (ORANGE), (165, 320), 8) # C
    pygame.draw.circle(WIN, (ORANGE), (165, 375), 8) # C# and Db
    pygame.draw.circle(WIN, (ORANGE), (165, 435), 8) # D
    pygame.draw.circle(WIN, (ORANGE), (165, 495), 8) # D# and Eb
    pygame.draw.circle(WIN, (ORANGE), (165, 550), 8) # E
    pygame.draw.circle(WIN, (ORANGE), (165, 605), 8) # F
    pygame.draw.circle(WIN, (ORANGE), (165, 655), 8) # F# and Gb
    pygame.draw.circle(WIN, (ORANGE), (165, 710), 8) # G

    #Circles B (2th) String (0-12) 
    pygame.draw.circle(WIN, (ORANGE), (192, 30), 8) # B
    pygame.draw.circle(WIN, (ORANGE), (192, 65), 8) # C
    pygame.draw.circle(WIN, (ORANGE), (192, 130), 8) # C# and Db
    pygame.draw.circle(WIN, (ORANGE), (192, 195), 8) # D
    pygame.draw.circle(WIN, (ORANGE), (192, 260), 8) # D# and Eb
    pygame.draw.circle(WIN, (ORANGE), (192, 320), 8) # E
    pygame.draw.circle(WIN, (ORANGE), (192, 375), 8) # F
    pygame.draw.circle(WIN, (ORANGE), (192, 435), 8) # F# and Gb
    pygame.draw.circle(WIN, (ORANGE), (192, 495), 8) # G
    pygame.draw.circle(WIN, (ORANGE), (192, 550), 8) # G# and Ab
    pygame.draw.circle(WIN, (ORANGE), (192, 605), 8) # A
    pygame.draw.circle(WIN, (ORANGE), (192, 655), 8) # A# and Bb
    pygame.draw.circle(WIN, (ORANGE), (192, 710), 8) # B

    #Circles E (1th) String (0-12) 
    pygame.draw.circle(WIN, (ORANGE), (219, 30), 8) # E
    pygame.draw.circle(WIN, (ORANGE), (219, 65), 8) # F
    pygame.draw.circle(WIN, (ORANGE), (219, 130), 8) # F# and Gb
    pygame.draw.circle(WIN, (ORANGE), (219, 195), 8) # G
    pygame.draw.circle(WIN, (ORANGE), (219, 260), 8) # G# and Ab
    pygame.draw.circle(WIN, (ORANGE), (219, 320), 8) # A
    pygame.draw.circle(WIN, (ORANGE), (219, 375), 8) # A# and Bb
    pygame.draw.circle(WIN, (ORANGE), (219, 435), 8) # B
    pygame.draw.circle(WIN, (ORANGE), (219, 495), 8) # C
    pygame.draw.circle(WIN, (ORANGE), (219, 550), 8) # C# and Db
    pygame.draw.circle(WIN, (ORANGE), (219, 605), 8) # D
    pygame.draw.circle(WIN, (ORANGE), (219, 655), 8) # D# and Eb
    pygame.draw.circle(WIN, (ORANGE), (219, 710), 8) # E


    #################################################################################################################

    #Circles E (6th) String (12-24)
    pygame.draw.circle(WIN, (ORANGE), (315, 60), 8) # E
    pygame.draw.circle(WIN, (ORANGE), (315, 120), 8) # F
    pygame.draw.circle(WIN, (ORANGE), (315, 185), 8) # F# and Gb
    pygame.draw.circle(WIN, (ORANGE), (316, 245), 8) # G
    pygame.draw.circle(WIN, (ORANGE), (316, 300), 8) # G# and Ab
    pygame.draw.circle(WIN, (ORANGE), (316, 355), 8) # A
    pygame.draw.circle(WIN, (ORANGE), (316, 410), 8) # A# and Bb
    pygame.draw.circle(WIN, (ORANGE), (316, 465), 8) # B
    pygame.draw.circle(WIN, (ORANGE), (317, 517), 8) # C
    pygame.draw.circle(WIN, (ORANGE), (317, 565), 8) # C# and Db
    pygame.draw.circle(WIN, (ORANGE), (317, 620), 8) # D
    pygame.draw.circle(WIN, (ORANGE), (317, 665), 8) # D# and Eb
    pygame.draw.circle(WIN, (ORANGE), (317, 715), 8) # E

    #Circles A (5th) String (12-24)
    pygame.draw.circle(WIN, (ORANGE), (340, 60), 8) # A
    pygame.draw.circle(WIN, (ORANGE), (340, 120), 8) # A# and Bb
    pygame.draw.circle(WIN, (ORANGE), (340, 185), 8) # B
    pygame.draw.circle(WIN, (ORANGE), (341, 245), 8) # C
    pygame.draw.circle(WIN, (ORANGE), (341, 300), 8) # C# and Db
    pygame.draw.circle(WIN, (ORANGE), (341, 355), 8) # D
    pygame.draw.circle(WIN, (ORANGE), (341, 410), 8) # D# and Eb
    pygame.draw.circle(WIN, (ORANGE), (341, 465), 8) # E
    pygame.draw.circle(WIN, (ORANGE), (342, 517), 8) # F
    pygame.draw.circle(WIN, (ORANGE), (342, 565), 8) # F# and Gb
    pygame.draw.circle(WIN, (ORANGE), (342, 620), 8) # G
    pygame.draw.circle(WIN, (ORANGE), (342, 665), 8) # G# and Ab
    pygame.draw.circle(WIN, (ORANGE), (342, 715), 8) # A

    #Circles D (4th) String (12-24)
    pygame.draw.circle(WIN, (ORANGE), (367, 60), 8) # D
    pygame.draw.circle(WIN, (ORANGE), (367, 120), 8) # D# and Eb
    pygame.draw.circle(WIN, (ORANGE), (367, 185), 8) # E
    pygame.draw.circle(WIN, (ORANGE), (368, 245), 8) # F
    pygame.draw.circle(WIN, (ORANGE), (368, 300), 8) # F# and Gb
    pygame.draw.circle(WIN, (ORANGE), (368, 355), 8) # G
    pygame.draw.circle(WIN, (ORANGE), (368, 410), 8) # G# and Ab
    pygame.draw.circle(WIN, (ORANGE), (368, 465), 8) # A
    pygame.draw.circle(WIN, (ORANGE), (369, 517), 8) # A# and Bb
    pygame.draw.circle(WIN, (ORANGE), (369, 565), 8) # B
    pygame.draw.circle(WIN, (ORANGE), (369, 620), 8) # C
    pygame.draw.circle(WIN, (ORANGE), (369, 665), 8) # C# and Db
    pygame.draw.circle(WIN, (ORANGE), (369, 715), 8) # D

    #Circles G (3th) String (12-24)
    pygame.draw.circle(WIN, (ORANGE), (393, 60), 8) # G
    pygame.draw.circle(WIN, (ORANGE), (393, 120), 8) # G# and Ab
    pygame.draw.circle(WIN, (ORANGE), (393, 185), 8) # A
    pygame.draw.circle(WIN, (ORANGE), (394, 245), 8) # A# and Bb
    pygame.draw.circle(WIN, (ORANGE), (394, 300), 8) # B
    pygame.draw.circle(WIN, (ORANGE), (394, 355), 8) # C
    pygame.draw.circle(WIN, (ORANGE), (394, 410), 8) # C# and Db
    pygame.draw.circle(WIN, (ORANGE), (394, 465), 8) # D
    pygame.draw.circle(WIN, (ORANGE), (395, 517), 8) # D# and Eb
    pygame.draw.circle(WIN, (ORANGE), (395, 565), 8) # E
    pygame.draw.circle(WIN, (ORANGE), (395, 620), 8) # F
    pygame.draw.circle(WIN, (ORANGE), (395, 665), 8) # F# and Gb
    pygame.draw.circle(WIN, (ORANGE), (395, 715), 8) # G

    #Circles B (2th) String (12-24) 
    pygame.draw.circle(WIN, (ORANGE), (418, 60), 8) # B
    pygame.draw.circle(WIN, (ORANGE), (418, 120), 8) # C
    pygame.draw.circle(WIN, (ORANGE), (418, 185), 8) # C# and Db
    pygame.draw.circle(WIN, (ORANGE), (419, 245), 8) # D
    pygame.draw.circle(WIN, (ORANGE), (419, 300), 8) # D# and Eb
    pygame.draw.circle(WIN, (ORANGE), (419, 355), 8) # E
    pygame.draw.circle(WIN, (ORANGE), (419, 410), 8) # F
    pygame.draw.circle(WIN, (ORANGE), (419, 465), 8) # F# and Gb
    pygame.draw.circle(WIN, (ORANGE), (420, 517), 8) # G
    pygame.draw.circle(WIN, (ORANGE), (420, 565), 8) # G# and Ab
    pygame.draw.circle(WIN, (ORANGE), (420, 620), 8) # A
    pygame.draw.circle(WIN, (ORANGE), (420, 665), 8) # A# and Bb
    pygame.draw.circle(WIN, (ORANGE), (420, 715), 8) # B

    #Circles E (1th) String (12-24) 
    pygame.draw.circle(WIN, (ORANGE), (443, 60), 8) # E
    pygame.draw.circle(WIN, (ORANGE), (443, 120), 8) # F
    pygame.draw.circle(WIN, (ORANGE), (443, 185), 8) # F# and Gb
    pygame.draw.circle(WIN, (ORANGE), (444, 245), 8) # G
    pygame.draw.circle(WIN, (ORANGE), (444, 300), 8) # G# and Ab
    pygame.draw.circle(WIN, (ORANGE), (444, 355), 8) # A
    pygame.draw.circle(WIN, (ORANGE), (444, 410), 8) # A# and Bb
    pygame.draw.circle(WIN, (ORANGE), (444, 465), 8) # B
    pygame.draw.circle(WIN, (ORANGE), (445, 517), 8) # C
    pygame.draw.circle(WIN, (ORANGE), (445, 565), 8) # C# and Db
    pygame.draw.circle(WIN, (ORANGE), (445, 620), 8) # D
    pygame.draw.circle(WIN, (ORANGE), (445, 665), 8) # D# and Eb
    pygame.draw.circle(WIN, (ORANGE), (445, 715), 8) # E
    """
 #0-12 fret nested loop dot draw STORAGE
    
"""for i in range(82, 220, dotWidthChange + OFFSET):
    pygame.draw.circle(WIN, (ORANGE), (i + OFFSET, 21), 8)
    #OFFSET += .655

    for i in range(82, 220, dotWidthChange + OFFSET2):
        for j in range(52 ,725, 60):
            def varied_step_range(start,stop,stepiter):
                step = iter(stepiter)
                while start < stop:
                    yield start
                    start += next(step)
            pygame.draw.circle(WIN, (ORANGE), (i + OFFSET2, j), 8)
            OFFSET2 += .655
        
    for i in varied_step_range(0,6[1,2,3,4,5,6]):"""

"""GUITAR_FRETBOARD_IMAGE = pygame.image.load(
    os.path.join('GuitarKeyProgram', 'GuitarNeckBase.png'))
GUITAR_FRETBOARD_IMAGE = pygame.transform.scale(GUITAR_FRETBOARD_IMAGE, (500, 750))"""