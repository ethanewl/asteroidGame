from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import UI
import pygame
import sys

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    font = pygame.font.Font(None, 50)
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    ui_element = pygame.sprite.Group()
    

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    score_UI = UI(10, 10, font)
    
    
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
                print("Game over!")
                sys.exit()
                
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")            
                    asteroid.split()
                    shot.kill()
                    score_UI.score+=10
                    
                
        
        screen.fill("black")
        
        
        for objects in drawable:
            objects.draw(screen)
            
        score_UI.draw(screen)
            
        pygame.display.flip()
        
        # limit framerate to 60 fps
        dt = clock.tick(60)/1000

        


if __name__ == "__main__":
    main()
