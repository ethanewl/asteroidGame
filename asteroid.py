import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_SPEED

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def direction(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        vector_rotate = unit_vector.rotate(self.rotation)
        vector_lenth = vector_rotate * (ASTEROID_SPEED * dt)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
        