import random
import pygame


# Initialisierung
pygame.init()

# Screen Size
screen_size =width, height=(500, 1000)
screen = pygame.display.set_mode(screen_size)

#Variable für bewegenden Hintergrund
i= 0

# Hintergrundbild laden
background = pygame.image.load("Images\space2.jpg").convert()

# Raumschiff (gerade noch Ball)
ball_radius = 25
ball_color = (255, 255, 204)
ball_position = [200, 400]
ball_speed = [3, 3]

# Game Loop
running = True
while running:
    # Hauptteil
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Hintergrundbild zeichnen + bewegen
    screen.blit(background, (0, i))
    screen.blit(background, (0,height+i))
    i -= 1
    if i == -height:
       screen.blit(background, ( 0,height+i))
       i= 0


    # Update ball position
    ball_position[0] += ball_speed[0]
    ball_position[1] += ball_speed[1]

    # Bounce off the walls
    if ball_position[0] - ball_radius < 0 or ball_position[0] + ball_radius > screen_size[0]:
        ball_speed[0] *= -1

    if ball_position[1] - ball_radius < 0 or ball_position[1] + ball_radius > screen_size[1] - 150:
        ball_speed[1] *= -1

    # Draw Ball      
    pygame.draw.circle(screen, ball_color, (int(ball_position[0]), int(ball_position[1])), ball_radius)

    # Untere Wand
    pygame.draw.line(screen, (255, 255, 255), (0, screen_size[1] - 150), (screen_size[0], screen_size[1] - 150), 2)
    #screen.fill((63, 71, 84), (0, screen_size[1] - 149, screen_size[0], 149))

    #Bewegender Hintergrund

    # Update Display
    pygame.display.flip()

    # FPS
    pygame.time.Clock().tick(60)

    # Titel
    pygame.display.set_caption("Defenders of Planet Earth")
    
# Quit
pygame.quit()
