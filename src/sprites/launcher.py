import pygame
import math

class Launcher:
    def __init__(self, position):
        self.position = position
        self.angle = 90
        self.color = (255, 0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, 30)

        direction_x = self.position[0] + 40 * math.cos(math.radians(self.angle))
        direction_y = self.position[1] - 40 * math.sin(math.radians(self.angle))
        
        pygame.draw.line(screen, (255, 255, 255), self.position, (direction_x, direction_y), 5)


    def rotate(self, delta):
        self.angle += delta
        self.angle = max(10, min(170, self.angle))