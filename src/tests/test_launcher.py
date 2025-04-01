import unittest
from sprites.launcher import Launcher

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

        