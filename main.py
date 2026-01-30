from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from UI import UI
import pygame
import sys
import math

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    bg = pygame.image.load("./source_art/BG.jpeg")    
    font = pygame.font.Font(None, 50)
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    score_UI = UI(10, 10, font)
    Lives_UI = UI(300,10, font)
    Stamina_UI = UI(600, 10, font)
    
    
    dt = 0


    while True:
        
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                player.lives-=1
                if score_UI.score_element == 0:
                    pass
                else:
                    score_UI.score_element-=10

                if player.lives == 0:
                    print("Game over!")
                    sys.exit()
                    
                remaining_lives= player.lives    
                player.kill()
                
               
                player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                player.lives = remaining_lives
                

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")            
                    asteroid.split()
                    shot.kill()
                    score_UI.score_element+=10
                    
        screen.fill("black")            
        screen.blit(pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT)), (0,0))
        
        for objects in drawable:
            objects.draw(screen)
            
        score_UI.score(screen)
        Lives_UI.lives(screen, live = player.lives)
        Stamina_UI.stamina(screen, stamina=math.ceil(player.stamina))
            
        pygame.display.flip()
        
        # limit framerate to 60 fps
        dt = clock.tick(60)/1000

        


if __name__ == "__main__":
    main()
