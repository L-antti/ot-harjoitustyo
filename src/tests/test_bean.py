import unittest
import math
import pygame
from sprites.bean import Bean
from settings import SCREEN_WIDTH


class TestBean(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.bean = Bean((128, 0, 128), (200, 400))

    def tearDown(self):
        pygame.quit()

    def test_shoot(self):
            self.bean.shoot(45)
            expected_velocity = [5 * math.cos(math.radians(45)), -5 * math.sin(math.radians(45))]
            self.assertAlmostEqual(self.bean.velocity[0], expected_velocity[0])
            self.assertAlmostEqual(self.bean.velocity[1], expected_velocity[1])

    def test_bounce_off_walls(self):
        self.bean.rect.left = 0
        self.bean.velocity = [-3, 0]
        self.bean.update([])
        self.assertEqual(self.bean.velocity[0], 3)

        self.bean.rect.right = SCREEN_WIDTH
        self.bean.velocity = [3, 0]
        self.bean.update([])
        self.assertEqual(self.bean.velocity[0], -3) 

    def test_attach_to_the_top(self):
        self.bean.rect.top = 0
        self.bean.velocity = [3, 0]
        self.bean.update([])
        self.assertEqual(self.bean.velocity[0], 0)


if __name__ == "__main__":
    unittest.main()