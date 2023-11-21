import random
import pygame

# Initialisierung
pygame.init()

# Screen Size
screen_size = (500, 1000)
screen = pygame.display.set_mode(screen_size)

# Highscore und Leben
highscore = 0
lives = 3 # Startanzahl der Leben
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
            rocket_position = list(pygame.mouse.get_pos())
            if rocket_position[1] > screen_size[1] - 150:
                rockets.append(rocket_position)
                rocket_fired = True
                ball_speed[0] *= 1.15
                ball_speed[1] *= 1.15

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
        rocket[1] -= 10
        if rocket[1] < 0:
            rockets.remove(rocket)
            rocket_fired = False
            lives -= 1  # Reduziere die Anzahl der Leben, wenn eine Rakete den Bildschirm verlässt
            if lives == 0:
                running = False  # Spiel beenden, wenn alle Leben verloren sind
        else:
            rocket_rect = pygame.Rect(rocket[0], rocket[1], rocket_image.get_width(), rocket_image.get_height())
            ball_rect = pygame.Rect(ball_position[0] - ball_radius, ball_position[1] - ball_radius, ball_radius * 2, ball_radius * 2)
            if rocket_rect.colliderect(ball_rect):
                rockets.remove(rocket)
                rocket_fired = False
                highscore += 1

    # Zeichne Highscore oben rechts
    highscore_text = font.render("Punkte: " + str(highscore), True, (255, 255, 255))
    screen.blit(highscore_text, (screen_size[0] - highscore_text.get_width() - 10, 10))

    # Zeichne verbleibende Leben oben links
    lives_text = font.render("Leben: " + str(lives), True, (255, 255, 255))
    screen.blit(lives_text, (10, 10))

    # Untere Wand
    pygame.draw.line(screen, (255, 255, 255), (0, screen_size[1] - 150), (screen_size[0], screen_size[1] - 150), 2)

    # Update Display
    pygame.display.flip()

    # FPS
    pygame.time.Clock().tick(60)

    # Titel
    pygame.display.set_caption("Defenders of Planet Earth")

    #Game Over
    if lives == 0:
        font_game_over = pygame.font.Font(None, 80)
        game_over_text = font_game_over.render("Game Over", True, (255, 51, 51))
        screen.blit(game_over_text, ((screen_size[0] - game_over_text.get_width()) // 2, (screen_size[1] - game_over_text.get_height()) // 2))
        pygame.display.flip()
        pygame.time.wait(5000)  
        running = False  

    
# Quit
pygame.quit()
