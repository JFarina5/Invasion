class GameStats():
    """Track statistics for Invasion"""

    def __init__(self, invasion_settings):
        """Initialize statistcs"""
        self.invasion_settings = invasion_settings
        self.reset_stats()

        # Start invasion in an active state
        self.game_active = True

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.ships_left = self.invasion_settings.ship_limit