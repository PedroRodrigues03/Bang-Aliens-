import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ba_game):
        """Initializate the ship and set its starting position"""
        self.screen = ba_game.screen
        self.settings = ba_game.settings
        self.screen_rect = ba_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship2.png').convert()
        self.image.set_colorkey((0, 0, 35))
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store decimals value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement Flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x
        self.rect.x = self.x
    
    def blitem(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)