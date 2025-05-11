import pygame
from settings import (BACKGROUND_COLOR,
                      SCREEN_HEIGHT,
                      SCREEN_WIDTH,
                      FONT_COLOR,
                      FONT_NAME,
                      FONT_SIZE)


class GameOverView:
    def __init__(self, screen, highscore_manager):
        """
        Initializes the GameOverView with a screen and a highscore manager.

        Args:
            screen (pygame.Surface): The surface to draw on.
            highscore_manager (HighscoreManager): The manager responsible for handling high scores.
        """
        self.screen = screen
        self.highscore_manager = highscore_manager
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
        self.title_font = pygame.font.SysFont(FONT_NAME, 48)
        self.instruction_font = pygame.font.SysFont(FONT_NAME, 24)

    def show_game_over_screen(self):
        """Displays the game over screen."""
        self._draw_game_over()
        pygame.display.flip()
        pygame.time.delay(1000)

    def _draw_game_over(self):
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

    def draw_name_input(self, name):
        """
        Draws the screen where the player can input their name after a game over.

        Args:
            name (str): The player's name entered for the highscore.
        """
        self.screen.fill(BACKGROUND_COLOR)
        title = self.font.render("Game Over!", True, FONT_COLOR)
        self.screen.blit(title, (SCREEN_WIDTH // 2 -
                         title.get_width() // 2, 80))

        prompt_text = self.font.render(
            "Enter your name for High Scores:", True, FONT_COLOR)
        self.screen.blit(prompt_text, (SCREEN_WIDTH // 2 -
                         prompt_text.get_width() // 2, 160))

        name_display = self.font.render(name + "|", True, (255, 255, 0))
        self.screen.blit(name_display, (SCREEN_WIDTH // 2 -
                         name_display.get_width() // 2, 220))

        info_text = self.font.render(
            "Press Enter to confirm", True, FONT_COLOR)
        self.screen.blit(info_text, (SCREEN_WIDTH // 2 -
                         info_text.get_width() // 2, 300))
        pygame.display.flip()

    def show_highscores_screen(self, highscore_manager):
        """
        Displays the high scores screen with the list of high scores.

        Args:
            highscore_manager (HighscoreManager): The manager that retrieves the high scores.
        """
        self._draw_highscores(highscore_manager)
        pygame.display.flip()

    def _draw_highscores(self, highscore_manager):
        self.screen.fill(BACKGROUND_COLOR)
        title_text = self.font.render("HIGH SCORES", True, FONT_COLOR)
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
            "Press any key to start again", True, FONT_COLOR)
        self.screen.blit(prompt_text, (SCREEN_WIDTH // 2 -
                         prompt_text.get_width() // 2, y_offset + 40))

        pygame.display.flip()
