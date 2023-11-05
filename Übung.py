
import sys, pygame
pygame.init()

alienspeed = [1, 1 ]
speed= [1, 1]
fpsClock = pygame.time.Clock()
i= 0
size= width,height= 500,1000
playwidth= 500
playheight= 1000
screen = pygame.display.set_mode(size)

background = pygame.image.load("images/background.png")


#Gegner generieren
pygame.display.set_caption("Shoot The Moon")
alien = pygame.image.load("images/ball.png")
alien = pygame.transform.scale(alien,(199,162))
alien_rect= alien.get_rect()


friendly = pygame.image.load("images/astronaut.png")
friendly = pygame.transform.scale(friendly,(199,162))
friendly_rect= friendly.get_rect(topleft= [100,400])



while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            
            exit()


    alien_rect = alien_rect.move(alienspeed)
    if alien_rect.left < 0 or alien_rect.right > playwidth: 
        alienspeed [0] = -alienspeed [0]
    if alien_rect.top < 0 or alien_rect.bottom > playheight:
        alienspeed [1] = -alienspeed [1]

    friendly_rect= friendly_rect.move(speed) 
    if friendly_rect.left < 0 or friendly_rect.right > playwidth: 
        speed [0] = -speed [0]
    if friendly_rect.top < 0 or friendly_rect.bottom > playheight:
        speed [1] = -speed [1]


    if alien_rect.colliderect(friendly_rect):
        print("Collision")

    screen.blit(background,(0,i))
    screen.blit(background, (0,height+i))
    i -= 1
    if i == -height:
       screen.blit(background, ( 0,height+i))
       i= 0

        

    screen.blit(alien, alien_rect)
    screen.blit(friendly, friendly_rect)
    pygame.display.flip()
    fpsClock.tick(60)
pygame.quit()