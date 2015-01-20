import random
import wikipedia
import sys
reload(sys)
class robot:
    

    locationX = 0 #The location location of the robot
    locationY = 0

    name = ""   #The name of the Robot

    image = None  #the image which represents the image. (Could make an image object?)

    points = 0    #The amount of points this robot has
    goal = ""   #???

    



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
            

    def checkLight(self):
        print "check light"
        #insert code to check if there is a traffic light near

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
            treasureCheck(treasureLandmark, arena, treasureFound) #calls the treasrueCheck methof and hands it the parameters treasureLandmark, arena and treasureFound


        elif self.ret_element_val(self.locationX, self.locationY) = 7:
            self.landmarkVar "Big Ben"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)



        elif self.ret_element_val(self.locationX, self.locationY) = 8:
            self.landmarkVar = "Taj Mahal"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.ret_element_val(self.locationX, self.locationY) = 9:
            self.landmarkVar = "Cloud Gate"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.ret_element_val(self.locationX, self.locationY) = 10:
            self.landmarkVar = "Arc De Triomphe"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.ret_element_val(self.locationX, self.locationY) = 11:
            ladmarkVar = "Todaji Temple"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.ret_element_val(self.locationX, self.locationY) = 12:
            self.landmarkVar = "The Gherkin"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.ret_element_val(self.locationX, self.locationY) = 13:
            self.landmarkVar = "The Shard"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.ret_element_val(self.locationX, self.locationY) = 14:
            self.landmarkVar = "The Statue Of Liberty"
            self.landInfo = wikipedia.summ ary(self.landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.ret_element_val(self.locationX, self.locationY) = 15:
            self.landmarkVar = "Maracana Stadium"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.ret_element_val(self.locationX, self.locationY) = 16:
            self.landmarkVar = "Ayers Rock"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.ret_element_val(self.locationX, self.locationY) = 17:
            self.landmarkVar = "Stone Henge"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.ret_element_val(self.locationX, self.locationY) = 18:
            self.landmarkVar = "City Hall"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


    def treasureCheck(self, arena, treasureLandmark, treasureLandmark1, treasureLandmark2, treasureLandmark3, paulPoints): #this method checks to see if the landmark that the robot has arrived at has any treasure
            if self.ret_element_val(self.locationX,self.locationY) = treasureLandmark1:
                print "Treasure 1 Found"
                self.treasureFound = self.treasureFound + 1
                self.paulPoints = self.paulPoints + 1 #adds points to robot. not sure if I need to do this for both robots.

            elif self.ret_element_val(self.locationX,self.locationY) = treasureLandmark2:
                print "Treasure 2 Found"
                self.treasureFound = self.treasureFound + 1
                self.paulPoints = self.paulPoints + 1


            elif self.ret_element_val(self.locationX,self.locationY) = treasureLandmark3:
                print "Treasure 3 Found"
                self.treasureFound = self.treasureFound + 1
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
    
    def RobotPaulPoints(self): #this should display pauls points but im not sure if this needs to be done for both robots

        self.scoreFont = pygame.font.Font("Comic Sans MS",30)
        self.paulScoreText = self.scoreFont.render(self.paulPoints,1,(10,10,10))
        screen.blit(label,(1,0))
        pygame.display.flip()

    def RobotBarryPoints(self): #not sure if this class is needed













