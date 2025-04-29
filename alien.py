import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""
	def __init__(self, ai_settings, screen):
		"""Initialize the alien and set its starting position."""
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		# Load the alien image and set its rect attribute.
		self.image = pygame.image.load("C:\\Games\\AlienInvasion\\images\\faysal.bmp")
		self.rect = self.image.get_rect()
		
		# Scale the image
		self.image = pygame.transform.scale(self.image, (60, 80))
		
		
		
		# Start each new alien near the top left of the screen.
		self.rect.x = 0
		self.rect.y = 0
		
	def blitme(self):
		"""Draw the alien at its current location."""
		self.screen.blit(self.image, self.rect)

