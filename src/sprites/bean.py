import math
import pygame
from settings import BEAN_DEFAULT_SPEED, SCREEN_WIDTH


class Bean(pygame.sprite.Sprite):
    """Represents a single bean, handling movement and collisions."""

    def __init__(self, color, position):
        """Initializes a bean with a given color and position."""
        super().__init__()
        self.color = color
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (20, 20), 20)
        self.rect = self.image.get_rect(center=position)
        self.velocity = [0, 0]
        self.radius = 20
        self.neighbours = pygame.sprite.Group()

    def set_velocity(self, angle):
        """Sets the bean's velocity based on the given launch angle."""
        angle_rad = math.radians(angle)
        self.velocity = [BEAN_DEFAULT_SPEED * math.cos(angle_rad),
                         -BEAN_DEFAULT_SPEED * math.sin(angle_rad)]

    def move(self):
        """Updates bean's position and bounces off side walls."""
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.velocity[0] *= -1

    def has_collided(self, beans_group):
        """Returns True if this bean collides with another bean or hits the top."""
        if self.rect.top <= 0:
            return True

        overlapping = pygame.sprite.spritecollide(
            self, beans_group, False, pygame.sprite.collide_circle
        )
        return bool(overlapping)

    def update(self, y_offset):
        """Moves the bean downward by a certain offset."""
        self.rect.y += y_offset

    def stop(self):
        """Stops the bean's movement."""
        self.velocity = [0, 0]

    def __hash__(self):
        """Returns a unique hash for the bean."""
        return id(self)

    def __eq__(self, other):
        """Checks if two beans are the same."""
        return self is other
