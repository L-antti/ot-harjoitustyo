import unittest
from unittest.mock import MagicMock
from game_logic import GameLogic
from game_state import GameState
from sprites.bean import Bean
from settings import MAX_Y


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.mock_area = MagicMock()
        self.mock_area.beans = set()
        self.game_logic = GameLogic(self.mock_area)

    def test_check_game_over_collision(self):
        self.mock_area.beans = [MagicMock(rect=MagicMock(bottom=MAX_Y))]
        self.assertTrue(self.game_logic.check_game_over())

    def test_launch_next_bean_not_idle(self):
        self.game_logic.state = GameState.MOVING
        self.game_logic.launch_next_bean(MagicMock())
        self.assertIsNone(self.game_logic.current_bean)

    def test_launch_next_bean_when_idle(self):
        self.mock_area.get_next_bean = MagicMock(return_value=(255, 0, 0))
        self.game_logic.state = GameState.IDLE
        launcher_mock = MagicMock(angle=45)

        self.game_logic.launch_next_bean(launcher_mock)
        self.assertIsInstance(self.game_logic.current_bean, Bean)
        self.assertEqual(self.game_logic.state, GameState.MOVING)

    def test_evaluate_bean_failed_shot(self):
        bean_mock = MagicMock()
        self.game_logic.get_connected_same_color = MagicMock(
            return_value=[bean_mock] * 2)

        self.game_logic.failed_shots = 2
        self.game_logic.current_bean = bean_mock
        self.game_logic.evaluate_bean()

        self.assertEqual(self.game_logic.state, GameState.ADDING_ROW)

    def test_move_current_bean(self):
        bean_mock = MagicMock()
        bean_mock.rect.x = 100
        bean_mock.rect.y = 5
        bean_mock.velocity = [0, -5]
        bean_mock.rect.top = 0
        bean_mock.rect.left = 10
        bean_mock.rect.right = 50

        self.game_logic.current_bean = bean_mock
        self.game_logic.state = GameState.MOVING

        with unittest.mock.patch('pygame.sprite.spritecollide', return_value=[]):
            self.game_logic.move_current_bean()

        self.assertEqual(self.game_logic.state, GameState.EVALUATING)
        self.assertEqual(bean_mock.velocity, [0, 0])
        bean_mock.attach.assert_called_once()
        bean_mock.update_neighbours.assert_called_once()

    def test_transition_state_resets_failed_shots(self):
        self.game_logic.failed_shots = 2
        self.game_logic.transition_state(
            GameState.IDLE, reset_failed_shots=True)
        self.assertEqual(self.game_logic.failed_shots, 0)

    def test_get_connected_same_color(self):
        bean_mock = MagicMock(color=(255, 0, 0))
        neighbour_mock = MagicMock(color=(255, 0, 0))
        second_neighbour_mock = MagicMock(color=(255, 0, 0))
        bean_mock.neighbours = [neighbour_mock]
        neighbour_mock.neighbours = [second_neighbour_mock]

        result = self.game_logic.get_connected_same_color(bean_mock)

        self.assertIn(bean_mock, result)
        self.assertIn(neighbour_mock, result)
        self.assertIn(second_neighbour_mock, result)
        self.assertEqual(len(result), 3)


if __name__ == "__main__":
    unittest.main()
