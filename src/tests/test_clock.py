import unittest
from unittest.mock import MagicMock
from clock import Clock


class TestClock(unittest.TestCase):
    def test_tick_called_with_correct_fps(self):
        clock = Clock()

        clock.clock = MagicMock()

        fps = 60
        clock.tick(fps)

        clock.clock.tick.assert_called_once_with(fps)


if __name__ == "__main__":
    unittest.main()
