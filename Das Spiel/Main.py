#########################################################################
#                         Shoot the Moon 
#########################################################################

#Importe
import random
import pygame
 
#Initialisierung
pygame.init()

#Screen
screen = pygame.display.set_mode([915,515])
#Hintergrundbild
background = pygame.image.load("images/Background.jpg")

#Anpassen vom Hintergrund an die Größe des Fensters
background = pygame.transform.scale(background, (915,515))



pygame.mouse.set_visible(0)

# Run 
running = True
while running:

    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    pygame.draw.circle(screen, (204, 188, 122), (200, 400), 100)

    pygame.display.flip()

#Quit
pygame.quit()