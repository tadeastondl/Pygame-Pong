import pygame
from paddle import Paddle

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

# okno aplikace
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Turbo crazy Pong hra")

paddleA = Paddle(RED, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(BLUE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

pygame_icon = pygame.image.load('res/stefo.png')
pygame.display.set_icon(pygame_icon)

#list spritu
all_sprites_list = pygame.sprite.Group()
# pridani do listu
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)


powerOn = True

clock = pygame.time.Clock()
 
# game loop
while powerOn:
    #  Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
              powerOn = False
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE: 
                     powerOn=False  
 
    # Logika:
    all_sprites_list.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)    
 
 
    # Vykreslovani:
    screen.fill(BLACK)
    pygame.draw.line(screen, GREEN, [349, 0], [349, 500], 5)  
    all_sprites_list.draw(screen)
    pygame.display.flip()
     
    clock.tick(60)
 
pygame.quit()