import pygame

class Ship():
	def __init__(self,ai_settings,screen):
		"""Initialize the ship and set its starting position"""
		self.screen=screen
		self.ai_settings=ai_settings
		#Load the ship image
		self.image=pygame.image.load("C:\Games\AlienInvasion\images\space-ship-148536_1280.bmp")
		 
		# Scale the image
		self.image = pygame.transform.scale(self.image, (60, 80))
		
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#Start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom  
		
		# Store a decimal value for the ship's center.
		self.center = float(self.rect.centerx)
		
		
		#Movement flag
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		"""Update the ship's position based on the movement flag."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
			
		# Update rect object from self.center.
		self.rect.centerx = self.center

	def blitme(self):
		'''draw the ship at the current location'''
		self.screen.blit(self.image,self.rect)
		



