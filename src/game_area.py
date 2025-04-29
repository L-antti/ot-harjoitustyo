import random
from collections import deque
import pygame
from sprites.bean import Bean
from settings import SCREEN_WIDTH, BEAN_COLORS


class GameArea:
    """Manages the game area, including bean placement and queue handling."""

    def __init__(self):
        """Initializes the game area with beans and the bean queue."""
        self.beans = pygame.sprite.OrderedUpdates()
        self.bean_queue = self.initialize_bean_queue()
        self.offset = 20
        self._create_beans(rows=5, cols=SCREEN_WIDTH // 40)

    def _create_beans(self, rows, cols, **kwargs):
        """Creates and adds beans to the game area."""
        x_spacing = kwargs.get("x_spacing", 40)
        y_spacing = kwargs.get("y_spacing", 40)
        offset_adjustment = kwargs.get("offset_adjustment", 0)

        self.offset -= offset_adjustment

        for row in range(rows):
            y_position = row * y_spacing + self.offset
            for col in range(cols):
                x_position = col * x_spacing + 20
                color = random.choice(BEAN_COLORS)
                bean = Bean(color, (x_position, y_position))
                bean.attach(self.beans)
                self.beans.add(bean)

        self.offset = 20

        for bean in self.beans:
            bean.update_neighbours(self.beans)

    def update(self):
        """Updates neighbor relationships between beans."""
        for bean in self.beans:
            bean.update_neighbours(self.beans)

    def initialize_bean_queue(self, queue_length=4):
        """Initializes the queue of upcoming beans."""
        return deque([random.choice(BEAN_COLORS) for _ in range(queue_length)])

    def get_next_bean(self):
        """Returns the next bean and adds a new one to the queue."""
        next_color = self.bean_queue.popleft()
        self.bean_queue.append(random.choice(BEAN_COLORS))
        return next_color

    def add_new_row(self):
        """Adds a new row of beans to the game area and shifts existing beans down."""
        self._create_beans(rows=1, cols=SCREEN_WIDTH //
                           40, offset_adjustment=40)

        for bean in self.beans:
            bean.update_position(40)
