import random
import pygame
from pygame import mixer

# Initialisierung
pygame.init()
# Screen Size
screen_size =width, height=(500, 1000)                                                  #Größe des Spielfensters
screen = pygame.display.set_mode(screen_size)
collision_tolerance= 10                                                                 #Kollisionstoleranz, damit der Gegner nicht in den Ufo reinbuggt, wenn zum Beispiel schräg anfliegt
#Variable für bewegenden Hintergrund
# Highscore
highscore = 0
game_over=False                                                                         #Game Over Condition für den Loop im Game
font = pygame.font.Font(None, 25)  # Schriftart und Größe für den Text
# Hintergrundbild laden
background = pygame.image.load("images/background.png").convert()                       #Hintergrundbild
background= pygame.transform.scale(background,(500,1000))                               #Größe des Hintergrundbildes anpassen  

button_img = pygame.image.load('images/restart.png')                                    #Wird noch geändert
#Background Music
mixer.music.load("sound/background.wav")                                                #Hintergrundmusik
mixer.music.set_volume(0.05)                                                            #Lautstärke der Hintergrundmusik
mixer.music.play(-1)                                                                    #Loop der Hintergrundmusik

#game over font
font_small = pygame.font.SysFont('Lucida Sans', 20)                                     #Wird noch geändert
font_big = pygame.font.SysFont('Lucida Sans', 24)                                       #Wird noch geändert
game_over_text = font.render("GAME OVER", True, (200,200,200))                          #Wird noch geändert
game_over_score= font.render('Score:'+ str(highscore), True, (255,255,255))             #Wird noch geändert


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =pygame.image.load("images/ship.png")
        self.image=pygame.transform.scale(self.image,(120,60))
        self.rect = self.image.get_rect(center=(width/2,height/2))
        self.last_shot= pygame.time.get_ticks()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

        #shoot countdown
        cooldown=1000 #milliseconds
        time_now=pygame.time.get_ticks()
        bullet_sound =mixer.Sound("sound/laser.wav")
        pygame.mixer.Sound.set_volume(bullet_sound,0.25)
        #shoot #pygame.mouse.get_pressed()[0,1,2] -> links,mausred,rechts
        if pygame.mouse.get_pressed()[0] and time_now - self.last_shot > cooldown and self.rect.top >= screen_size[1]- 150:
            bullet_sound.play()
            bullet= Rocket(self.rect.centerx, self.rect.top)
            rocket_group.add(bullet)
            self.last_shot = time_now
    
class Rocket(pygame.sprite.Sprite):
    def __init__(rocket,pos_x,pos_y):
        super().__init__()
        rocket.image =pygame.image.load("images/rocket.png")                    #Bild der Rakete
        rocket.rect=rocket.image.get_rect(center=(pos_x,pos_y))                 #Position der Rakete(Wird auf der Maus sein, center dazu, dass die Rakete mittig erscheint und nicht oben drauf )
        rocket.speed=[0,-5]                                                     #Geschinwdigkeit der Rakete (Pro Tick 5 Pixel nach oben (y))

    def update(rocket): 
        global highscore
        global game_over
        if rocket.rect.bottom < screen_size[1] -950:                            #1. Game Over Szenario (Wenn die Rakete die obere weiße Linie trifft)
            game_over=True

        if pygame.sprite.collide_rect(rocket,ally1):                             #2. Game Over Szenario (Wenn die Rakete den Verbündeten trifft)
            game_over= True

        pygame.draw.rect(screen, (255,0,0),rocket.rect,4)
        rocket.rect = rocket.rect.move(rocket.speed)

        if enemy.rect.colliderect(rocket.rect):
            collision_sound= mixer.Sound("sound/explosion.wav")                 #Explosionssound, wenn die Rakete den Gegner trifft
            pygame.mixer.Sound.set_volume(collision_sound,0.25)                 #Lautstärke vom Explosionssound annpassen
            collision_sound.play()                                              #Erhöht die X Geschwindigkeit vom Gegner um 5%
            enemy.speed[0]  *=1.05                                              #Erhöht die Y Geschwindigkeit vom Gegner um 5%
            enemy.speed[1]  *=1.05

            if rocket.rect.bottom < 200 and rocket.rect.bottom > 50:            #Wenn die Rakete den Gegner ganz oben trifft score +7
                highscore +=7
                rocket.kill()                                                   #Rocket kill = Rakete verschwindet, damit sie nicht weiter fliegt
            if enemy.rect.bottom < 499 and rocket.rect.bottom > 201:            #Wenn die Rakete den Gegner oben trifft score +5
                highscore +=5
                rocket.kill()                                                   #Rocket kill = Rakete verschwindet, damit sie nicht weiter fliegt
            if rocket.rect.bottom < 750 and rocket.rect.bottom > 500:           #Wenn die Rakete den Gegner mittig trifft score +3
                highscore +=3
                rocket.kill()                                                   #Rocket kill = Rakete verschwindet, damit sie nicht weiter fliegt
            if rocket.rect.bottom < 850 and rocket.rect.bottom > 751:           #Wenn die Rakete den Gegner unten trifft score +1
                highscore +=1
                rocket.kill()                                                   #Rocket kill = Rakete verschwindet, damit sie nicht weiter fliegt
                
        if pygame.sprite.spritecollide(rocket, freeze_group, True):
            freeze.start_freeze()
            freeze.adjust_enemy_speed(enemy)
            rocket.kill()

#108-111 Chat GPT bin verzweifelt
        split_hit_sprites = pygame.sprite.spritecollide(rocket, split_group, True)  # Check for collision with split_group and remove collided sprites
        for split in split_hit_sprites:
            ally2.kill()
            rocket.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(enemy,pos_x,pos_y):
        super().__init__()
        enemy.image = pygame.image.load("images/enemy.png")         #Bild vom Gegner
        enemy.image=pygame.transform.scale(enemy.image,(80,40))     #Größe des Bildes wird angepasst
        enemy.rect= enemy.image.get_rect(center=(pos_x,pos_y))      #Position vom Gegner
        enemy.speed = [3,3]                                         #Geschwindigkeit vom Verbündeten 1. Stelle = x Speed ; 2. Stelle = y Speed

    def update(enemy):
        enemy.rect = enemy.rect.move(enemy.speed)
        if abs(enemy.rect.left < 0 or enemy.rect.right > screen_size[0]): 
            enemy.speed [0] = -enemy.speed [0]
        if abs(enemy.rect.top -51 < 0 or enemy.rect.bottom +149> screen_size[1]): 
            enemy.speed [1] = -enemy.speed [1]

class Ally(pygame.sprite.Sprite):
    def __init__(ally,pos_x,pos_y):
        super().__init__()
        ally.image = pygame.image.load("images/ally.png")           #Bild vom Verbündeten 
        ally.image=pygame.transform.scale(ally.image,(80,40))       #Größe des Bildes wird angepasst
        ally.rect= ally.image.get_rect(center=(pos_x,pos_y))        #Poistion vom Verbündeten
        ally.speed = [2,2]                                          #Geschwindigkeit vom Verbündeten 1. Stelle = x Speed ; 2. Stelle = y Speed

    def update(ally):
        ally.rect = ally.rect.move(ally.speed)
        if abs(ally.rect.left < 0 or ally.rect.right > screen_size[0]):     #Wenn der Verbündete Links oder Rechts abprallt, dann wird er von der Wand abprallen
            ally.speed [0] = -ally.speed [0]
        if abs(ally.rect.top -51 < 0 or ally.rect.bottom +149> screen_size[1]): #Wenn der Verbündete Oben oder Unten abprallt, dann wird er von der Wand abprallen
            ally.speed [1] = -ally.speed [1]

class Button():
	def __init__(self, x, y):
		self.image = pygame.image.load('images/restart.png')        #Bild vom Knopf 
		self.rect = self.image.get_rect()                           #Knopf in ein Rect machen (zum anklicken)
		self.rect.topleft = (x, y)                                  #Koordinaten vom Knopf

	def draw(self):

		#draw button
		screen.blit(self.image, (self.rect.x, self.rect.y))

class Freeze(pygame.sprite.Sprite):
    def __init__(freeze,x,y,filename):
          super().__init__()
          freeze.image=pygame.image.load(filename)
          freeze.image=pygame.transform.scale(freeze.image,(80,40))   
          freeze.rect=freeze.image.get_rect(center=(x,y))
          freeze.rect.topleft=(x,y)
          freeze.start_time=0
          freeze.duration = 5000
          freeze.is_hit=False
    
    def start_freeze(freeze):
         freeze.start_time= pygame.time.get_ticks()

    def adjust_enemy_speed(freeze, enemy:Enemy):
        elapsed_time = pygame.time.get_ticks() - freeze.start_time
        if elapsed_time < freeze.duration:
            # Adjust the enemy's speed as needed
            enemy.speed[0] *= 0.5  # Reduce X speed by 50%
            enemy.speed[1] *= 0.5  # Reduce Y speed by 50%
        else:
            # Freeze effect is over, double the enemy's speed
            enemy.speed[0] *= 2  # Double X speed
            enemy.speed[1] *= 2  # Double Y speed
class Split(pygame.sprite.Sprite):
    def __init__(split,x,y,filename):
         super().__init__()
         split.image=pygame.image.load(filename)
         split.image=pygame.transform.scale(split.image,(80,40))   
         split.rect=split.image.get_rect(center=(x,y))
         split.rect.topleft=(x,y)

#Collision Funktion, damit main Loop schöner aussieht
def check_collision():
        # collision detection
    if enemy.rect.colliderect(ally1.rect):       #Funktion wenn Gegner und Verbündeter zusammenstoßen, dass sie voneinander abprallen
            if  abs(ally1.rect.top - enemy.rect.bottom) < collision_tolerance and enemy.speed[1] >0:    
                enemy.speed[1] *= -1
            if abs(ally1.rect.bottom - enemy.rect.top) < collision_tolerance and enemy.speed[1] <0:
                enemy.speed[1] *= -1
            if abs(ally1.rect.right - enemy.rect.left) < collision_tolerance and enemy.speed[0] <0:
                enemy.speed[0] *= -1
            if abs(ally1.rect.left - enemy.rect.right) < collision_tolerance and enemy.speed[0] >0:
                enemy.speed[0] *= -1             
            pygame.draw.rect(screen, (255,0,0),ally1.rect,4)     #Testweise Roter Kasten um Verbündeten wird gelöscht
def deco():
             #Untere graue Box
        screen.fill((63, 71, 84), (0, screen_size[1] - 149, screen_size[0], 149))
        #Obere graue Box
        screen.fill((63, 71, 84), (0, screen_size[1] - 1000, screen_size[0], 51))
        # Untere Wand
        pygame.draw.line(screen, (255, 255, 255), (0, screen_size[1] - 150), (screen_size[0], screen_size[1] - 150), 2)
        #Obere Wand
        pygame.draw.line(screen, (255, 255, 255), (0, screen_size[1] - 950), (screen_size[0], screen_size[1] - 950), 2)

def bg_loop():
    i = 0
    screen.blit(background, (0, i))
    screen.blit(background, (0,height+i))
    i-=1
    if i == -height:
        screen.blit(background, ( 0,height+i))
        i=0 
#Maus unsichtbar machen 
pygame.mouse.set_visible(False)

#Gegnerisches Ufo auf position 100,200 erscheinen lassen
enemy=Enemy(100,400)
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)
#Verbündeten auf position 200,750 erscheinen lassen
all_allies = pygame.sprite.Group()
ally1=Ally(400,100)
all_allies.add(ally1)

#Spieler(Maus/Raumschiff,welches Raketen feuert auf der laden)
player=Player()
player_group = pygame.sprite.Group()
player_group.add(player)
#Spieler(Maus/Raumschiff,welches Raketen feuert auf der laden)
pos=pygame.mouse.get_pos()
rocket=Rocket(pos[0],pos[1])
rocket_group=pygame.sprite.Group()
#Knopf zum restarten des Spiels erstellen
button = Button(screen_size[0] // 2 - 50, screen_size[1] // 2 - 100)
#####Freeze
freeze=Freeze(100,80, "images/Freeze.png")
freeze_group= pygame.sprite.Group()
freeze_group.add(freeze)

split_group=pygame.sprite.Group()
split= Split(300,700,"images/cursor.jpg")
split_group.add(split)

ally2= None

# Game Loop
running = True
while running:

    pygame.time.Clock().tick(60)    
    bg_loop()
            # Hintergrundbild zeichnen + bewegen


    # Hauptteil           
    if game_over==False:
        if highscore >1 and ally2 is None: #ally 2 is none von ChatGPT
            ally2=Ally(100,500)
            all_allies.add(ally2)

        check_collision()
        deco()

        player_group.update()     
        enemy_group.update()
        rocket_group.update() 
        split_group.update()
        all_allies.update()
        freeze_group.update() 
        split_group.draw(screen)      
        player_group.draw(screen)
        enemy_group.draw(screen)
        rocket_group.draw(screen)
        all_allies.draw(screen)
        freeze_group.draw(screen)  

        # Zeichne Highscore oben rechts
        highscore_text = font.render("Punkte: " + str(highscore), True, (255, 255, 255))
        screen.blit(highscore_text, (screen_size[0] - highscore_text.get_width() - 10, 10))
    # Titel
        pygame.display.set_caption("Defenders of Planet Earth")
    else:  #Game Over = True Funktion 
            screen.fill((0,0,0))       #Schwarzer Bildschirm             
            button.draw()              #Restart Knopf erscheinen lassen         
            pygame.mouse.set_visible(True)  #Maus sichtbar machen zum klicken (Restart oder Quit)
            screen.blit(game_over_text, (screen_size[0]/2 - (game_over_text.get_width()/2), screen_size[1]/2 - game_over_text.get_height()/2))  #Game Over Text anzeigen lassen
            screen.blit(highscore_text, (screen_size[0]/2 - (game_over_score.get_width()/3), screen_size[1] - game_over_score.get_height()-200))    #Score im akutellen Run anzeigen lassen
            pygame.mixer.music.set_volume(0)    #Musik ausmachen

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.flip()
# Quit
pygame.quit()
#Collission tolerance mit decke und boden sonst buggt manchmkal evtl rein