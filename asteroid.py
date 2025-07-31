import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    from constants import ASTEROID_MIN_RADIUS

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), int(self.radius), 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
    # Always remove the asteroid that got hit
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # It's already the smallest size

    # Generate random angle between 20° and 50°
        angle = random.uniform(20, 50)

    # Create two new velocity directions
        velocity1 = self.velocity.rotate(angle) * 1.2
        velocity2 = self.velocity.rotate(-angle) * 1.2

    # Calculate new smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

    # Spawn two new asteroids at the same position
        from asteroid import Asteroid  # Prevent circular import errors

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = velocity1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = velocity2
