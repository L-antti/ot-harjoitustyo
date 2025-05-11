import unittest
import pygame
from unittest.mock import MagicMock
from game_state import GameState
from controller.gameover_controller import GameOverController


class TestGameOverController(unittest.TestCase):
    def setUp(self):
        self.logic = MagicMock()
        self.highscore_manager = MagicMock()
        self.view = MagicMock()

        self.controller = GameOverController(
            self.logic, self.highscore_manager, self.view)

    def test_game_over_flow(self):
        self.logic.check_game_over.return_value = True
        self.logic.state = GameState.GAME_OVER

        pygame.event.get = MagicMock(
            return_value=[pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_RETURN})])

        self.controller._ask_player_name = MagicMock(return_value="Player1")

        self.controller.handle_game_over()

        self.view.show_game_over_screen.assert_called_once()
        self.logic.reset_game.assert_called_once()
        self.highscore_manager.add_score.assert_called_once_with(
            "Player1", self.logic.score)


if __name__ == "__main__":
    unittest.main()
