import sys
import pygame

def check_events():
    """Responsible for handling key and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(invasion_settings, screen, ship):
    """Responsible for updating images on screen"""
    # Redraws screen each loop interval
    screen.fill(invasion_settings.bg_color)
    ship.blitme()

    # Make the screen visible
    pygame.display.flip()