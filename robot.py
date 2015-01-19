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
        
        if self.arena[self.locationX,self.locationY] = 6:
            landmarkVar = "Pyramid"
            self.landInfo = wikipedia.summary("Pyramids", sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.arena[,] = 7:
            landmarkVar "Big Ben"
            self.landInfo = wikipedia.summary("Big Ben", sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)



        elif self.arena[self.locationX,self.locationY] = 8:
            landmarkVar = "Taj Mahal"
            self.landInfo = wikipedia.summary(landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.arena[self.locationX,self.locationY] = 9:
            landmarkVar = "Cloud Gate"
            self.landInfo = wikipedia.summary(landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.arena[self.locationX,self.locationY] = 10:
            landmarkVar = "Arc De Triomphe"
            self.landInfo = wikipedia.summary(landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.arena[self.locationX,self.locationY] = 11:
            ladmarkVar = "Todaji Temple"
            self.landInfo = wikipedia.summary(landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.arena[self.locationX,self.locationY] = 12:
            landmarkVar = "The Gherkin"
            self.landInfo = wikipedia.summary(landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.arena[self.locationX,self.locationY] = 13:
            landmarkVar = "The Shard"
            self.landInfo = wikipedia.summary(landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.arena[self.locationX,self.locationY] = 14:
            landmarkVar = "The Statue Of Liberty"
            self.landInfo = wikipedia.summ ary(landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.arena[self.locationX,self.locationY] = 15:
            landmarkVar = "Maracana Stadium"
            self.landInfo = wikipedia.summary(landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.arena[self.locationX,self.locationY] = 16:
            landmarkVar = "Ayers Rock"
            self.landInfo = wikipedia.summary(landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.arena[self.locationX,self.locationY] = 17:
            landmarkVar = "Stone Henge"
            self.landInfo = wikipedia.summary(landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


        elif self.arena[self.locationX,self.locationY] = 18:
            landmarkVar = "City Hall"
            self.landInfo = wikipedia.summary(landmarkVar, sentences = 2)
            treasureCheck(treasureLandmark, arena, treasureFound)


    def treasureCheck(self, arena, treasureLandmark, treasureLandmark1, treasureLandmark2, treasureLandmark3):
            if arena[self.locationX,self.locationY] = treasureLandmark1:
                print "Treasure 1 Found"
                self.treasureFound = self.treasureFound + 1
            elif arena[self.locationX,self.locationY] = treasureLandmark2:
                print "Treasure 2 Found"
                self.treasureFound = self.treasureFound + 1
            elif arena[self.locationX,self.locationY] = treasureLandmark3:
                print "Treasure 3 Found"
                self.treasureFound = self.treasureFound + 1
    def CreateText(sefl, arena, treasureLandmark, landInfo):
        print "Text Outputting..."
        sys.setdefaultcoding('utf-8')
        textFont = pygame.font.Font(None,36)
        landInfoText = textFont.render(landInfo,1,(10,10,10))
        textPos = landInfoText.get_rect()
        testPos.centerx = background.get_rect().centerx
        background.blit(landInfoText,textPos)

    def waitForLights(self):
        time.sleep(2)
        #make robot wait two seconds.
    
    def RobotPaulPoints(self):
        paulPoints = 0

    def RobotBarryPoints(self):
        barryPoints = 0 













