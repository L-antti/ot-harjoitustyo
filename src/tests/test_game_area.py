import unittest
import pygame
from game_area import GameArea
from settings import BEAN_COLORS


class TestGameArea(unittest.TestCase):
    def setUp(self):

        pygame.init()
        self.game_area = GameArea()

    def test_initialize_predefined_beans(self):
        self.assertGreater(len(self.game_area.beans), 0)

        for bean in self.game_area.beans:
            self.assertTrue(bean.rect.x >= 0 and bean.rect.y >= 0)

    def test_get_next_bean(self):
        initial_bean_count = len(self.game_area.bean_queue)
        next_bean = self.game_area.get_next_bean()
        self.assertIn(next_bean, BEAN_COLORS)
        self.assertEqual(len(self.game_area.bean_queue), initial_bean_count)

    def test_add_new_row(self):
        initial_bean_count = len(self.game_area.beans)
        self.game_area.add_new_row()
        self.assertGreater(len(self.game_area.beans), initial_bean_count)


if __name__ == "__main__":
    unittest.main()
