import unittest
import pygame
from unittest.mock import MagicMock
from controller.event_handler import EventHandler
from game_state import GameState


class TestEventHandler(unittest.TestCase):
    def setUp(self):
        self.launcher = MagicMock()
        self.logic = MagicMock()
        self.handler = EventHandler(self.launcher, self.logic)

    def test_space_key_starts_game(self):
        self.handler.in_menu = True

        space_event = pygame.event.Event(
            pygame.KEYDOWN, {"key": pygame.K_SPACE})

        original_event_get = pygame.event.get
        pygame.event.get = lambda: [space_event]

        result = self.handler.process_events()

        self.assertFalse(self.handler.in_menu)
        self.assertTrue(result)

        pygame.event.get = original_event_get

    def test_up_key_launches_bean_when_game_is_idle(self):
        self.handler.in_menu = False
        self.logic.state = GameState.IDLE

        up_event = pygame.event.Event(
            pygame.KEYDOWN, {"key": pygame.K_UP})

        original_event_get = pygame.event.get
        pygame.event.get = lambda: [up_event]

        result = self.handler.process_events()

        self.logic.launch_next_bean.assert_called_once_with(self.launcher)
        self.assertFalse(result)

        pygame.event.get = original_event_get


if __name__ == "__main__":
    unittest.main()
