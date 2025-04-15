import unittest
from unittest.mock import MagicMock
from game_logic import GameLogic
from game_state import GameState


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.mock_area = MagicMock()
        self.mock_area.add_new_row = MagicMock()
        self.mock_area.update = MagicMock()
        self.game_logic = GameLogic(self.mock_area)

    def test_update_game_state_game_over(self):
        self.game_logic.state = GameState.GAME_OVER
        self.game_logic.update_game_state()
        self.mock_area.add_new_row.assert_not_called()

    def test_update_game_state_check_game_over(self):
        self.game_logic.state = GameState.LAUNCHING
        self.game_logic.check_game_over = MagicMock(return_value=True)
        self.game_logic.update_game_state()
        self.mock_area.add_new_row.assert_not_called()

    def test_update_game_state_idle(self):
        self.game_logic.state = GameState.IDLE
        self.game_logic.update_game_state()
        self.mock_area.add_new_row.assert_not_called()

    def test_update_game_state_continue_to_add_row(self):
        self.game_logic.state = GameState.ADDING_ROW
        self.game_logic.check_game_over = MagicMock(return_value=False)
        self.game_logic.update_game_state()
        self.mock_area.add_new_row.assert_called_once()
        self.assertEqual(self.game_logic.state, GameState.IDLE)

    def test_transition_state(self):
        self.game_logic.transition_state(GameState.MOVING)
        self.assertEqual(self.game_logic.state, GameState.MOVING)


if __name__ == "__main__":
    unittest.main()
