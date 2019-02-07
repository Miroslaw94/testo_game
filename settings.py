class Settings:
    """Class for settings of the game."""

    def __init__(self):
        """Settings initialisation."""
        self.screen_width = 1200
        self.screen_height = 760
        self.bg_color = (230, 230, 230)

        self.ship_limit = 3

        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 225, 40, 00
        self.bullets_allowed = 10

        self.fleet_drop_speed = 15

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialization of settings which will change during the game."""
        self.ship_speed_factor = 4.5
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 2
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Change of speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor += 1
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

