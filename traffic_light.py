import pygame
import time
import random

class trafficLights:
    def __init__(self, x, y):
        self.state = 3
        self.locationX = x 
        self.locationY = y
        self.image = "ASSETS/red.png"
        self.red = False

    def changeLight(self):
        rand  = random.randint(0,10)
        print rand
        if rand < 3:
            self.image = "ASSETS/red.png"
            self.red = True 
            self.state = 3
        if rand > 7:
            self.image = "ASSETS/yellow.png"
            self.red = False
            self.state = 4

    def get_state(self): #Return the state of the light
        return self.state

    def getImage(self):  #Return the image for the light
        return self.image

    def getLocationX(self):   #Return the locations
        return self.locationX

    def getLocationY(self):
        return self.locationY
        
