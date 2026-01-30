import pygame
from player import Player

class UI():
    def __init__(self, x, y, font):
        self.position = pygame.Vector2(x, y)
        self.font = font
        self.score = 0
        #self.lives = Player.lives
        
    
    def draw(self, screen):
        text = self.font.render(f"Score: {self.score}", True, (255,255,255))
        screen.blit(text, (self.position.x, self.position.y))
        
        
        
    def update(self):
        pass
        
        
        