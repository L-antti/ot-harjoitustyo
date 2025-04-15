import math
import pygame
from settings import BEAN_DEFAULT_SPEED


class Bean(pygame.sprite.Sprite):
    def __init__(self, color, position):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (20, 20), 20)
        self.rect = self.image.get_rect(center=position)
        self.velocity = [0, 0]
        self.radius = 20
        self.neighbours = pygame.sprite.Group()

    def set_velocity(self, angle):
        angle_rad = math.radians(angle)
        self.velocity = [BEAN_DEFAULT_SPEED * math.cos(angle_rad),
                         -BEAN_DEFAULT_SPEED * math.sin(angle_rad)]

    def update_neighbours(self, beans_group):
        self.neighbours.empty()

        for bean in beans_group:
            if bean != self and pygame.sprite.collide_circle_ratio(1.2)(self, bean):
                self.neighbours.add(bean)

    def attach(self, beans_group):
        beans_group.add(self)
        self.update_neighbours(beans_group)

    def update_position(self, y_spacing):
        self.rect.y += y_spacing

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return self is other
