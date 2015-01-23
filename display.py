import pygame

#Creates display and handles all the functionality of drawing to the display.
#Functions get given data from other displayable objects 


class display:      #Class which handles all the display functionality.
    def __init__(self, background): #Creates a display 
        self.background = background
        self.State = False

        pygame.init()
        display = pygame.display.set_mode((400, 400))
        my_font = pygame.font.Font(None, 22)
        pygame.display.update()
        
    def setRobot(self,x,y,image):   #Set the location of the robot
        return

    def setLandmark(self,x,y,image):    #Set the location of the landmark
        return
    
    def render(self):                #Render currently buffered scene
        return
