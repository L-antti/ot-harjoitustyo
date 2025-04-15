import pygame
from game_controller import GameController
from settings import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Bean Shooter")

    game_controller = GameController(screen)
    game_controller.run()

    pygame.quit()


if __name__ == "__main__":
    main()
