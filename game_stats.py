import json


class GameStats:
    """Monitoring game statistics."""

    def __init__(self, ai_settings):
        """Initialisation of statistic data."""
        self.ai_settings = ai_settings
        self.game_active = False
        self.main_buttons_active = True
        self.high_score = [0, 0, 0, 0, 0]
        self.save_file = 'save_file.json'
        self.game_difficulty = ""
        self.reset_stats()

    def reset_stats(self):
        """Initialisation of statistic data which can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_scores(self):
        try:
            with open(self.save_file) as hs:
                self.high_score = json.load(hs)
        except FileNotFoundError:
            with open(self.save_file, 'w') as hs:
                json.dump(self.high_score, hs)

    def save_high_scores(self):
        with open(self.save_file, 'w') as hs:
            json.dump(self.high_score, hs)

