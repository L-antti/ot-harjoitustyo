import unittest
import pygame
from sprites.bean import Bean


class TestBean(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.bean = Bean((255, 0, 0), (100, 100))

    def test_bean_initialization(self):
        self.assertEqual(self.bean.color, (255, 0, 0))
        self.assertEqual(self.bean.rect.center, (100, 100))
        self.assertEqual(self.bean.velocity, [0, 0])
        self.assertEqual(len(self.bean.neighbours), 0)

    def test_bean_movement(self):
        self.bean.set_velocity(45)
        initial_position = self.bean.rect.center
        self.bean.rect.x += self.bean.velocity[0]
        self.bean.rect.y += self.bean.velocity[1]
        self.assertNotEqual(self.bean.rect.center, initial_position)

    def test_move_updates_position(self):
        self.bean.set_velocity(50)
        initial_position = self.bean.rect.copy()
        self.bean.move()
        self.assertNotEqual(self.bean.rect.topleft, initial_position.topleft)

    def test_has_collided_hits_top(self):
        self.bean.rect.top = -1
        beans_group = pygame.sprite.Group()
        self.assertTrue(self.bean.has_collided(beans_group))

    def test_has_collided_with_other_bean(self):
        other_bean = Bean((0, 255, 0), (105, 100))
        beans_group = pygame.sprite.Group(other_bean)
        self.assertTrue(self.bean.has_collided(beans_group))

    def test_has_not_collided(self):
        far_bean = Bean((0, 255, 0), (300, 300))
        beans_group = pygame.sprite.Group(far_bean)
        self.assertFalse(self.bean.has_collided(beans_group))


if __name__ == "__main__":
    unittest.main()
