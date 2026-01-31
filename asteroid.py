import pygame
import random
import math
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.time_alive = 0
        self.rotation = 0
        self.local_points = self.shape()
        
        
    def shape(self):
        points = []
        count = 25
        for i in range(count):
            angle = math.tau * i / count
            lump = random.uniform(-self.radius * 0.08, self.radius * 0.08)
            r = self.radius + lump
            x = math.cos(angle) * r
            y = math.sin(angle) * r
            points.append(pygame.Vector2(x, y))

        return points

    def draw(self, screen):
        world_points = [self.position + p.rotate(self.rotation) for p in self.local_points]
        pygame.draw.polygon(screen, "white", world_points, LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt
        self.rotation += 15 * dt
        self.time_alive += dt
        
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
        

            