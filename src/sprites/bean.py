import math
import pygame
from settings import SCREEN_WIDTH


class Bean(pygame.sprite.Sprite):
    def __init__(self, color, position):
        super().__init__()
        self.image = pygame.Surface(
            (40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (20, 20), 20)
        self.rect = self.image.get_rect(center=position)
        self.velocity = [0, 0]
        self.attached = False
        self.radius = 20
        self.neighbours = []

    def update(self, beans):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.velocity[0] *= -1

        if self.rect.top <= 0:
            self.velocity = [0, 0]
            self.attached = True
            self.add_neighbors(beans)

        for other_bean in beans:
            if self != other_bean and self.check_collision(other_bean):
                self.velocity = [0, 0]
                self.attached = True
                self.add_neighbors(beans)

    def shoot(self, angle):
        angle_rad = math.radians(angle)
        self.velocity = [5 * math.cos(angle_rad), -5 * math.sin(angle_rad)]

    def check_collision(self, other_bean):
        distance = math.sqrt(
            (self.rect.centerx - other_bean.rect.centerx) ** 2 +
            (self.rect.centery - other_bean.rect.centery) ** 2
        )
        return distance < (self.radius + other_bean.radius)

    def add_neighbors(self, beans):
        self.neighbours = [
            other_bean for other_bean in beans
            if self != other_bean and self.check_collision(other_bean)
        ]

    @staticmethod
    def check_color_groups(beans):
        beans_to_remove = set()

        for bean in beans:
            if bean.attached:
                same_color_neighbours = [
                    neighbour for neighbour in bean.neighbours
                    if neighbour.image.get_at((20, 20)) == bean.image.get_at((20, 20))
                ]

                cluster = [bean] + same_color_neighbours

                if len(cluster) >= 3:
                    beans_to_remove.add(bean)
                    beans_to_remove.update(cluster)

        return list(beans_to_remove)
