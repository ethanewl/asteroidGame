import pygame
from player import Player

class UI():
    def __init__(self, x, y, font):
        self.position = pygame.Vector2(x, y)
        self.font = font
        self.score_element = 0
        
    def score(self, screen):
        score_text = self.font.render(f"Score: {self.score_element}", True, (255,255,255))
        screen.blit(score_text, (self.position.x, self.position.y))
        
    def lives(self, screen, live):
        lives_text = self.font.render(f"Lives: {live}", True, (255,255,255))
        screen.blit(lives_text, (self.position.x, self.position.y))
        
    def stamina(self, screen, stamina):
        stamina_text = self.font.render(f"Stamina: {stamina}", True, (255,255,255))
        screen.blit(stamina_text, (self.position.x, self.position.y)) 
        
    def update(self):
        pass
        
        
        