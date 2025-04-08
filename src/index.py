import pygame
from game_area import initialize_display, initialize_launcher
from menu import run_menu
from game_loop import run_game
from clock import Clock


def main():
    pygame.init()

    clock = Clock()

    display = initialize_display()

    start_game = run_menu(display)
    if not start_game:
        pygame.quit()
        return

    launcher = initialize_launcher()

    run_game(display, launcher, clock)

    pygame.quit()


if __name__ == "__main__":
    main()
