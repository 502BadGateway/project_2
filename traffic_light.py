import pygame
import time

class trafficLights:
    def __init__(self, x, y):
        self.locationX = x 
        self.locationY = y
        self.image = "red"
        load.gif(red)
        self.red = False

    def changeLight(self):
        #print "test"
        #CHANGE .red TO FALSE
        self.red = False
        #CHANGE REDIMAGE TO GREEN IMAGE
        self.image = "green"
        #WAIT FIVE SECONDS
        time.sleep(5)
        #CHANGE .red to TRUE
        self.red = True
        #CHANGE GREEN IMAGE TO RED
        self.image = "red"
        
