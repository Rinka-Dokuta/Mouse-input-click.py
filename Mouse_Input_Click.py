import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1200,800)) #screen is a rectangle, not square!
pygame.display.set_caption("fish mouse imput")

#mouse input
xpos = 0
ypos = 0
mousePos = (xpos, ypos)

background = 1

fishieXpos = []
fishieYpos = []

bobXpos = []
bobYpos = []

patXpos = []
patYpos = []

#load images
castleImg = pygame.image.load("castle.png").convert_alpha()
pygame.Surface.set_colorkey (castleImg, [255,255,255])
castleImg2 = pygame.image.load("castle2.png").convert_alpha()
pygame.Surface.set_colorkey (castleImg2, [255,255,255])

plantImg = pygame.image.load("plants.png").convert_alpha()
pygame.Surface.set_colorkey (plantImg, [255,255,255])
plantImg2 = pygame.image.load("plants2.png").convert_alpha()
pygame.Surface.set_colorkey (plantImg2, [255,255,255])

fishImg = pygame.image.load("fish.png").convert_alpha()
pygame.Surface.set_colorkey (fishImg, [255,0,255])

spongyboy =  pygame.image.load("spongyboy.png").convert_alpha()
pygame.Surface.set_colorkey (spongyboy, [255,0,255])

thestar =  pygame.image.load("thestar.png").convert_alpha()
pygame.Surface.set_colorkey (thestar, [255,0,255])

Spongebob = pygame.image.load("Spongebob.png").convert_alpha()
pygame.Surface.set_colorkey (Spongebob, [255,255,255])
Spongebob2 = pygame.image.load("Spongebob2.png").convert_alpha()
pygame.Surface.set_colorkey (Spongebob2, [255,255,255])

while 1: #game loop###########################################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        print(mousePos) #this is to help you know where to set these boundaries
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            #background selection
            if mousePos[0]>1000 and mousePos[0] < 1200 and mousePos[1]>50 and mousePos[1]<225:
               background = 1 #castle
            elif mousePos[0]>1000 and mousePos[0] < 1200 and mousePos[1]>225 and mousePos[1]<425:
                background = 2 #plants
            elif mousePos[0]>1000 and mousePos[0] < 1200 and mousePos[1]>600 and mousePos[1]<800:
                background = 3 #Spongebob
                
                
            #fish selection
            elif mousePos[0]>25 and mousePos[0] < 200 and mousePos[1]>50 and mousePos[1]<150:
               fishieXpos.append(random.randrange(250, 900))
               fishieYpos.append(random.randrange(50,750))
            elif mousePos[0]>25 and mousePos[0] < 200 and mousePos[1]>400 and mousePos[1]<800:
               bobXpos.append(random.randrange(250, 900))
               bobYpos.append(random.randrange(50,750))
            elif mousePos[0]>25 and mousePos[0] < 200 and mousePos[1]>132 and mousePos[1]<332:
               patXpos.append(random.randrange(250, 900))
               patYpos.append(random.randrange(50,750))
         
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos        
    

    #render section------------------------------
    
    screen.fill((0,0,0))# Clear the screen

    #fill in "water" for tank
    pygame.draw.rect(screen, (100, 100, 200), (200, 0, 800, 800)) #make sure you know what these numbers do!

    #draw the lines on the screen
    pygame.draw.line(screen, (255,255,255), (200, 0), (200, 800), 2) #make sure you know what these numbers do!
    pygame.draw.line(screen, (255,255,255), (1000, 0), (1000, 800), 2)
    
    #draw background image
    if background == 1:
        screen.blit(castleImg, (240, 140))
    elif background ==2: 
        screen.blit(plantImg, (240, 140))
    elif background ==3:
        screen.blit(Spongebob, (240, 140))
    
    #draw fishies!
    
    for i in range(len(patXpos)):
        screen.blit(thestar, (patXpos[i], patYpos[i]))
    for i in range(len(bobXpos)):
        screen.blit(spongyboy, (bobXpos[i], bobYpos[i]))
    for i in range(len(fishieXpos)):
        screen.blit(fishImg, (fishieXpos[i], fishieYpos[i]))
        
    #show sidebar images
    screen.blit(castleImg2, (1000, 50))
    screen.blit(plantImg2, (1010, 250))
    screen.blit(fishImg, (50, 50))
    screen.blit(Spongebob, (994, 645))
    screen.blit(thestar,(50, 150))
    screen.blit(spongyboy,(50, 400))
    
    pygame.display.flip()# Update the display

#end of game loop###################################################################
pygame.quit()
