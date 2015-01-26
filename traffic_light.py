import pygame
import time

class trafficLights:
    def __init__(self, x, y):
        self.locationX = x 
        self.locationY = y
        self.image = "ASSETS/red.png"
        self.red = False

    def changeLight(self):
        #CHANGE .red TO FALSE
        self.red = False
        #CHANGE REDIMAGE TO GREEN IMAGE
        self.image = "ASSETS/green.png"
        #WAIT FIVE SECONDS
        time.sleep(5)
        #CHANGE .red to TRUE
        self.red = True
        #CHANGE GREEN IMAGE TO RED
        self.image = "ASSETS/red.png"

    def get_state(self): #Return the state of the light
        return self.red

    def getImage(self):  #Return the image for the light
        return self.image

    def getLocationX(self):   #Return the locations
        return self.locatonX

    def getLocationY(self):
        return self.locatonY
        
