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
    width = ar.ret_size()[0]
    height = ar.ret_size()[1]
    picked = [3]

    print "Using width:"+str(width)
    print "Using height:"+str(height)
    
    placed = False

    for i in range(0, num_lights):
        while placed != True:

           rand_row = random.randint(0,height-1) #Pick a random row to spawn a trafficlight
   
           for x in range(0, width):
               print rand_row, x
               print ar.ret_element_value(rand_row, x)  #Why does this always return 0???? XXX
               if ar.ret_element_value(rand_row, x) == 1 or ar.ret_element_value(rand_row, x) == 2:
                   lights[x] = trafficLights(rand_row, x) #Add a new traffic light.
                   ar.put(rand_row, x)
                   picked.append(rand_row)             #append the thing so we know not to put two lights on the same row
                   placed = True



def main():

    #Create an instance of the pygeo class.
    #Doing so will call the constructor of the pygeo class.

    mapName = "map1"
    lights = [3]

    geo = pygeo.Geo(mapName)
    geo.GetsScreenshot()
    #Should now be an image called map1.png in the current directory
    arena = gen_arena.arena(mapName+".png")
    arena.show_arena()
    insertTrafficLights(arena, lights, 3)
    print arena.ret_element_value(0, 9) #Give row, col
    print lights
    arena.show_arena()


main()


