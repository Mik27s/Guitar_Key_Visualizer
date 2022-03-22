#Guitar Key Visualizer Code
import pygame
import os

#DISPLAY SIZE
WIDTH, HEIGHT = 1025, 775
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guitar Key Visualizer")

#COLORS
DARKBLUE = (18, 112, 138)
BLACK = (0,0,0)
ORANGE = (237, 89, 14)

FPS = 144
GUITAR_FRETBOARD_IMAGE = pygame.image.load(
    os.path.join('GuitarKeyProgram', 'GuitarNeckBase.png'))
GUITAR_FRETBOARD_IMAGE = pygame.transform.scale(GUITAR_FRETBOARD_IMAGE, (500, 750))

def draw_window():
    WIN.fill(DARKBLUE)
    WIN.blit(GUITAR_FRETBOARD_IMAGE, (12.5,12.5))
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

    pygame.display.update()


#MAIN CODE LOOP
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