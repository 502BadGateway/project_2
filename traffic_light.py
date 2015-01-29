import pygame #imports pygame library
import time #imports time api
import random #imports random api

class trafficLights: #a class for the traffic light
    def __init__(self, x, y): #stores all variables 
        self.state = 3 #variable initiated by keyword "self" in this case variable is state for array 3 
        self.locationX = x #variable for location x
        self.locationY = y #variable for location y
        self.image = "ASSETS/red.png" #variable for image, images have to be in .png format in pygame
        self.red = False #returns red image/traffic light when robot comes across array 3

    def changeLight(self): #stores variasbles for changing the light colour
        rand  = random.randint(0,10) #uses random api to generate random array number from 0 to 10 
        if rand < 3: #if statement for if robot comes across an array greater than 3
            self.image = "ASSETS/red.png" #variable for red traffic light image 
            self.red = True 
            self.state = 3 
        if rand > 7:#if statement for if robot comes across an array less than 7
            self.image = "ASSETS/yellow.png" #variable for yellow traffic light image
            self.red = False
            self.state = 4

    def get_state(self): #Return the state of the light
        return self.state

    def getImage(self):  #Return the image for the light
        return self.image

    def getLocationX(self):   #Return the location x
        return self.locationX

    def getLocationY(self): #returns the location Y
        return self.locationY
        
