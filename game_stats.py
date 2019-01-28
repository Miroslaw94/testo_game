class GameStats:
    """Monitoring game statistics."""

    def __init__(self, ai_settings):
        """Initialisation of statistic data."""
        self.ai_settings = ai_settings
        self.game_active = False
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        """Initialisation of statistic data which can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

