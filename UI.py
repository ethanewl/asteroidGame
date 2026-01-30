import pygame
from player import Player

class UI():
    def __init__(self, x, y, font):
        self.position = pygame.Vector2(x, y)
        self.font = font
        self.score_element = 0
        
    
    def score(self, screen):
        text = self.font.render(f"Score: {self.score_element}", True, (255,255,255))
        screen.blit(text, (self.position.x, self.position.y))
        
    def lives(self, screen, live):
        lives = self.font.render(f"Lives: {live}", True, (255,255,255))
        screen.blit(lives, (self.position.x, self.position.y))
        
        
        
        
    def update(self):
        pass
        
        
        