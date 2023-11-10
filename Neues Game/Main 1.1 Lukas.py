import random
import pygame


# Initialisierung
pygame.init()

# Screen Size
screen_size = (500, 1000)
screen = pygame.display.set_mode(screen_size)

# Highscore
highscore = 0
font = pygame.font.Font(None, 30)  # Schriftart und Größe für den Text

# Hintergrundbild laden
background = pygame.image.load("Images\space2.jpg").convert()

# Raumschiff (gerade noch Ball)
ball_radius = 50
ball_color = (255, 255, 204)
ball_position = [200, 400]
ball_speed = [3, 3]

# Liste für Raketen erstellen
rockets = []
rocket_fired = False
rocket_image = pygame.image.load("Images\Missiles\spaceMissiles_006.png")  # Passe den Dateipfad entsprechend an
rocket_image = pygame.transform.scale(rocket_image, (20, 40))  # Passe die Größe des Bildes an

running = True
while running:
    # Hauptteil
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not rocket_fired:
            # Wenn Maustaste 1 (links) gedrückt wird, keine Rakete abgefeuert wurde und die Y-Position der Rakete unterhalb der Linie liegt
            rocket_position = list(pygame.mouse.get_pos())  # Mausposition abrufen
            if rocket_position[1] > screen_size[1] - 150:  # Überprüfen, ob die Rakete unterhalb der Linie ist
                rockets.append(rocket_position)
                rocket_fired = True  # Rakete wurde abgefeuert
                # Ballgeschwindigkeit erhöhen, wenn die Rakete abgefeuert wird
                ball_speed[0] *= 1.15  # Erhöhe die x-Geschwindigkeit des Balls um 15%
                ball_speed[1] *= 1.15  # Erhöhe die y-Geschwindigkeit des Balls um 15%
        
        

    # Hintergrundbild zeichnen
    screen.blit(background, (0, 0))

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

    # Draw Rockets
    for rocket in rockets:
        screen.blit(rocket_image, (rocket[0], rocket[1]))
        rocket[1] -= 10  # Geschwindigkeit der Rakete nach oben
        if rocket[1] < 0:
            rockets.remove(rocket)
            rocket_fired = False
        else:
            # Kollisionserkennung mit dem Ball
            rocket_rect = pygame.Rect(rocket[0], rocket[1], rocket_image.get_width(), rocket_image.get_height())
            ball_rect = pygame.Rect(ball_position[0] - ball_radius, ball_position[1] - ball_radius, ball_radius * 2, ball_radius * 2)
            if rocket_rect.colliderect(ball_rect):
                rockets.remove(rocket)
                rocket_fired = False
                highscore += 1  # Erhöhe den Highscore, wenn die Rakete den Ball trifft

    
    # Zeichne Highscore oben rechts
    highscore_text = font.render("Punkte: " + str(highscore), True, (255, 255, 255))
    screen.blit(highscore_text, (screen_size[0] - highscore_text.get_width() - 10, 10))

    # Untere Wand
    pygame.draw.line(screen, (255, 255, 255), (0, screen_size[1] - 150), (screen_size[0], screen_size[1] - 150), 2)

    # Update Display
    pygame.display.flip()

    # FPS
    pygame.time.Clock().tick(60)

    # Titel
    pygame.display.set_caption("Defenders of Planet Earth")
    
# Quit
pygame.quit()