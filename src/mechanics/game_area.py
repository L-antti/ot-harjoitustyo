import random
from collections import deque
import pygame
from sprites.bean import Bean
from settings import SCREEN_WIDTH, BEAN_COLORS


class GameArea:
    """Manages the game area, including bean placement and queue handling."""

    def __init__(self, queue_length=4):
        """Initializes the game area with beans and the bean queue."""
        self.beans = pygame.sprite.OrderedUpdates()
        self.bean_queue = deque(random.choices(BEAN_COLORS, k=queue_length))
        self.offset = 20
        self._create_beans(rows=5, cols=SCREEN_WIDTH // 40)

    def _create_beans(self, rows, cols, **kwargs):
        x_spacing = kwargs.get("x_spacing", 40)
        y_spacing = kwargs.get("y_spacing", 40)
        offset_adjustment = kwargs.get("offset_adjustment", 0)

        self.offset -= offset_adjustment
        new_beans = []

        for row in range(rows):
            y_position = row * y_spacing + self.offset
            for col in range(cols):
                x_position = col * x_spacing + 20
                color = random.choice(BEAN_COLORS)
                bean = Bean(color, (x_position, y_position))
                self.beans.add(bean)
                new_beans.append(bean)
        self.offset = 20

        return new_beans

    def attach_bean(self, bean):
        """Attaches a bean to the area and updates neighbors globally."""
        self.beans.add(bean)
        self._update_all_neighbours()

    def _update_all_neighbours(self):
        """Updates neighbor info for all beans."""
        for bean in self.beans:
            bean.neighbours.empty()
            for other in self.beans:
                if bean != other and pygame.sprite.collide_circle_ratio(1.2)(bean, other):
                    bean.neighbours.add(other)
                    other.neighbours.add(bean)

    def get_next_bean(self):
        """Returns the next bean and adds a new one to the queue."""
        next_color = self.bean_queue.popleft()
        self.bean_queue.append(random.choice(BEAN_COLORS))
        return next_color

    def get_next_bean_color(self):
        """Returns color of the next bean in queue."""
        return self.bean_queue[0] if self.bean_queue else None

    def add_new_row(self):
        """Adds a new row of beans to the game area and shifts existing beans down."""
        new_beans = self._create_beans(rows=1, cols=SCREEN_WIDTH //
                                       40, offset_adjustment=40)
        self._shift_beans_down(40)
        self._update_neighbours_for_new_beans(new_beans)

    def _update_neighbours_for_new_beans(self, new_beans):
        for bean in new_beans:
            bean.neighbours.empty()
            for other in self.beans:
                if bean != other and pygame.sprite.collide_circle_ratio(1.2)(bean, other):
                    bean.neighbours.add(other)
                    other.neighbours.add(bean)

    def _shift_beans_down(self, y_offset):
        self.beans.update(y_offset)

    def reset(self):
        """Resets the area and queue to starting state."""
        self.beans.empty()
        self.bean_queue = deque(random.choices(
            BEAN_COLORS, k=len(self.bean_queue)))
        self._create_beans(rows=5, cols=SCREEN_WIDTH // 40)
