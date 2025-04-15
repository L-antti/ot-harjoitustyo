import unittest
import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, BACKGROUND_COLOR, FONT_COLOR
from game_ui import GameUI


class TestGameUI(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.ui = GameUI(self.screen)

    def test_draw_game_area(self):
        self.ui.draw_game_area()
        color = self.screen.get_at((0, 0))
        self.assertEqual(color, BACKGROUND_COLOR)


if __name__ == "__main__":
    unittest.main()
