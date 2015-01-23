import random
import wikipedia
import sys
reload(sys)
class robot:


    def __init__(self, name): #Constructor

        self.locationX = 0 
        self.locationY = 0 
        self.name = name 
        self.image = open("robot.png", 'r') #Open the robot image

        self.points = 0 
        self.goal = ""

    def moveUp(self, arena): #Change the location of the robot to make it move up
        self.locationY -= 1
        arena.put(self.locationX, self.locationY-1)
        self.check()
    def moveDown(self):
        self.locationY += 1
        arena.put(self.locationX, self.locationY+1)
        self.check()
    def moveLeft(self):
        self.locationX += 1
        arena.put(self.locationX-1, self.locationY)
        self.check()
    def moveRight(self):
        self.locationX += 1
        arena.put(self.locationX+1, self.locationY)
        self.check()

    def plotPath(self):
        print "find path"
        #insert DANNYS code.
        
    def checkLight(self): # object that checks if a traffic light is present 
        
         print "check light" 
         if(arena[self.locationY + 2][self.locationX] == 3): # checks if traffic light is green  
             print "test"
         if(arena[self.locationY - 2][self.locationX] == 3):
             print "test"
         if(arena[self.locationY][self.locationX + 2] == 3):
             print "test"
         if(arena[self.locationY][self.locationX - 2] == 3):
             print "test"
         if(arena[self.locationY + 2][self.locationX] == 4): # checks if traffic light is red 
             print "test"
         if(arena[self.locationY - 2][self.locationX] == 4):
             print "test"
         if(arena[self.locationY][self.locationX + 2] == 4):
             print "test"
         if(arena[self.locationY][self.locationX - 2] == 4):
             print "test"
            

        

    def passbyLandmark(self,arena):
        print "passby text display"
        #insert PHILS code for text display
        self.treasureLandmark1 = random.randint(6,18) #these 3 lines create a random number between 6 - 18 that will deicide which landmarks have treasure
        self.treasureLandmark2 = random.randint(6,18)
        self.treasureLandmark3 = random.randint(6,18)
        
        self.treasureFound = 0
        
        if arena.ret_element_val(self.locationX, self.locationY) = 6:  # checks to see if the robot is at one of the landmarks
            self.landmarkVar = "Pyramid"                                     # this is what will search wikipedia
            self.landInfo = wikipedia.summary(self.ladmarkVar, sentences = 2) #puts what wikipedia outputs under thr landInfo variable to be used later
            self.font = pygame.font.Font("Comic Sans MS", 20) #this is the font handed to the render_textrect method
            treasureCheck(treasureLandmark, arena, treasureFound) #calls the treasrueCheck methof and hands it the parameters treasureLandmark, arena and treasureFound
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0) # this calls the method that does the word wrap, this may need to be modified becuse I think it will create a new display.


        elif self.ret_element_val(self.locationX, self.locationY) = 7:
            self.landmarkVar "Big Ben"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            slef.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)



        elif self.ret_element_val(self.locationX, self.locationY) = 8:
            self.landmarkVar = "Taj Mahal"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            slef.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) = 9:
            self.landmarkVar = "Cloud Gate"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            slef.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) = 10:
            self.landmarkVar = "Arc De Triomphe"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            slef.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) = 11:
            ladmarkVar = "Todaji Temple"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            slef.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) = 12:
            self.landmarkVar = "The Gherkin"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            slef.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) = 13:
            self.landmarkVar = "The Shard"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            slef.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) = 14:
            self.landmarkVar = "The Statue Of Liberty"
            self.landInfo = wikipedia.summ ary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            slef.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) = 15:
            self.landmarkVar = "Maracana Stadium"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            slef.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) = 16:
            self.landmarkVar = "Ayers Rock"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            slef.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) = 17:
            self.landmarkVar = "Stone Henge"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            slef.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) = 18:
            self.landmarkVar = "City Hall"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            slef.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


    def treasureCheck(self, arena, treasureLandmark, treasureLandmark1, treasureLandmark2, treasureLandmark3, paulPoints): #this method checks to see if the landmark that the robot has arrived at has any treasure
            if self.ret_element_val(self.locationX,self.locationY) = treasureLandmark1: #if the coodinates the robot is at is what has been selected to be treasrueLandmark1 then add a point to robots score
                print "Treasure 1 Found"
                self.paulPoints = self.paulPoints + 1 #adds points to robot. not sure if I need to do this for both robots.

            elif self.ret_element_val(self.locationX,self.locationY) = treasureLandmark2: #if the coodinates the robot is at is what has been selected to be treasrueLandmark2 then add a point to robots score
                print "Treasure 2 Found"
                self.paulPoints = self.paulPoints + 1


            elif self.ret_element_val(self.locationX,self.locationY) = treasureLandmark3: #if the coodinates the robot is at is what has been selected to be treasrueLandmark3 then add a point to robots score
                print "Treasure 3 Found"
                self.paulPoints = self.paulPoints + 1
            else:
                print "No Treasrue at this landmark"

    def CreateText(self, arena, treasureLandmark, landInfo):

        print "Text Outputting..."

        sys.setdefaultcoding('utf-8') #converts to UNICODE
        self.textFont = pygame.font.Font("Comic Sans MS",15) #sets font and text size
        self.landInfoText = self.textFont.render(landInfo,1,(10,10,10)) #loads the text to be displayed to the screen (need to work out how to word wrap)
        screen.blit(self.landInfoText,(0,0)) #blits the screen and sets the poistion I think (not sure becuase I cant test it)
        pygame.display.flip() #refreshes display


    def waitForLights(self):
        time.sleep(2)
        #make robot wait two seconds.
    
    def RobotPoints(self,robotScore,positionVar): #this should display pauls points but im not sure if this needs to be done for both robots

        self.scoreFont = pygame.font.Font("Comic Sans MS",30)
        self.scoreText = self.scoreFont.render(self.robotScore,1,(10,10,10))
        self.textPos = pygame.Rect(positionVar) #positionVar needs to be given to this method, it should be in the format "600,10,0,0" and "600,30,0,0"
        background.blit(scoreText, textPos)
        screen.blit(background, (0,0))
        pygame.display.flip()
    
    def returnLocationX():
        return self.locationX
    def returnLocationY():
        return self.locationY
    def returnImage():
        return self.image

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








