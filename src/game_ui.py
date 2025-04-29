
import math
import pygame
from game_state import GameState
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
        self.title_font = pygame.font.SysFont(FONT_NAME, 48)
        self.instruction_font = pygame.font.SysFont(FONT_NAME, 24)

    def render(self, logic, area, launcher):

        self.draw_game_area()
        self.draw_score(logic.score)
        self.draw_beans(area.beans)

        if logic.state == GameState.MOVING:
            self.draw_single_bean(logic.current_bean)

        if logic.state != GameState.ADDING_ROW:
            self.draw_launcher(launcher)

        if logic.state == GameState.GAME_OVER:
            self.draw_game_over()

        self.draw_next_bean(area.bean_queue)
        self.draw_bean_queue(area.bean_queue)

        pygame.display.flip()

    def draw_menu(self):

        self.screen.fill(BACKGROUND_COLOR)

        title = self.title_font.render("BEAN SHOOTER", True, FONT_COLOR)
        instructions = self.instruction_font.render(
            "Press SPACE to Start", True, FONT_COLOR)

        self.screen.blit(title, (SCREEN_WIDTH // 2 -
                         title.get_width() // 2, 100))
        self.screen.blit(instructions, (SCREEN_WIDTH // 2 -
                         instructions.get_width() // 2, 300))

    def draw_game_area(self):
        self.screen.fill(BACKGROUND_COLOR)

    def draw_launcher(self, launcher):
        pygame.draw.circle(self.screen, launcher.color, launcher.position, 30)

        angle_rad = math.radians(launcher.angle)
        direction_x = launcher.position[0] + 40 * math.cos(angle_rad)
        direction_y = launcher.position[1] - 40 * math.sin(angle_rad)

        pygame.draw.line(self.screen, (255, 255, 255),
                         launcher.position, (direction_x, direction_y), 5)

    def update_score(self, score):
        self.draw_score(score)

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
            'OH NO! Beans too close!', True, FONT_COLOR)

        text_width, text_height = game_over_text.get_size()
        box_width = text_width + 30
        box_height = text_height + 10

        box_x = (SCREEN_WIDTH - box_width) // 2
        box_y = (SCREEN_HEIGHT - box_height) // 2

        pygame.draw.rect(self.screen, (0, 100, 0),
                         (box_x, box_y, box_width, box_height))

        text_x = box_x + (box_width - text_width) // 2
        text_y = box_y + (box_height - text_height) // 2
        self.screen.blit(game_over_text, (text_x, text_y))

    def draw_highscores(self, highscore_manager):
        self.screen.fill(BACKGROUND_COLOR)
        title_text = self.title_font.render("HIGH SCORES", True, FONT_COLOR)
        self.screen.blit(title_text, (SCREEN_WIDTH // 2 -
                         title_text.get_width() // 2, 100))

        scores = highscore_manager.get_scores()
        y_offset = 180
        for i, entry in enumerate(scores, 1):
            score_line = f"{i}. {entry['name']} - {entry['score']}"
            score_text = self.font.render(score_line, True, FONT_COLOR)
            self.screen.blit(score_text, (SCREEN_WIDTH // 2 -
                             score_text.get_width() // 2, y_offset))
            y_offset += 40

        prompt_text = self.instruction_font.render(
            "Press any key to return to menu", True, FONT_COLOR)
        self.screen.blit(prompt_text, (SCREEN_WIDTH // 2 -
                         prompt_text.get_width() // 2, y_offset + 40))

        pygame.display.flip()

    def draw_name_input_screen(self, name):
        self.screen.fill(BACKGROUND_COLOR)

        title = self.title_font.render("Game Over!", True, FONT_COLOR)
        self.screen.blit(title, (SCREEN_WIDTH // 2 -
                         title.get_width() // 2, 80))

        prompt_text = self.font.render(
            "Enter your name for High Scores:", True, FONT_COLOR)
        self.screen.blit(prompt_text, (SCREEN_WIDTH // 2 -
                         prompt_text.get_width() // 2, 160))

        name_display = self.font.render(name + "|", True, (255, 255, 0))
        self.screen.blit(name_display, (SCREEN_WIDTH // 2 -
                         name_display.get_width() // 2, 220))

        info_text = self.instruction_font.render(
            "Press Enter to confirm", True, FONT_COLOR)
        self.screen.blit(info_text, (SCREEN_WIDTH // 2 -
                         info_text.get_width() // 2, 300))
