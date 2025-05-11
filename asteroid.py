import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    
    def __init__(self,x ,y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", 
                           self.position, self.radius)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_velocity= self.velocity.rotate(random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        for _ in range(0,2):
            new_ast = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast.velocity = new_velocity * 1.2
            new_velocity *= -1

