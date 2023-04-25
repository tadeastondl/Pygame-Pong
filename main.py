import pygame
import sys
from paddle import Paddle
from ball import Ball
class Pong: 
    
    #barvicky
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    BLUE = (0,0,255)
    GREEN = (0,255,0)

    
    
    @staticmethod
    def init():
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        wall_sound = pygame.mixer.Sound("pongWall.mp3")
        hit_sound = pygame.mixer.Sound("pongHit.wav")
        font = pygame.font.Font(None, 74)
        textScore = font.render(" ", True, (255, 255, 255))

        
    


        # okno aplikace
        sizeWidth = 700
        sizeHeight = 500
        size = (sizeWidth, sizeHeight)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Muj Pong  >:)")

        paddleA = Paddle(Pong.RED, 15, 115)
        paddleA.rect.x = 20
        paddleA.rect.y = 200

        paddleB = Paddle(Pong.BLUE, 15, 115)
        paddleB.rect.x = 670
        paddleB.rect.y = 200
        
        ball = Ball(Pong.WHITE,10,10)
        ball.rect.x = 345
        ball.rect.y = 195

        pygame_icon = pygame.image.load('res/Icon.png')
        pygame.display.set_icon(pygame_icon)

        #list spritu
        all_sprites_list = pygame.sprite.Group()
        # pridani do listu
        all_sprites_list.add(paddleA)
        all_sprites_list.add(paddleB)
        all_sprites_list.add(ball)


        powerOn = True

        clock = pygame.time.Clock()
        scoreA = 0
        scoreB = 0
        
        # game loop
        while powerOn:
            
            #  Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    powerOn = False
                elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_ESCAPE: 
                            sys.exit()
        
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
                
            #kontrola zda se micek dotkne :
            if ball.rect.x>=690:
                pygame.mixer.Sound.play(wall_sound)
                scoreA +=1
                ball.rect.x = 345
                ball.rect.y = 195
                ball.velocity[0] = -ball.velocity[0]
                paddleB.rect.y = 200
                paddleA.rect.y = 200    
                # textScore = font.render("cerveny dostal bod!", True, (255, 255, 255))
                pygame.time.wait(1500)                
            if ball.rect.x<=0:
                pygame.mixer.Sound.play(wall_sound)
                scoreB +=1
                ball.velocity[0] = -ball.velocity[0]
                ball.rect.x = 345
                ball.rect.y = 195    
                paddleB.rect.y = 200
                paddleA.rect.y = 200
                # textScore = font.render("modry dostal bod!", True, (255, 255, 255))
                pygame.time.wait(1500)
               #branky ^^

            if ball.rect.y>490:
                ball.velocity[1] = -ball.velocity[1]
            if ball.rect.y<0:            
                ball.velocity[1] = -ball.velocity[1] 
            #kolize mezi mickem a palkou
            if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
                ball.bounce()
                pygame.mixer.Sound.play(hit_sound)
        
            # Vykreslovani:
            screen.fill(Pong.BLACK)
            pygame.draw.line(screen, Pong.WHITE, [349, 0], [349, 500], 5)  
            all_sprites_list.draw(screen)
            
            #skore:
            screen.blit(textScore, (110,50 ))
            textA = font.render(str(scoreA), 1, Pong.RED)
            screen.blit(textA, (250,10))
            textB = font.render(str(scoreB), 1, Pong.BLUE)
            screen.blit(textB, (420,10))

            
            
            
            pygame.display.flip()
            


            clock.tick(60)
        
        pygame.quit()
if __name__ == '__main__':
    Pong.init()
    