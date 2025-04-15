import unittest
import pygame
from sprites.bean import Bean


class TestBean(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.bean = Bean((255, 0, 0), (0, 0))
        # Luo naapuripapu lähelle
        self.neighbour_bean = Bean((0, 255, 0), (10, 10))
        self.far_bean = Bean((0, 0, 255), (100, 100))
        self.beans_group = pygame.sprite.Group()

    def tearDown(self):
        pygame.quit()

    def test_update_neighbours(self):

        beans_group = pygame.sprite.Group()
        beans_group.add(self.bean)
        beans_group.add(self.neighbour_bean)
        beans_group.add(self.far_bean)

        self.bean.update_neighbours(beans_group)

        self.assertIn(self.neighbour_bean, self.bean.neighbours)
        self.assertNotIn(self.far_bean, self.bean.neighbours)

    def test_attach(self):
        self.bean.attach(self.beans_group)

        self.assertIn(self.bean, self.beans_group)

        self.bean.update_neighbours(self.beans_group)
        self.assertTrue(len(self.bean.neighbours) >= 0)


if __name__ == "__main__":
    unittest.main()
