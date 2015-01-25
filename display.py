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
        
        pygame.font.init()                              #Initialise fonts

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

    def CreateText(self, arena, treasureLandmark, landInfo):

        print "Text Outputting..."

        sys.setdefaultcoding('utf-8') #converts to UNICODE
        self.textFont = pygame.font.Font(None,15) #sets font and text size
        self.landInfoText = self.textFont.render(landInfo,1,(10,10,10)) #loads the text to be displayed to the screen (need to work out how to word wrap)
        screen.blit(self.landInfoText,(0,0)) #blits the screen and sets the poistion I think (not sure becuase I cant test it)
        pygame.display.flip() #refreshes display


    def waitForLights(self):
        time.sleep(2)
        #make robot wait two seconds.
    
    def RobotPoints(self,robotScore,positionVar): #this should display pauls points but im not sure if this needs to be done for both robots

        self.state = False
        scoreFont = pygame.font.Font(None,30)
        scoreText = scoreFont.render(str(robotScore),1,(10,10,10))
        textPos = pygame.Rect(positionVar) #positionVar needs to be given to this method, it should be in the format "600,10,0,0" and "600,30,0,0"
        self.display.blit(scoreText, textPos)
        #self.display.blit(background, (0,0))

    def render_textrect(landInfo, font, rect, text_color, background_color, justification=0): #this code will wordwrap text for you IT IS NOT MINE it is from "http://www.pygame.org/pcr/text_rect/index.php"

        import pygame
        
        final_lines = []

        requested_lines = landInfo.splitlines()

        # Create a series of lines that will fit on the provided
        # rectangle.

        for requested_line in requested_lines:
            if font.size(requested_line)[0] > rect.width:
                words = requested_line.split(' ')
                # if any of our words are too long to fit, return.
                for word in words:
                    if font.size(word)[0] >= rect.width:
                        raise TextRectException, "The word " + word + " is too long to fit in the rect passed."
                # Start a new line
                accumulated_line = ""
                for word in words:
                    test_line = accumulated_line + word + " "
                    # Build the line while the words fit.    
                    if font.size(test_line)[0] < rect.width:
                        accumulated_line = test_line 
                    else: 
                        final_lines.append(accumulated_line) 
                        accumulated_line = word + " " 
                final_lines.append(accumulated_line)
            else: 
                final_lines.append(requested_line) 

        # Let's try to write the text out on the surface.

        surface = pygame.Surface(rect.size) 
        surface.fill(background_color) 

        accumulated_height = 0 
        for line in final_lines: 
            if accumulated_height + font.size(line)[1] >= rect.height:
                raise TextRectException, "Once word-wrapped, the text string was too tall to fit in the rect."
            if line != "":
                tempsurface = font.render(line, 1, text_color)
                if justification == 0:
                    surface.blit(tempsurface, (0, accumulated_height))
                elif justification == 1:
                    surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
                elif justification == 2:
                    surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
                else:
                    raise TextRectException, "Invalid justification argument: " + str(justification)
            accumulated_height += font.size(line)[1]

        return surface


#dis = display("map1.png")  #dbg
