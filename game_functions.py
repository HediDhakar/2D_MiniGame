import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""Respond to keypresses"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT :
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
	"""Fire a bullet if limit not reached yet."""
	# Create a new bullet and add it to the bullets group.
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet) 

def check_keyup_events(event, ship):
	"""Respond to key releases"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	"""Respond to keypresses and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship ,aliens ,bullets):
	"""Update images on the screen and flip to the new screen"""
	# Redraw the screen during each pass through the loop.
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	aliens.draw(screen)
	
	# Make the most recently drawn screen visible
	pygame.display.flip()
	
	# Redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	
	# Make the most recently drawn screen visible
	pygame.display.flip()
	
	
def update_bullets(bullets):
	"""Update position of bullets and get rid of old bullets."""
	# Update bullet positions.
	bullets.update()
	
	# Get rid of bullets that have disappeared.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
			

def create_fleet(ai_settings, screen, aliens):
    """Create a full fleet of aliens from left to right, with no space between them."""
    # Create an alien and find the number of aliens that fit horizontally in a row.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width  # Use the full screen width
    number_aliens_x = int(available_space_x / alien_width)  # Calculate how many aliens fit in a row without extra space

    # Create the aliens in a horizontal line, directly next to each other.
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width * alien_number  # Position each alien directly next to the previous one
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height  # Keep the y-position fixed (top of the screen)
        aliens.add(alien)


