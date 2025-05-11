import unittest
import pygame
from mechanics.game_logic import GameLogic
from game_state import GameState
from sprites.bean import Bean
from settings import MAX_Y


class DummyGameArea:
    def __init__(self):
        self.beans = pygame.sprite.Group()
        self.update_called = False
        self.row_added = False
        self.bean_queue = [(255, 0, 0)]
        self.reset_called = False

    def get_next_bean(self):
        return self.bean_queue[0]

    def attach_bean(self, bean):
        self.beans.add(bean)

    def update(self):
        self.update_called = True

    def add_new_row(self):
        self.row_added = True

    def reset(self):
        self.reset_called = True


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.area = DummyGameArea()
        self.logic = GameLogic(self.area)

    def test_check_game_over_true(self):
        bean = Bean((255, 0, 0), (100, MAX_Y))
        bean.rect.bottom = MAX_Y
        self.area.beans.add(bean)

        result = self.logic.check_game_over()
        self.assertTrue(result)
        self.assertEqual(self.logic.state, GameState.GAME_OVER)

    def test_check_game_over_false(self):
        bean = Bean((255, 0, 0), (100, 100))
        bean.rect.bottom = 100
        self.area.beans.add(bean)

        result = self.logic.check_game_over()
        self.assertFalse(result)
        self.assertNotEqual(self.logic.state, GameState.GAME_OVER)

    def test_evaluate_bean_triggers_row_add(self):
        bean = Bean((255, 0, 0), (100, 100))
        self.logic.current_bean = bean
        self.logic.failed_shots = 2

        self.logic.get_connected_same_color = lambda b: [bean] * 2

        self.logic.evaluate_bean()

        self.assertEqual(self.logic.state, GameState.ADDING_ROW)
        self.assertTrue(self.area.row_added or self.logic.failed_shots == 0)

    def test_get_connected_same_color_returns_all_connected(self):
        b1 = Bean((255, 0, 0), (0, 0))
        b2 = Bean((255, 0, 0), (40, 0))
        b3 = Bean((255, 0, 0), (80, 0))

        b1.neighbours = [b2]
        b2.neighbours = [b3]

        result = self.logic.get_connected_same_color(b1)
        self.assertCountEqual(result, [b1, b2, b3])

    def test_transition_state_reset_failed_shots(self):
        self.logic.failed_shots = 3
        self.logic.transition_state(GameState.IDLE, reset_failed_shots=True)
        self.assertEqual(self.logic.failed_shots, 0)

    def test_reset_game(self):
        self.logic.state = GameState.LAUNCHING
        self.logic.score = 50
        self.logic.failed_shots = 1
        self.logic.current_bean = Bean((255, 0, 0), (100, 100))

        self.logic.reset_game()

        self.assertEqual(self.logic.state, GameState.IDLE)
        self.assertIsNone(self.logic.current_bean)
        self.assertEqual(self.logic.score, 0)
        self.assertEqual(self.logic.failed_shots, 0)
        self.assertTrue(self.logic.game_area.reset_called)


if __name__ == "__main__":
    unittest.main()
