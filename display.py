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

        
    def setRobot(self,x,y,image, pygame_im=False):   #Set the location of the robot
        if pygame_im == False:                          #If we're not giving a pygame surface
            robot_image = pygame.image.load(image)  #Load the image
        else:
            robot_image = image
        robot_image = pygame.transform.scale(robot_image, (20,20))
        self.display.blit(robot_image, (y*10, x*10))
        self.State = False
        return

    def setLandmark(self,x,y,image, pygame_im=False):    #Set the location of the landmark
        if pygame_im == False:                          #If we're not giving a pygame surface
            robot_image = pygame.image.load(image)  #Load the image
        else:
            landmark_image = image
        landmark_image = pygame.transform.scale(robot_image, (20,20))
        self.display.blit(landmark_image, (y*10, x*10))
        self.State = False
        return

    def showPoints(self, font, text, position):
        return

    def render(self):                #Render currently buffered scene
        if self.State == False:      #If the state is dirty
            pygame.display.flip()                                       #Flip buffers.
            self.display.blit(self.background, self.backgroundRect)     #Blit background
        self.state = True
        return


#dis = display("map1.png")  #dbg
