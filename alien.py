import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """This class represents a single alien"""

    def __init__(self, invasion_settings, screen):
        """Initialize alien and starting poisiton"""
        super().__init__()
        self.screen = screen
        self.invasion_settings = invasion_settings

        # Load alien image
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Start each alien near top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien in current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return true if aliens are at edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move alien to the right or left"""
        self.x += (self.invasion_settings.alien_speed *
                   self.invasion_settings.fleet_direction)
        self.rect.x = self.x
