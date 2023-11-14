class GameStats:
    """Track stats for Bang, Aliens!"""

    def __init__(self, ba_game):
        """Initialize statistics"""
        self.settings = ba_game.settings
        self.reset_stats()

        #Start Bang, Aliens! in an active state
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit