from pygeocoder import Geocoder
import pyscreenshot as ImageGrab
import time
import webbrowser
import sys 
import pygame
import urllib


class Geo():
    def __init__(self):
        self.place1 = raw_input("Please input a location: ")
        self.place2 = Geocoder.geocode(place1)


        print (self.place2[0])
        print (self.place2[0].coordinates)
        self.place3 = (place2[0])
        urlExtention = place2[0].coordinates
        print urlExtention


        self.strUrlExt = str(urlExtention)
        self.place4 = str(place3)


        self.strUrlExt = strUrlExt.replace('(','').replace(')','').replace(' ','')
        print self.strUrlExt


        self.mapsUrl2 = "http://maps.googleapis.com/maps/api/staticmap?center=" + self.strUrlExt + "&zoom=12&format=png&sensor=false&size=640x480&maptype=roadmap&style=element:labels|visibility:off"
        print self.mapsUrl2
        #webbrowser.open_new(mapsUrl2)


class imageDownload():
    def __init__(self,Geo):
        print Geo.mapsUrl2
        self.resource = urllib.urlopen(Geo.mapsUrl2)
        self.output = open("screenshot1.jpg","wb")
        self.output.write(resource.read())

class displayCreate():
    def __init__(self):
        pygame.init()
        self.background = pygame.image.load("screenshot1.jpg")
        self.backgroundRect = background.get_rect()

        self.size = (width, height) = background.get_size()
        self.screen = pygame.display.set_mode(self.size)

        screen.blit(background, backgroundRect)
        pygame.display.flip()

Geo()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()



    