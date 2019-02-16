import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, invasion_settings, screen, ship, bullets):
    """Responds to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(invasion_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(invasion_settings, screen, ship, bullets):
    """Fire bullet if there is less than five bullets on the screen"""
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


def update_screen(invasion_settings, screen, ship, aliens, bullets):
    """Responsible for updating images on screen"""
    # Redraws screen each loop interval
    screen.fill(invasion_settings.bg_color)

    ship.blitme()
    aliens.draw(screen)
    # Redraws all bullets from ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()


def update_bullets(invasion_settings, screen, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets"""
    # Update bullet positions
    bullets.update()

    # Get rid of bullets that have left the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        print(len(bullets))

    check_bullet_collision(invasion_settings, screen, ship, aliens, bullets)

    # Make the screen visible
    pygame.display.flip()


def check_bullet_collision(invasion_settings, screen, ship, aliens, bullets):
    """Respond to bullet-alien collision"""
    # Remove any bullets and aliens that collide
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet
        bullets.empty()
        create_fleet(invasion_settings, screen, ship, aliens)


def get_number_aliens_x(invasion_settings, alien_width):
    available_space_x = invasion_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(invasion_settings, ship_height, alien_height):
    """Determining the number of rows of aliens that fit screen"""
    available_space_y = (invasion_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(invasion_settings, screen, aliens, alien_number, row_number):
    """Create alien and place it in a row"""
    alien = Alien(invasion_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(invasion_settings, screen, ship, aliens):
    """Creating a fleet of aliens"""
    # Create an alien and find number of aliens in the row
    # Spacing is equal to one alien width
    alien = Alien(invasion_settings, screen)
    number_aliens_x = get_number_aliens_x(invasion_settings, alien.rect.width)
    number_rows = get_number_rows(invasion_settings, ship.rect.height,
                                  alien.rect.height)

    # Create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(invasion_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(invasion_settings, aliens):
    """Responds if any aliens have reached the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(invasion_settings, aliens)
            break


def change_fleet_direction(invasion_settings, aliens):
    """Drop fleet and change direction"""
    for alien in aliens.sprites():
        alien.rect.y += invasion_settings.alien_drop_speed
    invasion_settings.fleet_direction *= -1


def ship_hit(invasion_settings, stats, screen, ship, aliens, bullets):
    """Responds to ship being hit"""
    if stats.ships_left > 0:
        # Subtracts from ships left
        stats.ships_left -= 1

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center ship
        create_fleet(invasion_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)

    else:
        stats.game_active = False


def check_aliens_bottom(invasion_settings, stats, screen, ship, aliens, bullets):
    """Checks to see if any aliens are at the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treated as if ship was hit
            ship_hit(invasion_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(invasion_settings, stats, screen, ship, aliens, bullets):
    """Update alien fleet position"""
    check_fleet_edges(invasion_settings, aliens)
    aliens.update()

    # Look for alien-ship collision
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(invasion_settings, stats, screen, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen
    check_aliens_bottom(invasion_settings, stats, screen, ship, aliens, bullets)
