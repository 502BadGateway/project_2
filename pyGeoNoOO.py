from pygeocoder import Geocoder
from PIL import Image
import pyscreenshot as ImageGrab
import time
import webbrowser
import sys 
import pygame
import urllib


place1 = raw_input("Please input a location: ")
place2 = Geocoder.geocode(place1)


print (place2[0])
print (place2[0].coordinates)
place3 = (place2[0])
urlExtention = place2[0].coordinates
print urlExtention


strUrlExt = str(urlExtention)
place4 = str(place3)


strUrlExt = strUrlExt.replace('(','').replace(')','').replace(' ','')
print strUrlExt


mapsUrl2 = "http://maps.googleapis.com/maps/api/staticmap?center=" + strUrlExt + "&zoom=12&format=png&sensor=false&size=640x480&maptype=roadmap&style=element:labels|visibility:off"
print mapsUrl2

resource = urllib.urlopen(mapsUrl2)
output = open("screenshot1.png","wb")
output.write(resource.read())

#ImgToConvert = "screenshot1.jpg"
#img = Image.open(ImgToConvert)
#r, g, b, a = img.split()
#img = Image.merge("RGB", (r, g, b))
#img.save("screenshot1.bmp")

pygame.init()
print pygame.image.get_extended()
#imageScreenShot = "screenshot1.jpg"
background = pygame.image.load("screenshot1.png")
backgroundRect = background.get_rect()

size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

screen.blit(background, backgroundRect)
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

