class Landmarks:
	def __init__ (self, x, y,):
		self.name = None 
		self.treasure = None 
		self.locationX = x
		self.locationY = y
		self.image = "ASSETS/Pyramid.png" 
		self.infotext = None 
	def noTreasure (self):
                self.treasure = False
