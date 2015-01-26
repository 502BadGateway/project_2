class Landmarks: #this class is what spawns the image
	def __init__ (self, x, y,):
		self.name = None 
		self.treasure = None #tells the robto there isnt any treasreu
		self.locationX = x #the x coodrinate
		self.locationY = y #teh y coordinate
		self.image = "ASSETS/Pyramid.png"  # loads the image of the landmark
		self.infotext = None #loads the text from the wikipedia page
	def noTreasure (self): #desicdes if there is treasure
                self.treasure = False
