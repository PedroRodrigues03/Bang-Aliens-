"""
HERE I'LL MAKE AN EMPTY PYGAME WINDOW BY CREATING A CLASS TO REPRESENT THE GAME.
"""

import sys

import pygame

from settings import Settings

class BangAliens:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources"""

        # This pygame.init() function initializes the background settings that Pygame needs to work properly
        pygame.init()
        self.settings = Settings()

        # pygame.display.set_mode() creates a display window, on which we'll draw all the game's graphical elements. The argument (1200, 800) is a tuple that defines the dimensions of the game window, which will be 1200 pixels wide by 800 pixels hight. I assign this display window to the attribute self.screen, so it will be available in all methods in the class
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Bang, Aliens!")


    # The game is controlled by the run_game() method. This method contains a while loop that runs continually. The while loop contains an event loop and code that manages screen updates.
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance, and run the game.
    bang_aliens = BangAliens()
    bang_aliens.run_game()