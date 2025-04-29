import unittest
import pygame
from sprites.bean import Bean


class TestBean(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.bean = Bean((255, 0, 0), (0, 0))
        self.neighbour_bean = Bean((0, 255, 0), (10, 10))
        self.far_bean = Bean((0, 0, 255), (100, 100))
        self.beans_group = pygame.sprite.Group()

    def test_update_neighbours(self):
        self.beans_group.add(self.bean)
        self.beans_group.add(self.neighbour_bean)
        self.beans_group.add(self.far_bean)

        self.bean.update_neighbours(self.beans_group)

        self.assertIn(self.neighbour_bean, self.bean.neighbours)
        self.assertNotIn(self.far_bean, self.bean.neighbours)

    def test_attach(self):
        initial_position = self.bean.rect.topleft
        self.bean.attach(self.beans_group)
        self.assertIn(self.bean, self.beans_group)

        self.bean.update_neighbours(self.beans_group)

        self.assertTrue(len(self.bean.neighbours) >= 0)
        self.assertEqual(self.bean.rect.topleft, initial_position)


if __name__ == "__main__":
    unittest.main()
