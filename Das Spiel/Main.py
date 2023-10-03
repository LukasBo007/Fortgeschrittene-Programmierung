#########################################################################
#                         Shoot the Moon 
#########################################################################

#Importe
import random
import pygame
 
#Initialisierung
pygame.init()

#Screen
screen = pygame.display.set_mode([400, 800])

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