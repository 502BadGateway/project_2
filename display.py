import pygame

#Creates display and handles all the functionality of drawing to the display.
#Functions get given data from other displayable objects 


class display:      #Class which handles all the display functionality.
    def __init__(self, background): #Creates a display 

        pygame.init()

        #DATA --------------
        self.background = pygame.image.load(background) #Load the background image 
        self.State = False
        self.backgroundRect = self.background.get_rect() #Get the the background rectangle
        self.size = self.background.get_size()          #Get dimentions of the window

        self.display = pygame.display.set_mode((640, 479))     #Set the screen up
        self.defaultFont = pygame.font.Font(None, 22)          #
        
        self.render()                                   #Call render

        return

        
    def setRobot(self,x,y,image):   #Set the location of the robot
        return

    def setLandmark(self,x,y,image):    #Set the location of the landmark
        return

    def showPoints(self, font, text, position):
        return

    def render(self):                #Render currently buffered scene
        
        self.display.blit(self.background, self.backgroundRect)     #Blit background
        pygame.display.flip()                                       #Flip buffers.


        return


#dis = display("map1.png")  #dbg
