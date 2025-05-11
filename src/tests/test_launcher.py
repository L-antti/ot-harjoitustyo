import unittest
import math
from sprites.launcher import Launcher
from settings import BEAN_DEFAULT_SPEED


class TestLauncher(unittest.TestCase):
    def setUp(self):
        self.launcher = Launcher((200, 400))

    def test_launcher_initialization(self):
        self.assertEqual(self.launcher.position, (200, 400))
        self.assertEqual(self.launcher.angle, 90)

    def test_launcher_rotation(self):
        self.launcher.rotate(-10)
        self.assertEqual(self.launcher.angle, 80)

        self.launcher.rotate(200)
        self.assertEqual(self.launcher.angle, 170)

        self.launcher.rotate(-200)
        self.assertEqual(self.launcher.angle, 10)

    def test_get_launcher_velocity(self):
        self.launcher.angle = 45
        velocity = self.launcher.get_launch_velocity()
        expected_velocity = [
            BEAN_DEFAULT_SPEED * math.cos(math.radians(45)),
            -BEAN_DEFAULT_SPEED * math.sin(math.radians(45))
        ]
        self.assertAlmostEqual(velocity[0], expected_velocity[0], places=5)
        self.assertAlmostEqual(velocity[1], expected_velocity[1], places=5)


if __name__ == "__main__":
    unittest.main()
