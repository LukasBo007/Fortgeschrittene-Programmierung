#########################################################################
#                         Shoot the Moon 
#########################################################################

#Importe
import random
import pygame
 
#Initialisierung
pygame.init()

#Screen
screen = pygame.display.set_mode([700,1000])
#Hintergrundbild
bg = pygame.image.load

pygame.mouse.set_visible(0)

# Run 
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((43, 51, 64))

    pygame.draw.circle(screen, (204, 188, 122), (200, 400), 100)

    pygame.display.flip()

#Quit
pygame.quit()