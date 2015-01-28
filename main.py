#
#   This file should contain code which brings all the sections together and ties everything into the project.
#   This file should be the only file to be run.
#

import wikipedia
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
                nlight = traffic_light.trafficLights(rand_row, x+1)
                lights.append(nlight) #Add a new traffic light instance to lights list
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
 

def findRobotLocation(ar, name, robotList, targetX, targetY):
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
            bot = Robot(name, rand_row, x, ar,targetX, targetY)                                    #Create a new robot!
            robotList.append(bot)
            ar.put(rand_row, x, 5)                                                            #Save it in the arena
            placed = True                       #Move on
            break
        x += 1
    return robotList 

def  insertLandmarks(ar, landmarks, num_landmarks, landmarkslist, infoList): #Inserts landmarks onto the map. Behaves exactly the same as insertTrafficLights
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
            if ar.ret_element_value(rand_row, x) == 1 or ar.ret_element_value(rand_row, x) == 2 and ar.ret_element_value(rand_row, x) < 3:    #Check that the item we're on is a road.
                randomTreasure = random.randint(0,1)
                randomInfo = random.randint(0, len(infoList)-1)      #pick a number to select random image and name.

                number = landmarkslist.pop()  #Grab all the data about the next landmark. TODO probably a cleaner way of putting all this stuff into varibles.
                landmarks.append(LandmarksClass.Landmarks(rand_row, x+1, randomTreasure, infoList[randomInfo][1], infoList[randomInfo][0])) #Add a new traffic light instance to lights list
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

    clock = pygame.time.Clock()
    #Create an instance of the pygeo class.
    #Doing selfso will call the constructor of the pygeo class.

    mapName = "map1"
    lights = []
    landmarks = []
    landmarkslist = [6,7,8,9,10,11,12,13,14,15,16,17,18]    #list of numbers for landmarks TODO need to assotiate the right numbers with the right landmarks

    robotList = []          #List of instances of the robot

    landmarkInfo = [("ArcDeTriomphe.png","Arc De Triomphe"), ("ayersrock.png","Ayers Rock"),("bigBen.png","Big Ben"),("cloudgate.png","Cloud Gate"),("Pyraimd.png","Pyramid"),("stonehenge.png","Stone Henge"), ("TajMahal.png","Taj Mahal")]

    geo = pygeo.Geo(mapName)
    geo.GetsScreenshot()
    #Should now be an image called map1.png in the current directory
    arena = gen_arena.arena(mapName+".png") 
    arena.show_arena()
    lights = insertTrafficLights(arena, lights, 7)
    landmarks = insertLandmarks(arena, landmarks, len(landmarkslist), landmarkslist, landmarkInfo)
    arena.show_arena()
    
    rand_landmark_num = random.randint(0, len(landmarks)) #Choose a random landmark as a target
    rand_landmark = landmarks[rand_landmark_num]


    robotList = findRobotLocation(arena, "barry", robotList, rand_landmark.locationX, rand_landmark.locationY)      #Add new robot.
    robotList = findRobotLocation(arena, "paul", robotList, rand_landmark.locationX, rand_landmark.locationY)      #Add new robot.

    arena.show_arena()

    window = display.display(str(mapName)+".png")    #Create display
    
    while pygame.event.peek((pygame.QUIT, pygame.KEYDOWN)) != True:         #Loop forever until either QUIT or KEYDOWN. TODO Change this to something better. Like a key press of Q or something. Will do for now
        clock.tick()


        
        for i in landmarks:
            window.setLandmark(i.locationX, i.locationY, i.image)
        for i in lights:            #For every traffic light we created, queue it for render.
            i.changeLight()
            arena.put(i.getLocationX(), i.getLocationY(), i.get_state())
            window.setTrafficLight(i.getLocationX(), i.getLocationY(), i.getImage())

        for i in robotList:
            landmark = i.passbyLandmark(arena)      #Check for landmarks around the robot
            if landmark != None:                          #If we found one, then render it's info text
                window.drawWikiText(passbyLandmark[0], passbyLandmark[1], passbyLandmark[2])

            light = i.checkLight(arena)  #Check lights around it

            if light == False:           #If there was now light, or the light was green
                #i.move()        #Move. TODO Actually write this function
                window.setRobot(i.returnLocationX(), i.returnLocationY(), i.returnImage())

        window.render()
        print clock.get_fps()
    return
main()


#   IGNORE
#   Just  noting how i envision the robot loopy section to work 
#   Just here so i remember what i was going to do once Dna submits work from Jan 27th. - Sam
#   for i in robotList:
#       passedLadmark = i.passbyLandmark()
#       if passedLandmark != True:
#           i.move()
#
