import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        
        random_angle = random.uniform(20, 50)
        
        first_new_vector = self.velocity.rotate(random_angle)
        second_new_vector = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        first_astroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_astroid.velocity = first_new_vector * 1.2
        
        second_astroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_astroid.velocity = second_new_vector * 1.2
            