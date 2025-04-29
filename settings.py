class Settings():
	'''a class to store all the settings'''
	
	def __init__(self):
		'''initialize the game settings'''
		
		#screen settings
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(230,230,230)
		
		#ship settings
		self.ship_speed_factor = 1.5
		
		# Bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 5
		self.bullet_height = 20
		self.bullet_color = 75, 0, 130
		self.bullets_allowed = 10
	
	
