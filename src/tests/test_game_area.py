import unittest
from mechanics.game_area import GameArea
from sprites.bean import Bean
from settings import BEAN_COLORS


class TestGameArea(unittest.TestCase):
    def setUp(self):
        self.game_area = GameArea()

    def test_initialize_predefined_beans(self):
        self.assertGreater(len(self.game_area.beans), 0)

        for bean in self.game_area.beans:
            self.assertTrue(bean.rect.x >= 0 and bean.rect.y >= 0)

    def test_attach_bean(self):
        initial_count = len(self.game_area.beans)
        new_bean = Bean((255, 255, 0), (100, 100))
        self.game_area.attach_bean(new_bean)

        self.assertIn(new_bean, self.game_area.beans)
        self.assertEqual(len(self.game_area.beans), initial_count + 1)

    def test_get_next_bean(self):
        initial_bean_count = len(self.game_area.bean_queue)
        next_bean = self.game_area.get_next_bean()
        self.assertIn(next_bean, BEAN_COLORS)
        self.assertEqual(len(self.game_area.bean_queue), initial_bean_count)

    def test_add_new_row_updates_neighbours(self):
        self.game_area.add_new_row()
        all_neighbour_sets = [len(bean.neighbours)
                              for bean in self.game_area.beans]
        self.assertTrue(any(count > 0 for count in all_neighbour_sets))

    def test_get_next_bean_color(self):
        color = self.game_area.get_next_bean_color()
        self.assertIn(color, BEAN_COLORS)


if __name__ == "__main__":
    unittest.main()
