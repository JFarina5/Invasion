# import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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

    aliens, bullets, play_button, sb, ship, stats = instances(invasion_settings, screen)

    # Make the fleet of aliens
    gf.create_fleet(invasion_settings, screen, ship, aliens)

    # Start main loop for the game
    while True:
        gf.check_events(invasion_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(invasion_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(invasion_settings, screen, stats, sb, ship, aliens,
                             bullets)
        gf.update_screen(invasion_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)


def instances(invasion_settings, screen):
    # Make the play button
    play_button = Button(invasion_settings, screen, "Play")
    # Create an instance to store game stats and create a scoreboard
    stats = GameStats(invasion_settings)
    sb = Scoreboard(invasion_settings, screen, stats)
    # Making space ship
    ship = Ship(invasion_settings, screen)
    # Make a group to store bullets in
    bullets = Group()
    # Make a group to store a fleet of aliens
    aliens = Group()
    return aliens, bullets, play_button, sb, ship, stats


run_game()
