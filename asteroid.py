import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface)-> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float)-> None:
        self.position += self.velocity * dt

    def split(self)-> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_asteroid1_angle = random.uniform(20,50)
            new_asteroid2_angle = random.uniform(-20,-50)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x,self.position.y,new_asteroid_radius)
            asteroid2 = Asteroid(self.position.x,self.position.y,new_asteroid_radius)
            asteroid1.velocity = self.velocity.rotate(new_asteroid1_angle) * 1.2
            asteroid2.velocity = self.velocity.rotate(new_asteroid2_angle) * 1.2
