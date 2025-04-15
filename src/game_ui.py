import math
import pygame
from settings import (BACKGROUND_COLOR,
                      SCREEN_HEIGHT,
                      SCREEN_WIDTH,
                      LAUNCHER_POSITION,
                      FONT_COLOR,
                      FONT_NAME,
                      FONT_SIZE)


class GameUI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

    def draw_game_area(self):
        self.screen.fill(BACKGROUND_COLOR)

    def draw_launcher(self, launcher):
        pygame.draw.circle(self.screen, launcher.color, launcher.position, 30)

        angle_rad = math.radians(launcher.angle)
        direction_x = launcher.position[0] + 40 * math.cos(angle_rad)
        direction_y = launcher.position[1] - 40 * math.sin(angle_rad)

        pygame.draw.line(self.screen, (255, 255, 255), launcher.position,
                         (direction_x, direction_y), 5)

    def draw_score(self, score):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, (255, 255, 255))
        self.screen.blit(text, (10, SCREEN_HEIGHT - 50))

    def draw_single_bean(self, bean):
        self.screen.blit(bean.image, bean.rect)

    def draw_beans(self, beans):
        beans.draw(self.screen)

    def draw_next_bean(self, bean_queue):
        next_bean_color = bean_queue[0]
        pygame.draw.circle(self.screen, next_bean_color, LAUNCHER_POSITION, 20)

    def draw_bean_queue(self, bean_queue):
        queue_x_start = SCREEN_WIDTH - 150
        queue_y_start = SCREEN_HEIGHT - 50

        for i, color in enumerate(list(bean_queue)[1:]):
            x = queue_x_start + i * 50
            pygame.draw.circle(self.screen, color, (x, queue_y_start), 20)

    def draw_game_over(self):
        game_over_text = self.font.render(
            'GAME OVER! Pavut tulivat liian lähelle', True, FONT_COLOR)

        text_width, text_height = game_over_text.get_size()
        box_width = text_width + 40
        box_height = text_height + 20

        box_x = (SCREEN_WIDTH - box_width) // 2
        box_y = (SCREEN_HEIGHT - box_height) // 2

        pygame.draw.rect(self.screen, (0, 100, 0), (box_x, box_y,
                         box_width, box_height))

        text_x = box_x + (box_width - text_width) // 2
        text_y = box_y + (box_height - text_height) // 2
        self.screen.blit(game_over_text, (text_x, text_y))
