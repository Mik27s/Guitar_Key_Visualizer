#Guitar Key Visualizer Code
import pygame
from pygame.locals import *
import os
from Button import Button
from GuitarKeyProgram.Tab import Tab
from Note import Note
from Key import Key
from Fret import Fret
from String import String

#A major: [A,B,Cs,D,E,Fs,Gs]
#As major: [As,C,D,Ds,F,Fs,A]
#B major: [B,Cs,Ds,E,Fs,Gs,As]
#C major: [C,D,E,F,G,A,B]
#Cs major: [Cs,Ds,Es,Fs,Gs,As,Bs]
#D major: [D,E,Fs,G,A,B,Cs]
#Ds major: [Ds,F,G,Gs,As,C,D]
#E major: [E,Fs,Gs,A,B,Cs,Ds]
#F major: [F,G,A,As,C,D,E]
#Fs major: [Fs,Gs,As,B,Cs,Ds,F]
#G major: [G,A,B,C,D,E,Fs]
#Gs major: [Gs,As,Bs,Cs,Ds,Es,G]
pygame.init()
Buttons = []
Frets = []
Strings = []

#All E
#0-12
eE0 = Tab(6,0,"e")
eE12 = Tab(6,12,"e")
ea7 = Tab(5,7,"e")
ed2 = Tab(4,2,"e")
eg9 = Tab(3,9,"e")
eb5 = Tab(2,5,"e")
ee0 = Tab(1,0,"e")
ee12 = Tab(1,12,"e")
#13-23
ea19 = Tab(6,19,"e")
ed14 = Tab(4,14,"e")
eg21 = Tab(3,21,"e")
eb17 = Tab(2,17,"e")
e = Note("e", [eE0,eE12,ea7,ed2,eg9,eb5,ee0,ee12,ea19,ed14,eg21,eb17])

#All F
#0-12
fE1 = Tab(6,1,"f")
fa8 = Tab(5,8,"f")
fd3 = Tab(4,3,"f")
fg10 = Tab(3,10,"f")
fb6 = Tab(2,6,"f")
fe1 = Tab(1,1,"f")
#13-23
fE13 = Tab(6,13,"f")
fa20 = Tab(5,20,"f")
fd15 = Tab(4,15,"f")
fg22 = Tab(3,22,"f")
fb18 = Tab(2,18,"f")
fe13 = Tab(1,13,"f")
f = Note("f", [fE1,fa8,fd3,fg10,fb6,fe1,fE13,fa20,fd15,fg22,fb18,fe13])

#All F#
#0-12
fsE2 = Tab(6,2,"f#")
fsa9 = Tab(5,9,"f#")
fsd4 = Tab(4,4,"f#")
fsg11 = Tab(3,11,"f#")
fsb7 = Tab(2,7,"f#")
fse2 = Tab(1,2,"f#")
#13-23
fsE14 = Tab(6,14,"f#")
fsa21 = Tab(5,21,"f#")
fsd16 = Tab(4,16,"f#")
fsg23 = Tab(3,23,"f#")
fsb19 = Tab(2,19,"f#")
fse14 = Tab(1,14,"f#")

#All G
#0-12
gE3 = Tab(6,3,"g")
ga10 = Tab(5,10,"g")
gd5 = Tab(4,5,"g")
gg12 = Tab(3,12,"g")
gb8 = Tab(2,8,"g")
ge3 = Tab(1,3,"g")
#13-23
gE15 = Tab(6,15,"g")
ga22 = Tab(5,22,"g")
gd17 = Tab(4,17,"g")
gb20 = Tab(2,20,"g")
ge15 = Tab(1,15,"g")

#All G
#0-12
gE4 = Tab(6,3,"g#")
ga11 = Tab(5,11,"g#")
gd6 = Tab(4,6,"g#")
gg1 = Tab(3,1,"g#")
gb9 = Tab(2,9,"g#")
ge4 = Tab(1,4,"g#")
#13-23
gE16 = Tab(6,16,"g#")
ga23 = Tab(5,23,"g#")
gd18 = Tab(4,18,"g#")
gg13 = Tab(3,13,"g#")
gb21 = Tab(2,21,"g#")
ge16 = Tab(1,16,"g#")

#All A
#0-12
aE4 = Tab(6,5,"a")
aa0 = Tab(5,0,"a")
aa12 = Tab(5,12,"a")
ad7 = Tab(4,7,"a")
ag2 = Tab(3,2,"a")
ab10 = Tab(2,10,"a")
ae5 = Tab(1,5,"a")
#13-23
aE17 = Tab(6,17,"a")
ad19 = Tab(4,19,"a")
ag14 = Tab(3,14,"a")
ab22 = Tab(2,22,"a")
ae17 = Tab(1,17,"a")

#All A#
#0-12
asE6 = Tab(6,6,"a#")
asa1 = Tab(5,1,"a#")
asd8 = Tab(4,8,"a#")
asg3 = Tab(3,3,"a#")
asb11 = Tab(2,11,"a#")
ase6 = Tab(1,6,"a#")
#13-23
asE18 = Tab(6,18,"a#")
asa13 = Tab(5,13,"a#")
asd20 = Tab(4,20,"a#")
asg15 = Tab(3,15,"a#")
asb23 = Tab(2,23,"a#")
ase18 = Tab(1,18,"a#")

#All B
#0-12
bE7 = Tab(6,7,"b")
ba2 = Tab(5,2,"b")
bd9 = Tab(4,9,"b")
bg4 = Tab(3,4,"b")
bb0 = Tab(2,0,"b")
bb12 = Tab(2,12,"b")
be7 = Tab(1,7,"b")
#13-23
bE19 = Tab(6,19,"b")
ba14 = Tab(5,14,"b")
bd21 = Tab(4,21,"b")
bg17 = Tab(3,17,"b")
be19 = Tab(1,19,"b")

#All C
#0-12
cE8 = Tab(6,8,"c")
ca3 = Tab(5,3,"c")
cd10 = Tab(4,10,"c")
cg5 = Tab(3,5,"c")
cb1 = Tab(2,1,"c")
ce8 = Tab(1,8,"c")
#13-23
cE20 = Tab(6,20,"c")
ca15 = Tab(5,15,"c")
cd22 = Tab(4,22,"c")
cg17 = Tab(3,17,"c")
cb13 = Tab(2,13,"c")
ce20 = Tab(1,20,"c")

#All C
#0-12
csE9 = Tab(6,9,"c#")
csa4 = Tab(5,4,"c#")
csd11 = Tab(4,11,"c#")
csg6 = Tab(3,6,"c#")
csb2 = Tab(2,2,"c#")
cse9 = Tab(1,9,"c#")
#13-23
csE21 = Tab(6,21,"c#")
csa16 = Tab(5,16,"c#")
csd23 = Tab(4,23,"c#")
csg18 = Tab(3,18,"c#")
csb14 = Tab(2,14,"c#")
cse21 = Tab(1,21,"c#")

#All D
#0-12
dE10 = Tab(6,10,"d")
da5 = Tab(5,5,"d")
dd0 = Tab(4,0,"d")
dd12 = Tab(4,12,"d")
dg7 = Tab(3,7,"d")
db3 = Tab(2,3,"d")
de10 = Tab(1,10,"d")
#13-23
dE22 = Tab(6,22,"d")
da17 = Tab(4,17,"d")
dg19 = Tab(3,19,"d")
db15 = Tab(2,15,"d")
de22 = Tab(1,22,"d")

#All D#
#0-12
dsE11 = Tab(6,11,"d#")
dsa6 = Tab(5,6,"d#")
dsd1 = Tab(4,1,"d#")
dsg8 = Tab(3,8,"d#")
dsb4 = Tab(2,4,"d#")
dse11 = Tab(1,11,"d#")
#13-23
dsE23 = Tab(6,23,"d#")
dsa18 = Tab(5,18,"d#")
dsd13 = Tab(4,13,"d#")
dsg20 = Tab(3,20,"d#")
dsb16 = Tab(2,16,"d#")
dse23 = Tab(1,23,"d#")


E = Key("E", [e,fs])
keys = [E,F,...]

for k in keys:
    Buttons.append(Button(0,0,k.name, k.draw))






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


#Frets
for i in range(0, 24):
    Frets.append(Fret(i))

#Strings
for n,i in ["E","A","D","G","B","e"]:
    Strings.append(String(n,i + 1))

def draw_window(Buttons, Frets, Strings):
    WIN.fill(DARKBLUE)
    #WIN.blit(GUITAR_FRETBOARD_IMAGE, (12.5,12.5))
    #Draw Background
    pygame.draw.rect(WIN, (LIGHTYELLOW), (8, 8, 500, 750))
    for B in Buttons:
        B.draw(WIN)

    for F in Frets:
        F.draw(WIN)

    for S in Strings:
        S.draw(WIN)


    PLUSINDEX = 250
    FRETFONT = pygame.font.SysFont("palatino", 35)
    TITLEFONT = pygame.font.SysFont("Goudy Stout", 18)
    KEYSELECTFONT = pygame.font.SysFont("palatino", 100)
    

    #Dot Inlays
    for x in range(170 ,600, 120):
        pygame.draw.circle(WIN, (BLACK), (152, x), 8)

    for x in range (122, 200, 55):
        pygame.draw.circle(WIN, (BLACK), (x, 710), 8)

    #Dot Inlays
    for x in range(170 ,600, 120):
        pygame.draw.circle(WIN, (BLACK), (152 + PLUSINDEX, x + 60), 8)

    for x in range(373 ,452, 55):
        pygame.draw.circle(WIN, (BLACK), (x, 52), 8)


    #Textboxes for frets
    numArray = ["1","2","3","4","5","6","7","8","9","10","11","12"]
    numArray3 = ["12","13","14","15","16","17","18","19","20","21","22","23"]
    COUNT = 0


    for y in range(40, 720, 60):
        label = FRETFONT.render(numArray[COUNT], 1, (0,0,0))
        text_rect = label.get_rect()
        text_rect.right = 60
        text_rect.top = y
        WIN.blit(label, text_rect)
        COUNT += 1

    COUNT = 0
    for x in range(40, 725, 60):
        label = FRETFONT.render(numArray3[COUNT], 1, (0,0,0))
        WIN.blit(label, (35 + PLUSINDEX, x))
        COUNT += 1


    
    ###-----------------------------------------------------------------------------------------------------------
    
    #GAME TEXT and BUTTON BOXES
    COUNT = 0
    KeyNameArray = ["A","C#","F","A#","D","F#","B","D#","G","C","E","G#"]
    for x in range(535, 1055, 130):
        for y in range(80, 470, 130):
            Buttons.append(Button(x,y,KeyNameArray[COUNT]))
            COUNT += 1
            
    COUNT = 0
    pygame.draw.rect(WIN, BLACK, (545, 15, 450, 45))
    pygame.draw.rect(WIN, LIGHTYELLOW, (550, 20, 450, 45))
    label = TITLEFONT.render("Guitar Key Visualizer", 1 , BLACK)
    WIN.blit(label, (557, 25))
    COUNT = 0

    pygame.draw.rect(WIN, BLACK, (670, 465, 207, 80))
    Button = pygame.draw.rect(WIN, LIGHTYELLOW, (675, 470, 207, 80))
    Buttons.append(Button)
    label = KEYSELECTFONT.render("Reset", 1, (0,0,0) )
    WIN.blit(label, (685, 475))

    #Cursor
    MX, MY = pygame.mouse.get_pos()
    #print(MX, MY)
    
    WIN.blit(pygame.transform.rotate(CHICKEN, 0), 
    (MX + CENTERED[0], MY + CENTERED[1]))

    pygame.mouse.get_pos(1)
    pygame.mouse.set_visible(0)

    pygame.display.update()

    ###-----------------------------------------------------------------------------------------------------------


#MAIN CODE LOOP
def main():
    left_click = False
    clock = pygame.time.Clock()
    run = True
    Buttons = []
    while run:
        clock.tick(FPS)
        draw_window(Buttons)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0] == 1 and left_click == False:
                left_click = True
                for B in Buttons:
                    if B.collidepoint(pygame.mouse.get_pos()):
                        print("clicked")
            if pygame.mouse.get_pressed()[0] == 0:
                left_click = False  
            
        

    pygame.quit()

if __name__ == "__main__":
    main()

#OLD CODE STORAGE
