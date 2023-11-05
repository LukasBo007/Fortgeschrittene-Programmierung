#########################################################################
#                      Defenders of Planet Earth 
#########################################################################

#Importe
import random
import pygame
import sys

 
#Initialisierung
pygame.init()

#Screen Size
screen_size = (500, 1000)
screen = pygame.display.set_mode(screen_size)
        
# Hintergrundbild laden
background = pygame.image.load("Images\starfield.png").convert()        

#Raumschiff (gerade noch Ball)
ball_radius = 20
ball_color = (255, 0, 0)
ball_position = [200, 400]
ball_speed = [3, 3]

# Highscore
highscore = 0
font = pygame.font.Font(None, 25)  # Schriftart und Größe für den Text


#Game Loop
running = True
while running:
    #Hauptteil
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Hintergrundfarbe (Nachher png)
    screen.fill((43, 51, 64))

    #Update ball position
    ball_position[0] += ball_speed[0]
    ball_position[1] += ball_speed[1]

    # Bounce off the walls
    if ball_position[0] - ball_radius < 0 or ball_position[0] + ball_radius > screen_size[0]:
        ball_speed[0] *= -1

    if ball_position[1] - ball_radius < 0 or ball_position[1] + ball_radius > screen_size[1] - 150: #150 Pixel über der unteren Wand
        ball_speed[1] *= -1

    #Draw Ball      
    pygame.draw.circle(screen, ball_color, (int(ball_position[0]), int(ball_position[1])), ball_radius)

    #Untere Wand
    pygame.draw.line(screen, (255, 255, 255), (0, screen_size[1] - 150), (screen_size[0], screen_size[1] - 150), 2)
    screen.fill((63, 71, 84), (0, screen_size[1] - 149, screen_size[0], 149))

    # Zeichne Highscore oben rechts
    highscore_text = font.render("Punkte: " + str(highscore), True, (255, 255, 255))
    screen.blit(highscore_text, (screen_size[0] - highscore_text.get_width() - 10, 10))

    #Update Display
    pygame.display.flip()

    #FPS
    pygame.time.Clock().tick(60)

    #Titel
    pygame.display.set_caption("Defenders of Planet Earth")
    
#Quit
pygame.quit()
