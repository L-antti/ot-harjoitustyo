import json
import os


class HighscoreManager:
    def __init__(self, filepath="highscores.json", limit=10):
        self.filepath = filepath
        self.limit = limit
        self.highscores = self.load_scores()

    def load_scores(self):
        """Loads the scores from the file."""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def save_scores(self):
        """Saves the scores to the file."""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.highscores, f, indent=4)

    def add_score(self, name, score):
        """Adds a new score and keeps the top scores."""
        if not name.strip():
            return
        self.highscores.append({"name": name, "score": score})
        self.highscores = sorted(
            self.highscores, key=lambda x: x["score"], reverse=True)[:self.limit]
        self.save_scores()

    def get_scores(self):
        return self.highscores
