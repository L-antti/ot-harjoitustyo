import unittest
from unittest.mock import patch, MagicMock
from repository.highscore_manager import HighscoreManager


class TestHighscoreManager(unittest.TestCase):
    @patch("builtins.open", new_callable=MagicMock)
    def test_add_score_keeps_top_scores(self, mock_open):
        manager = HighscoreManager(filepath="test_highscores.json", limit=3)

        manager.highscores = [
            {"name": "Player1", "score": 150},
            {"name": "Player2", "score": 100},
            {"name": "Player3", "score": 50}
        ]

        manager.add_score("Player4", 200)

        self.assertEqual(len(manager.highscores), 3)
        self.assertEqual(manager.highscores[0]["name"], "Player4")
        self.assertEqual(manager.highscores[0]["score"], 200)

        self.assertEqual(manager.highscores[2]["name"], "Player2")

    @patch("builtins.open", new_callable=MagicMock)
    def test_add_score_does_not_add_empty_name(self, mock_open):
        manager = HighscoreManager(filepath="test_highscores.json")
        manager.add_score("", 100)
        self.assertEqual(len(manager.highscores), 0)
        mock_open.assert_not_called()


if __name__ == "__main__":
    unittest.main()
