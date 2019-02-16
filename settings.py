"""This class stores all of the settings for Invasion"""
class Settings():

    def __init__(self):
        """Initializing game settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 650
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 0.5

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3