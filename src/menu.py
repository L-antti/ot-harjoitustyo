import pygame
from settings import (SCREEN_WIDTH,
                      BACKGROUND_COLOR,
                      FONT_NAME,
                      FONT_COLOR)


class GameMenu:
    def __init__(self, screen):
        self.screen = screen  # Store the screen reference

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
        return False

    def draw_menu(self):
        self.screen.fill(BACKGROUND_COLOR)

        font = pygame.font.SysFont(FONT_NAME, 48)
        title = font.render("BEAN SHOOTER", True, FONT_COLOR)
        self.screen.blit(title, (SCREEN_WIDTH // 2 -
                         title.get_width() // 2, 100))

        font = pygame.font.SysFont(FONT_NAME, 24)
        instructions = font.render("Press SPACE to Start", True, FONT_COLOR)
        self.screen.blit(instructions, (SCREEN_WIDTH // 2 -
                                        instructions.get_width() // 2, 300))
