import unittest
from unittest.mock import patch
import pygame
from game_controller import GameController
from game_state import GameState
from clock import Clock


class TestGameController(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.mock_screen = pygame.Surface((600, 800))
        self.controller = GameController(self.mock_screen)
        self.controller.clock = Clock()
        self.controller.running = True
        self.controller.in_menu = True

    def test_game_starts_in_menu(self):
        self.assertTrue(self.controller.in_menu)
        self.assertTrue(self.controller.running)

    def test_exit_menu(self):
        start_game_event = pygame.event.Event(
            pygame.KEYDOWN, {"key": pygame.K_SPACE})
        pygame.event.post(start_game_event)
        self.controller.handle_events()
        self.assertFalse(self.controller.in_menu)

    @patch("game_controller.GameLogic.launch_next_bean")
    def test_launch_bean_when_idle(self, mock_launch_bean):
        self.controller.logic.state = GameState.IDLE
        launch_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_UP})
        pygame.event.post(launch_event)
        self.controller.handle_events()

        mock_launch_bean.assert_called()

        self.controller.logic.state = GameState.MOVING
        pygame.event.post(launch_event)
        self.controller.handle_events()

        mock_launch_bean.assert_called_once()


if __name__ == "__main__":
    unittest.main()
