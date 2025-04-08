import random
from collections import deque
import pygame
from sprites.launcher import Launcher
from sprites.bean import Bean
from settings import (SCREEN_WIDTH,
                      SCREEN_HEIGHT,
                      BACKGROUND_COLOR,
                      BORDER_COLOR,
                      BORDER_THICKNESS,
                      BEAN_COLORS)


def initialize_display():
    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("BEAN SHOOTER")
    return display


def initialize_launcher():
    return Launcher((SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))


def initialize_predefined_beans():
    beans = pygame.sprite.Group()
    x_spacing = 40
    y_spacing = 40
    rows = 1
    cols = SCREEN_WIDTH // x_spacing

    for row in range(rows):
        y_position = row * y_spacing + 20
        for col in range(cols):
            x_position = col * x_spacing + 20
            color = random.choice(BEAN_COLORS)
            bean = Bean(color, (x_position, y_position))
            beans.add(bean)
    return beans


def initialize_bean_queue():
    return deque([random.choice(BEAN_COLORS) for _ in range(3)])


def draw_game_area(screen):
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, BORDER_COLOR,
                     (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), BORDER_THICKNESS)


def draw_next_bean(screen, next_bean_color, launcher_position):
    x, y = launcher_position
    next_bean_y = y
    pygame.draw.circle(screen, next_bean_color, (x, next_bean_y), 20)


def draw_bean_queue(screen, bean_queue):
    screen_width = screen.get_width()
    queue_x_start = screen_width // 2 + 80
    queue_y = screen.get_height() - 50

    for i, color in enumerate(bean_queue):
        x = queue_x_start + i * 50
        pygame.draw.circle(screen, color, (x, queue_y), 20)


def draw_score(screen, score):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"{score}", True, (255, 255, 255))
    screen.blit(score_text, (50, SCREEN_HEIGHT-50))
