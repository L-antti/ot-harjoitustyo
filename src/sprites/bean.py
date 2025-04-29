import math
import pygame
from settings import BEAN_DEFAULT_SPEED


class Bean(pygame.sprite.Sprite):
    """Represents a bean in the game, handling movement, collisions, and interactions."""

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

    def update_neighbours(self, beans_group):
        """Updates the list of neighboring beans that are within collision range."""
        self.neighbours.empty()

        for bean in beans_group:
            if bean != self and pygame.sprite.collide_circle_ratio(1.2)(self, bean):
                self.neighbours.add(bean)

    def attach(self, beans_group):
        """Attaches the bean to the given group and updates its neighbors."""
        beans_group.add(self)
        self.update_neighbours(beans_group)

    def update_position(self, y_spacing):
        """Moves the bean downward when the game area shifts."""
        self.rect.y += y_spacing

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return self is other
