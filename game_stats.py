class GameStats:
    """Track stats for Bang, Aliens!"""

    def __init__(self, ba_game):
        """Initialize statistics"""
        self.settings = ba_game.settings
        self.reset_stats()

        #Start Bang, Aliens! in an inactive state
        self.game_active = False

        #Hight score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1