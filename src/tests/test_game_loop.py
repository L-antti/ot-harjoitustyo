import unittest
from unittest.mock import MagicMock
from controller.game_loop import GameLoop
from game_state import GameState


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.logic = MagicMock()
        self.logic.state = GameState.IDLE

        self.renderer = MagicMock()
        self.gameover = MagicMock()
        self.clock = MagicMock()

    def test_run_does_not_update_when_idle(self):
        events = MagicMock()
        events.in_menu = False
        events.process_events.return_value = False

        events.running = True

        def stop_running():
            events.running = False
        self.gameover.handle_game_over.side_effect = stop_running

        loop = GameLoop(
            self.logic,
            events,
            self.renderer,
            self.gameover,
            self.clock
        )

        loop.run()

        self.logic.update_game_state.assert_not_called()
        self.gameover.handle_game_over.assert_called_once()
        self.renderer.render_game_view.assert_called_once()
        self.clock.tick.assert_called_once()


if __name__ == "__main__":
    unittest.main()
