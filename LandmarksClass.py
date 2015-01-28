class Landmarks: #this class is what spawns the image
	def __init__ (self, x, y, treasure, name, image):
		self.name = name 
		self.treasure = treasure #tells the robot there isn't any treasre
		self.locationX = x #the x coodrinate
		self.locationY = y #the y coordinate
		self.image = "ASSETS/"+str(image)  # loads the image of the landmark
		self.infotext = None #loads the text from the wikipedia page
	def noTreasure (self): #decides if there is treasure
                self.treasure = False
