import pygame
from settings import (SCREEN_WIDTH,
                      BACKGROUND_COLOR,
                      FONT_NAME,
                      FONT_COLOR)


def draw_menu(screen):
    screen.fill(BACKGROUND_COLOR)

    font = pygame.font.SysFont(FONT_NAME, 48)
    title = font.render("BEAN SHOOTER", True, FONT_COLOR)
    screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

    font = pygame.font.SysFont(FONT_NAME, 24)
    instructions = font.render("Press SPACE to Start", True, FONT_COLOR)
    screen.blit(instructions, (SCREEN_WIDTH // 2 -
                instructions.get_width() // 2, 300))


def handle_menu_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return True
    return None


def run_menu(screen):
    while True:
        result = handle_menu_events()
        if result is False:
            return False
        if result is True:
            return True

        draw_menu(screen)
        pygame.display.flip()
