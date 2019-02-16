"""This class stores all of the settings for Invasion"""


class Settings():

    def __init__(self):
        """Initializing game settings"""
        # Screen settings
        self.screen_width = 1100
        self.screen_height = 750
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 1
        self.alien_drop_speed = 10
        # 1 represents right; -1 represents left
        self.fleet_direction = 1
