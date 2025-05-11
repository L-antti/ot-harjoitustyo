import pygame
from mechanics.game_area import GameArea
from mechanics.game_logic import GameLogic
from controller.event_handler import EventHandler
from controller.gameover_controller import GameOverController
from controller.game_loop import GameLoop
from ui.renderer import Renderer
from ui.gameover_view import GameOverView
from repository.highscore_manager import HighscoreManager
from sprites.launcher import Launcher
from clock import Clock
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, LAUNCHER_POSITION


def main():
    """
    Initializes and runs the Bean Shooter game.

    This function sets up the game environment, including the game area, logic, launcher,
    event handling, and rendering. It starts the main game loop and ends when the game is over,
    closing the Pygame window afterward.

    Components initialized:
        - Game area: The grid where the game beans are placed.
        - Game logic: Controls game mechanics and state.
        - Launcher: Manages bean shooting.
        - Highscore manager: Saves and loads high scores.
        - Event handler: Handles player input.
        - Renderer: Renders the game visuals.
        - Game over controller: Manages the game over screen.
        - Game loop: Runs the game by updating and rendering.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Bean Shooter")

    area = GameArea()
    logic = GameLogic(area)
    launcher = Launcher(LAUNCHER_POSITION)
    clock = Clock()
    highscore = HighscoreManager()
    view = GameOverView(screen, highscore)
    gameover = GameOverController(logic, highscore, view)

    event_handler = EventHandler(launcher, logic)
    renderer = Renderer(screen, area, logic, launcher)
    loop = GameLoop(logic, event_handler, renderer, gameover, clock)

    loop.run()
    pygame.quit()


if __name__ == "__main__":
    main()
