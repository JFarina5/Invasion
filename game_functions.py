import sys
import pygame

def check_events(ship):
    """Responsible for handling key and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(invasion_settings, screen, ship):
    """Responsible for updating images on screen"""
    # Redraws screen each loop interval
    screen.fill(invasion_settings.bg_color)
    ship.blitme()

    # Make the screen visible
    pygame.display.flip()