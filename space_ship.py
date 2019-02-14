import pygame

class Ship():

    """Initialize ship and set starting position"""
    def __init__(self, screen):
        self.screen = screen

        # Load ship image
        self.image = pygame.image.load('images/space_ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Setting position to bottom/center screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Drawing ship and current location"""
        self.screen.blit(self.image, self.rect)
