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


def insertTrafficLights(ar, lights):   #Takes an instance of arena and places the traffic light elements into that arena
    width = ar.ret_size()[0]
    height = ar.ret_size()[1]
    picked = [3]

    for i in range(0, len(picked)):

        rand_row = random.randint(0,height) #Pick a random row to spawn a trafficlight
        picked.append(rand_row)             #append the thing so we know not to put two lights on the same row

        for x in range(0, width):
            if ar.ret_element_value(height, x) == 1:
                lights[x] = trafficLights(rand_row, x) #Add a new traffic light.
    



def main():

    #Create an instance of the pygeo class.
    #Doing so will call the constructor of the pygeo class.

    mapName = "map1"
    lights = [3]

    geo = pygeo.Geo(mapName)
    geo.GetsScreenshot()
    #Should now be an image called map1.png in the current directory
    arena = gen_arena.arena(mapName+".png")
    insertTrafficLights(arena, lights)


main()


