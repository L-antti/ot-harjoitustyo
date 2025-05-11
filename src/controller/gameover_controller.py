import pygame
from game_state import GameState


class GameOverController:
    """
    Handles what happens when the game ends.
    """

    def __init__(self, logic, highscore_manager, view):
        """
        Sets up the controller with game logic, highscore manager, and view.
        """
        self.logic = logic
        self.highscore_manager = highscore_manager
        self.view = view

    def handle_game_over(self):
        """
        Shows the game over screen, asks for name, saves score, and resets the game.
        """
        if self.logic.check_game_over() or self.logic.state == GameState.GAME_OVER:
            self.view.show_game_over_screen()

            player_name = self._ask_player_name()
            if player_name:
                self.highscore_manager.add_score(player_name, self.logic.score)

            self.view.show_highscores_screen(self.highscore_manager)
            self._wait_for_any_key()
            self.logic.reset_game()

    def _ask_player_name(self):
        name = ""
        input_active = True
        while input_active:
            self.view.draw_name_input(name)
            input_active, name = self._handle_name_input(name)
        return name.strip() if name.strip() else None

    def _handle_name_input(self, name):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False, name
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_RETURN:
                return False, name
            if event.key == pygame.K_BACKSPACE:
                return True, name[:-1]
            if len(name) < 12 and event.unicode.isprintable():
                return True, name + event.unicode
        return True, name

    def _wait_for_any_key(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type in (pygame.QUIT, pygame.KEYDOWN):
                    waiting = False
