"""This class stores all of the settings for Invasion"""


class Settings():

    def __init__(self):
        """Initializing game settings"""
        self.screen_settings()

        self.ship_settings()

        self.bullet_settings()

        # Alien settings
        self.alien_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def screen_settings(self):
        # Screen settings
        self.screen_width = 1100
        self.screen_height = 750
        self.bg_color = (230, 230, 230)

    def ship_settings(self):
        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

    def bullet_settings(self):
        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1

        # Fleet direction
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and points per alien"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
