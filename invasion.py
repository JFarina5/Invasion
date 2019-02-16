import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from space_ship import Ship
import game_functions as gf


# Initialize game, settings, and screen object
def run_game():
    pygame.init()
    invasion_settings = Settings()
    screen = pygame.display.set_mode((
        invasion_settings.screen_width, invasion_settings.screen_height
    ))
    pygame.display.set_caption("Invasion")

    # Making space ship
    ship = Ship(screen, invasion_settings)

    # Make a group to store bullets in
    bullets = Group()

    # Make a group to store a fleet of aliens
    aliens = Group()

    # Make the fleet of aliens
    gf.create_fleet(invasion_settings, screen, ship, aliens)

    # Start main loop for the game
    while True:
        gf.check_events(invasion_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(invasion_settings, aliens)
        gf.update_screen(invasion_settings, screen, ship, aliens, bullets)


run_game()
