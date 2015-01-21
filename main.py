#
#   This file should contain code which brings all the sections together and ties everything into the project.
#   This file should be the only file to be run.
#


import pygeo
import gen_arena
#import robot
import LandmarksClass
import traffic_light
import random


def insertTrafficLights(ar, lights, num_lights):   #Takes an instance of arena and places the traffic light elements into that arena
    width = ar.ret_size()[0]-1        #Get the width and heights of the array
    height = ar.ret_size()[1]-1
    picked = [3]                    #Store how many we have picked TODO Do i really need to use this, might not be nessesary

    print "Using width:"+str(width) #dbg
    print "Using height:"+str(height)
    
    placed = False                  #Store if we've placed anything
    x = 0

    for i in range(0, num_lights):  #Loop for amount of lights specified.

        rand_row = random.randint(0,height) #Pick a random row to spawn a trafficlight
   
        while x <= width-1 or placed != True:   #While we havent looked at every item in the row, and havent placed a light
            if ar.ret_element_value(rand_row, x) == 1 or ar.ret_element_value(rand_row, x) == 2:    #Check that the item we're on is a road.
                lights.append(traffic_light.trafficLights(rand_row, x+1)) #Add a new traffic light instance to lights list
                ar.put(rand_row, x+1, 3)                                                            #Save it in the arena
                picked.append(rand_row)             #append the thing so we know not to put two lights on the same row
                placed = True                       #Move on
            x += 1
        x = 0
        placed = False     #Make sure we reset the stuff we place anything



def main():

    #Create an instance of the pygeo class.
    #Doing so will call the constructor of the pygeo class.

    mapName = "map1"
    lights = [3]

    geo = pygeo.Geo(mapName)
    geo.GetsScreenshot()
    #Should now be an image called map1.png in the current directory
    arena = gen_arena.arena(mapName+".png", True)
    arena.show_arena()
    insertTrafficLights(arena, lights, 7)
    arena.show_arena()


main()


