import random
from collections import deque
import pygame
from sprites.bean import Bean
from settings import SCREEN_WIDTH, BEAN_COLORS


class GameArea:
    def __init__(self):
        self.beans = pygame.sprite.OrderedUpdates()
        self.bean_queue = self.initialize_bean_queue()
        self.offset = 20
        self.initialize_predefined_beans()

    def initialize_predefined_beans(self):
        x_spacing = 40
        y_spacing = 40
        rows = 5
        cols = SCREEN_WIDTH // x_spacing
        self._create_and_attach_beans(
            rows, cols, x_spacing, y_spacing)

        for bean in self.beans:
            bean.update_neighbours(self.beans)

    def _create_and_attach_beans(self, rows, cols, x_spacing, y_spacing):
        for row in range(rows):
            y_position = row * y_spacing + self.offset
            for col in range(cols):
                x_position = col * x_spacing + 20
                color = random.choice(BEAN_COLORS)
                bean = Bean(color, (x_position, y_position))
                bean.attach(self.beans)
                self.beans.add(bean)

    def update(self):
        for bean in self.beans:
            bean.update_neighbours(self.beans)

    def initialize_bean_queue(self, queue_length=4):
        return deque([random.choice(BEAN_COLORS) for _ in range(queue_length)])

    def get_next_bean(self):
        next_color = self.bean_queue.popleft()
        self.bean_queue.append(random.choice(BEAN_COLORS))
        return next_color

    def add_new_row(self):
        x_spacing = 40
        y_spacing = 40
        cols = SCREEN_WIDTH // x_spacing

        self.offset -= y_spacing
        self._create_and_attach_beans(
            1, cols, x_spacing, y_spacing)
        self.offset = 20

        for bean in self.beans:
            bean.update_position(y_spacing)
