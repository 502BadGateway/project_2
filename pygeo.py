import pygame
from pygeocoder import Geocoder
import PIL 
import Image
import pyscreenshot as ImageGrab
import time
import webbrowser
import sys 
import urllib


class Geo():
    def __init__(self):
        self.place1 = raw_input("Please input a location: ")
        self.place2 = Geocoder.geocode(self.place1)


        print (self.place2[0])
        print (self.place2[0].coordinates)
        self.place3 = (self.place2[0])
        urlExtention = self.place2[0].coordinates
        print urlExtention


        self.strUrlExt = str(urlExtention)
        self.place4 = str(self.place3)


        self.strUrlExt = self.strUrlExt.replace('(','').replace(')','').replace(' ','')
        print self.strUrlExt


        self.mapsUrl2 = "http://maps.googleapis.com/maps/api/staticmap?center=" + self.strUrlExt + "&zoom=12&format=png&sensor=false&size=640x480&maptype=roadmap&style=element:labels|visibility:off"
        print self.mapsUrl2
        #webbrowser.open_new(mapsUrl2)


        print self.mapsUrl2
        self.resource = urllib.urlopen(self.mapsUrl2)
        self.output = open("screenshot1.png","wb")
        self.output.write(self.resource.read())


        #time.sleep(2)
        pygame.init()
        print pygame.image.get_extended
        imageScreenShot = "screenshot1.png"
        self.background = pygame.image.load(imageScreenShot)
        self.backgroundRect = self.background.get_rect()

        self.size = (width, height) = self.background.get_size()
        self.screen = pygame.display.set_mode(self.size)

        self.screen.blit(self.background, self.backgroundRect)
        pygame.display.flip()

Geo()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()



    