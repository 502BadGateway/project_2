class Landmarks:
	def __init__ (self, name, x, y, image, infotext, treasure=False):
		self.name = name 
		self.treasure = teasure 
		self.locationX = x
		self.locationY = y
		self.image = image 
		self.infotext = infotext 
	def noTreasure (self):
                self.treasure = False
