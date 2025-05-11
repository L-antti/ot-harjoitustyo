import math
import pygame
import textwrap
from game_state import GameState
from settings import (BACKGROUND_COLOR,
                      SCREEN_HEIGHT,
                      SCREEN_WIDTH,
                      LAUNCHER_POSITION,
                      FONT_COLOR,
                      FONT_NAME,
                      FONT_SIZE)


class Renderer:
    def __init__(self, screen, game_area, logic, launcher):
        """
        Initializes the Renderer with all required game components.

        Args:
            screen (pygame.Surface): The surface to render graphics on.
            game_area (GameArea): The current game area containing beans.
            logic (GameLogic): The game logic handling state and scoring.
            launcher (Launcher): The launcher used to shoot beans.
        """
        self.screen = screen
        self.game_area = game_area
        self.logic = logic
        self.launcher = launcher
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
        self.title_font = pygame.font.SysFont(FONT_NAME, 48)
        self.instruction_font = pygame.font.SysFont(FONT_NAME, 24)

    def draw_menu(self):
        """Draws the start menu with the title and instructions."""
        self.screen.fill(BACKGROUND_COLOR)
        title = self.title_font.render("BEAN SHOOTER", True, FONT_COLOR)
        instructions = [
            "Shoot beans and collect points.",
            "If you miss 3 shots, a new row will be added.",
            "The game ends when a bean reaches the bottom.",
            "Use left and right arrow keys to move the launcher.",
            "Press up arrow to shoot beans.",
            "HAPPY SHOOTING!",
            "",
            "",
            "Press SPACE to Start"
        ]

        y_offset = 300
        for line in instructions:
            instruction = self.instruction_font.render(line, True, FONT_COLOR)

            self.screen.blit(instruction, (SCREEN_WIDTH // 2 -
                             instruction.get_width() // 2, y_offset))
            y_offset += 30

        self.screen.blit(title, (SCREEN_WIDTH // 2 -
                         title.get_width() // 2, 100))
        pygame.display.flip()

    def render_game_view(self):
        """
        Renders the full game screen including:
        - Game area
        - Score
        - Beans
        - Current bean (if moving)
        - Launcher
        - Next bean
        - Bean queue
        """
        self._draw_game_area()
        self._draw_score(self.logic.score)
        self._draw_beans(self.game_area.beans)

        if self.logic.state == GameState.MOVING:
            self._draw_single_bean(self.logic.current_bean)

        self._draw_launcher(self.launcher)

        self._draw_next_bean(self.game_area.get_next_bean_color())
        self._draw_bean_queue(self.game_area.bean_queue)
        pygame.display.flip()

    def _draw_game_area(self):
        self.screen.fill(BACKGROUND_COLOR)

    def _draw_launcher(self, launcher):
        pygame.draw.circle(self.screen, launcher.color, launcher.position, 30)
        angle_rad = math.radians(launcher.angle)
        direction_x = launcher.position[0] + 40 * math.cos(angle_rad)
        direction_y = launcher.position[1] - 40 * math.sin(angle_rad)
        pygame.draw.line(self.screen, (255, 255, 255),
                         launcher.position, (direction_x, direction_y), 5)

    def _draw_score(self, score):
        text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        self.screen.blit(text, (10, SCREEN_HEIGHT - 50))

    def _draw_single_bean(self, bean):
        self.screen.blit(bean.image, bean.rect)

    def _draw_beans(self, beans):
        beans.draw(self.screen)

    def _draw_next_bean(self, next_bean_color):
        if next_bean_color:
            pygame.draw.circle(self.screen, next_bean_color,
                               LAUNCHER_POSITION, 20)

    def _draw_bean_queue(self, bean_queue):
        queue_x_start = SCREEN_WIDTH - 150
        queue_y_start = SCREEN_HEIGHT - 50
        for i, color in enumerate(list(bean_queue)[1:]):
            x = queue_x_start + i * 50
            pygame.draw.circle(self.screen, color, (x, queue_y_start), 20)
