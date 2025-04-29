import pygame
from game_area import GameArea
from game_ui import GameUI
from game_logic import GameLogic
from game_state import GameState
from sprites.launcher import Launcher
from highscore_manager import HighscoreManager
from clock import Clock
from settings import LAUNCHER_POSITION, FPS


class GameController:
    """Manages the overall game flow, user inputs, and interactions between game logic and UI."""

    def __init__(self, screen):
        """Initializes the game controller with UI, game area, logic, and necessary components.

        Args:
            screen (pygame.Surface): The main game screen.
        """
        self.ui = GameUI(screen)
        self.area = GameArea()
        self.logic = GameLogic(self.area)
        self.launcher = Launcher(LAUNCHER_POSITION)
        self.clock = Clock()
        self.highscore_manager = HighscoreManager()
        self.running = True
        self.in_menu = True

    def run(self):
        """Starts the game loop, handling events, game state updates, and rendering."""
        while self.running:
            self.handle_events()

            if self.in_menu:
                self.ui.draw_menu()
                pygame.display.flip()
                if self.handle_events():
                    pygame.event.clear()
            else:
                if self.logic.state != GameState.IDLE:
                    self.logic.update_game_state()

                self.handle_game_over()

                self.ui.update_score(self.logic.score)
                self.ui.render(self.logic, self.area, self.launcher)

                self.clock.tick(FPS)

    def handle_events(self):
        """Handles user inputs, including movement, game actions, and quitting.

        Returns:
            bool: True if the user exits the menu, False otherwise.
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.launcher.rotate(1)
        if keys[pygame.K_RIGHT]:
            self.launcher.rotate(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.in_menu:
                    self.in_menu = False
                    return True
                if event.key == pygame.K_UP and self.logic.state == GameState.IDLE:
                    self.logic.launch_next_bean(self.launcher)

        return False

    def handle_game_over(self):
        """Handles the game over state, asks for player's name and saves highscore."""
        if self.logic.check_game_over() or self.logic.state == GameState.GAME_OVER:
            self.ui.draw_game_over()
            pygame.display.flip()
            pygame.time.delay(1000)

            player_name = self.ask_player_name()

            if player_name:
                self.highscore_manager.add_score(player_name, self.logic.score)

            self.show_highscores()
            self.reset_game()

    def show_highscores(self):
        """Displays the high scores screen."""
        showing = True
        while showing:
            self.ui.draw_highscores(self.highscore_manager)
            for event in pygame.event.get():
                if event.type in (pygame.QUIT, pygame.KEYDOWN):
                    showing = False

    def ask_player_name(self):
        name = ""
        input_active = True

        while input_active:
            self.ui.draw_name_input_screen(name)
            pygame.display.flip()

            name, input_active = self.handle_name_input(name, input_active)

        return name.strip()

    def handle_name_input(self, name, input_active):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None, False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name.strip():
                    return name, False
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif len(name) < 12 and event.unicode.isprintable():
                    name += event.unicode

        return name, input_active

    def reset_game(self):
        self.area = GameArea()
        self.logic = GameLogic(self.area)
        self.launcher = Launcher(LAUNCHER_POSITION)
        self.clock = Clock()
        self.in_menu = True
