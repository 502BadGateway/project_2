#
#   This file should contain code which brings all the sections together and ties everything into the project.
#   This file should be the only file to be run.
#


import pygeo
import gen_arena
from robot import Robot
import LandmarksClass
import traffic_light
import random
import display
import time
import pygame

def insertTrafficLights(ar, lights, num_lights):   #Takes an instance of arena and places the traffic light elements into that arena
    width = ar.ret_size()[0]-1        #Get the width and heights of the array
    height = ar.ret_size()[1]-1
    picked = [3]                    #Store how many we have picked TODO Do i really need to use this, might not be nessesary

    print "Using width:"+str(width) #dbg
    print "Using height:"+str(height)
    
    placed = False                  #Store if we've placed anything
    x = 0

    lightTot = 0
    
    for i in range(0, num_lights):  #Loop for amount of lights specified.
        print i
        rand_row = random.randint(0,height) #Pick a random row to spawn a trafficlight
   
        while x <= width-1 or placed != True:   #While we havent looked at every item in the row, and havent placed a light
            if ar.ret_element_value(rand_row, x) == 1 or ar.ret_element_value(rand_row, x) == 2:    #Check that the item we're on is a road.
                lights.append(traffic_light.trafficLights(rand_row, x+1)) #Add a new traffic light instance to lights list
                ar.put(rand_row, x+1, 3)                                                            #Save it in the arena
                lightTot += 1
                picked.append(rand_row)             #append the thing so we know not to put two lights on the same row
                placed = True                       #Move on
                break
            x += 1
        x = 0
        placed = False     #Make sure we reset the stuff we place anything
    print "Total Lights"
    print lightTot
    return lights
 

def findRobotLocation(ar, name):
    width = ar.ret_size()[0]-1        #Get the width and heights of the array
    height = ar.ret_size()[1]-1

    print "Using width:"+str(width) #dbg
    print "Using height:"+str(height)
    
    placed = False                  #Store if we've placed anything
    x = 0
    rand_row = random.randint(0,height) #Pick a random row to spawn a trafficlight

    while x <= width-1 or placed != True:   #While we havent looked at every item in the row, and havent placed a light
        if ar.ret_element_value(rand_row, x) == 1 or ar.ret_element_value(rand_row, x) == 2:    #Check that the item we're on is a road.
            print "ROBOT:"
            print rand_row, x
            bot = Robot(name, rand_row, x)                                    #Create a new robot!
            ar.put(rand_row, x, 5)                                                            #Save it in the arena
            placed = True                       #Move on
            break
        x += 1
    return bot

def  insertLandmarks(ar, landmarks, num_landmarks, landmarkslist): #Inserts landmarks onto the map. Behaves exactly the same as insertTrafficLights
    width = ar.ret_size()[0]-1        #Get the width and heights of the array
    height = ar.ret_size()[1]-1
    picked = [3]                    #Store how many we have picked TODO Do i really need to use this, might not be nessesary

    print "Using width:"+str(width) #dbg
    print "Using height:"+str(height)
    
    placed = False                  #Store if we've placed anything
    x = 0

    landmarkTot = 0
    
    for i in range(0, num_landmarks):  #Loop for amount of lights specified.
        print i
        rand_row = random.randint(0,height) #Pick a random row to spawn a trafficlight
   
        while x <= width-1 or placed != True:   #While we havent looked at every item in the row, and havent placed a light
            if ar.ret_element_value(rand_row, x) == 1 or ar.ret_element_value(rand_row, x) == 2:    #Check that the item we're on is a road.
                
                number = landmarkslist.pop()  #Grab all the data about the next landmark. TODO probably a cleaner way of putting all this stuff into varibles.
                landmarks.append(LandmarksClass.Landmarks(rand_row, x+1 )) #Add a new traffic light instance to lights list
                ar.put(rand_row, x+1, number)                                                            #Save it in the arena
                landmarkTot += 1
                picked.append(rand_row)             #append the thing so we know not to put two lights on the same row
                placed = True                       #Move on
                break
            x += 1
        x = 0
        placed = False     #Make sure we reset the stuff we place anything
    print "Total Landmarks"
    print landmarkTot
    return landmarks 


def main():

    #Create an instance of the pygeo class.
    #Doing so will call the constructor of the pygeo class.

    mapName = "map1"
    lights = []
    landmarks = []
    landmarkslist = [6,7,8,9,10,11,12,13,14,15,16,17,18]

    geo = pygeo.Geo(mapName)
    geo.GetsScreenshot()
    #Should now be an image called map1.png in the current directory
    arena = gen_arena.arena(mapName+".png") 
    arena.show_arena()
    lights = insertTrafficLights(arena, lights, 7)
    landmarks = insertLandmarks(arena, landmarks, len(landmarkslist), landmarkslist)
    arena.show_arena()
    bot = findRobotLocation(arena, "barry")

    arena.show_arena()

    

    window = display.display(str(mapName)+".png")    #Create display
    
    while pygame.event.peek((pygame.QUIT, pygame.KEYDOWN)) != True:         #Loop forever until either QUIT or KEYDOWN. TODO Change this to something better. Like a key press of Q or something. Will do for now
        window.setRobot(bot.returnLocationX(), bot.returnLocationY(), bot.returnImage())
        #window.setLandmark(lm.locationX, lm.locationY, lm.image)
        for i in landmarks:
            window.setLandmark(i.locationX, i.locationY, i.image)
        for i in lights:            #For every traffic light we created, queue it for render.
            window.setTrafficLight(i.locationX, i.locationY, i.image)
        window.RobotPoints(20,(600,30,0,0))
        window.CreateText("THIS IS SOME INFO", (300, 30,0,0))
        window.render()
        time.sleep(2)   #Sleep for two secs every loop to avoid running at 100% CPU while there is nothing to do here.
        print "Hello!"  #dbg
    return
main()


