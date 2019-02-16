import pygame


class Ship():
    """Initialize ship and set starting position"""

    def __init__(self, screen, invasion_settings):
        self.screen = screen
        self.invasion_settings = invasion_settings

        # Load ship image
        self.image = pygame.image.load('images/space_ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Setting position to bottom/center screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store decimal value for ship's center
        self.center = float(self.rect.centerx)

        # Moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship's position based on movement flag"""
        # Updating ship's center value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.invasion_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.invasion_settings.ship_speed_factor

        # Update from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Drawing ship and current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx
