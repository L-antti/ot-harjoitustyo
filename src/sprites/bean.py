import pygame
import math


class Bean(pygame.sprite.Sprite):
    def __init__(self, color, position):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (20, 20), 20)
        self.rect = self.image.get_rect(center=position)
        self.velocity = [0, 0]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.left <= 0 or self.rect.right >= 400: 
            self.velocity[0] *= -1  

        if self.rect.top <= 0:
            self.velocity = [0, 0]