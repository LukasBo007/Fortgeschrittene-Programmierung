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
#background= pygame.transform.scale(background,(500,1000))



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =pygame.image.load("images/ship.png")
        self.image=pygame.transform.scale(self.image,(120,60))
        self.rect = self.image.get_rect(center=(width/2,height/2))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
    
    def create_bullet(self):
            return Bullet(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
    
class Bullet(pygame.sprite.Sprite):
        def __init__(self,pos_x,pos_y):
                super().__init__()
                self.image =pygame.image.load("images/rocket.png")
                self.rect=self.image.get_rect(center=(pos_x,pos_y))
        
        def update(self):
            self.rect.y-=5
          

# Raumschiff (gerade noch Ball)
enemy = pygame.image.load("images/enemy.png")
enemy= pygame.transform.scale(enemy,(80,40))
enemy_speed = [3, 3]
enemy_rect= enemy.get_rect(topleft= [200,400])

ally = pygame.image.load("images/ally.png")
ally= pygame.transform.scale(ally,(80,40))
ally_speed = [2, 2]
ally_rect= enemy.get_rect(topleft= [200,750])



#Maus unsichtbar machen 
pygame.mouse.set_visible(False)

player=Player()
player_group = pygame.sprite.Group()
player_group.add(player)


bullet_group= pygame.sprite.Group()

# Highscore
highscore = 0
font = pygame.font.Font(None, 25)  # Schriftart und Größe für den Text



# Game Loop
running = True
while running:
    # Hauptteil
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.create_bullet())

    # Hintergrundbild zeichnen + bewegen
    screen.blit(background, (0, i))
    screen.blit(background, (0,height+i))
    i -= 1
    if i == -height:
       screen.blit(background, ( 0,height+i))
       i= 0

    enemy_rect = enemy_rect.move(enemy_speed)
    if enemy_rect.left < 0 or enemy_rect.right > screen_size[0]: 
        enemy_speed [0] = -enemy_speed [0]
    if enemy_rect.top -51 < 0 or enemy_rect.bottom +149> screen_size[1]:
        enemy_speed [1] = -enemy_speed [1]

    ally_rect = ally_rect.move(ally_speed)
    if ally_rect.left < 0 or ally_rect.right > screen_size[0]: 
        ally_speed [0] = -ally_speed [0]
    if ally_rect.top -51 < 0 or ally_rect.bottom +149> screen_size[1]:
        ally_speed [1] = -ally_speed [1]

    # collision detection
    collision_tolerance= 10
    if enemy_rect.colliderect(ally_rect):
        if  abs(ally_rect.top - enemy_rect.bottom) < collision_tolerance and enemy_speed[1] >0:
            enemy_speed[1] *= -1
        if abs(ally_rect.bottom - enemy_rect.top) < collision_tolerance and enemy_speed[1] <0:
             enemy_speed[1] *= -1
        if abs(ally_rect.right - enemy_rect.left) < collision_tolerance and enemy_speed[0] <0:
             enemy_speed[0] *= -1
        if abs(ally_rect.left - enemy_rect.right) < collision_tolerance and enemy_speed[0] >0:
             enemy_speed[0] *= -1             
        pygame.draw.rect(screen, (255,0,0),ally_rect,4)


    # Draw Ball      
    #pygame.draw.circle(screen, ball_color, (int(ball_position[0]), int(ball_position[1])), enemyl_radius)

    # Untere Wand
    pygame.draw.line(screen, (255, 255, 255), (0, screen_size[1] - 150), (screen_size[0], screen_size[1] - 150), 2)

    #obere wand
    pygame.draw.line(screen, (255, 255, 255), (0, screen_size[1] - 950), (screen_size[0], screen_size[1] - 950), 2)

    screen.fill((63, 71, 84), (0, screen_size[1] - 149, screen_size[0], 149))
    screen.fill((63, 71, 84), (0, screen_size[1] - 1000, screen_size[0], 51))

    # Zeichne Highscore oben rechts
    highscore_text = font.render("Punkte: " + str(highscore), True, (255, 255, 255))
    screen.blit(highscore_text, (screen_size[0] - highscore_text.get_width() - 10, 10))

    # Update Display
    screen.blit(enemy,enemy_rect)
    screen.blit(ally,ally_rect)
    bullet_group.draw(screen)
    player_group.draw(screen)
    player_group.update()
    bullet_group.update()
    pygame.display.flip()


    # FPS
    pygame.time.Clock().tick(60)

    # Titel
    pygame.display.set_caption("Defenders of Planet Earth")
    
# Quit
pygame.quit()
