#gopher mash
#written by Dr. Mo, 11/10/2020
import pygame
import math #needed for square root function

pygame.init()#initializes Pygame
print(pygame.font.get_fonts())
pygame.display.set_caption("Cookie Clicker")#sets the window title
screen = pygame.display.set_mode((400,400))#creates game screen

print(pygame.font.get_fonts())
#player variables
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
numClicks = 0
isBig = False
#circle variables: circX and circY are the coordinates of the center (where it's drawn), and the radius is how big it is
circX = 188
circY = 187
radius = 100

CookiePic = pygame.image.load("cookie.png")
CookieRect = CookiePic.get_rect(topleft=(-35,10))

CookiePic2 = pygame.image.load ("cookie2.png")
CookieRect2 = CookiePic2.get_rect(topleft=(-15,10))

font = pygame.font.Font('freesansbold.ttf', 32)
text1 = font.render('score:', False, (0, 200, 200))
text2 = font.render(str(int(numClicks)), 1, (0, 200, 200))

#gameloop###################################################
while True:
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()

    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN: #check if clicked
        if math.sqrt((mousePos[0]-circX)**2+(mousePos[1]-circY)**2)<radius:
              numClicks+=1
              isBig = True
        print("CLICK")
    else:
        isBig = False 
    if event.type == pygame.MOUSEMOTION: #check if mouse moved
        mousePos = event.pos #refreshes mouse position
        print("mouse position: (",mousePos[0]," , ",mousePos[1], ")")
 
#render section---------------------------------------------
    screen.fill((255, 255, 255)) #wipe screen (without this, things smear)
    
    pygame.draw.circle(screen, (200, 0, 200), (circX,circY), radius)
    print("clicks:", numClicks) #uncomment this once collision is set up
    if isBig == False: 
        screen.blit(CookiePic, CookieRect)
    else:
        screen.blit(CookiePic2, CookieRect2)
    text2 = font.render(str(int(numClicks)), 1, (0, 200, 200))
    screen.blit(text1, (10, 10))
    screen. blit(text2, (110, 10))
        
    pygame.display.flip()
    

#end game loop##############################################

pygame.quit()




