import pygame #imports pygame which is the libary that is being used display everything
from pygeocoder import Geocoder # this libary gets the coordinates that the user searches
import PIL # this is so pygame support PNG
import Image
#import pyscreenshot as ImageGrab
import time
import webbrowser #I think this is now not needed. I will check later. It opens a URL in users default webbrowser 
import sys  
import urllib # this gets the image created by the URL below


class Geo(): #main class
    def __init__(self): # main method
        self.place1 = raw_input("Please input a location: ") # user imputs there desired location
        self.place2 = Geocoder.geocode(self.place1) # geolocation of inputted location is generated


        print (self.place2[0]) # prints out what the geocoder has enterpreted the users input as
        print (self.place2[0].coordinates) # print the geolocation of that location
        self.place3 = (self.place2[0]) # stores location name under a new varibale name, isnt acturlty used but might be later
        urlExtention = self.place2[0].coordinates # stores the locatiuon coordinates under a new variable
        print urlExtention # prints it out to check it is correct, ill prob remove this later


        self.strUrlExt = str(urlExtention) #turns urlExtention into a string
        self.place4 = str(self.place3) #turns place3 into a string


        self.strUrlExt = self.strUrlExt.replace('(','').replace(')','').replace(' ','') # removes brackets and spaces from the coordinates
        print self.strUrlExt # prints it out to so i can see it is correct


        self.mapsUrl2 = "http://maps.googleapis.com/maps/api/staticmap?center=" + self.strUrlExt + "&zoom=16&format=png&sensor=false&size=640x480&maptype=roadmap&style=element:labels|visibility:off"
        # this is the URL that is used to get the iamge, it is created from concatinating in the geolocation coordinateds that are ceated above
    
    def GetsScreenshot(self): # this method gets the background image from the URL crrated above
        print self.mapsUrl2 # prints out the URL so I can check it is correct
        self.resource = urllib.urlopen(self.mapsUrl2) # opens the image from the URL
        self.output = open("screenshot1.png","wb") # save the image
        self.output.write(self.resource.read()) # outputs the image
        
        self.output.close() #Close the resources we opened.
        self.resource.close() #close the image

    def CreatesDisplay(self): # this method should be moved somewhere else
        pygame.init() # intiates pygame
        ExtentionWorking = pygame.image.get_extended() # checks that the needed iamge extention is working
        print ExtentionWorking #prints the result (should be 0)
        imageScreenShot = "screenshot1.png" # stores the images name under a variable
        self.background = pygame.image.load(imageScreenShot) # loads the image
        self.backgroundRect = self.background.get_rect() # creates the background

        self.size = (width, height) = self.background.get_size() # makes the window the same size as the background image
        self.screen = pygame.display.set_mode(self.size) # sets the size

        self.screen.blit(self.background, self.backgroundRect)	# blits the display to load everything onto it
        pygame.display.flip() #refreshes the display so everything is outputted

geo1 = Geo() # calls the class
geo1.GetsScreenshot() # calls the method
geo1.CreatesDisplay() # calls the methos

while 1: #loops the display so it stays open,this will be removed later
    for event in pygame.event.get():
        if event.type == pygame.quit: 
            pygame.quit()
            sys.exit()







    
    
