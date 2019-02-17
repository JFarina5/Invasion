import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class handels bullets fired from ship"""

    def __init__(self, invasion_settings, screen, ship):
        super().__init__()
        self.screen = screen

        self.bullet_position(invasion_settings, ship)

        self.color = invasion_settings.bullet_color
        self.speed = invasion_settings.bullet_speed

    def bullet_position(self, invasion_settings, ship):
        # Create bullet at (0, 0) then correct position
        self.rect = pygame.Rect(0, 0, invasion_settings.bullet_width, invasion_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Store bullet position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet up the screen"""
        # Update decimal position of bullet
        self.y -= self.speed
        # Update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
