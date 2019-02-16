import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, invasion_settings, screen, ship, bullets):
    """Responds to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(invasion_settings, screen, ship, bullets)

def fire_bullet(invasion_settings, screen, ship, bullets):
    """Fire bullet if there is less than three bullets on the screen"""
    # Create a new bullet and add to bullet group
    if len(bullets) < invasion_settings.bullets_allowed:
        new_bullet = Bullet(invasion_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Responds to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(invasion_settings, screen, ship, bullets):
    """Responsible for handling key and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, invasion_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(invasion_settings, screen, ship, bullets):
    """Responsible for updating images on screen"""
    # Redraws screen each loop interval
    screen.fill(invasion_settings.bg_color)
    ship.blitme()
    # Redraws all bullets from ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets"""
    # Update bullet positions
    bullets.update()

    # Get rid of bullets that have left the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        print(len(bullets))


    # Make the screen visible
    pygame.display.flip()
