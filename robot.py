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
            print "Pyramid"
            treasureCheck(treasureLandmark, arena, treasureFound)
            self.landInfo = wikipedia.summary("Pyramids", sentences = 2)
        elif self.arena[,] = 7:
            print "Big Ben"
            treasureCheck(treasureLandmark, arena, treasureFound)
            self.landInfo = wikipedia.summary("Big Ben", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 8:
            print "Taj Mahal"
            treasureCheck(treasureLandmark, arena, treasureFound)
            self.landInfo = wikipedia.summary("Taj Mahal", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 9:
            print "Cloud Gate"
            treasureCheck(treasureLandmark, arena, treasureFound)
            self.landInfo = wikipedia.summary("Cloud Gate", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 10:
            print "Arc De Triomphe"
            treasureCheck(treasureLandmark, arena, treasureFound)
            self.landInfo = wikipedia.summary("Arc De Triophe", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 11:
            print "Todaji Temple"
            treasureCheck(treasureLandmark, arena, treasureFound)
            self.landInfo = wikipedia.summary("Todaji Temple", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 12:
            print "The Gherkin"
            treasureCheck(treasureLandmark, arena, treasureFound)
            self.landInfo = wikipedia.summary("The Gherkin", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 13:
            print "The Shard"
            treasureCheck(treasureLandmark, arena, treasureFound)
            self.landInfo = wikipedia.summary("The Shard", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 14:
            print "The Statue Of Liberty"
            treasureCheck(treasureLandmark, arena, treasureFound)
            self.landInfo = wikipedia.summ ary("The Statue Of Liberty", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 15:
            print "Maracana Stadium"
            treasureCheck(treasureLandmark, arena, treasureFound)
            self.landInfo = wikipedia.summary("Maracana Stadium", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 16:
            print "Ayers Rock"
            treasureCheck(treasureLandmark, arena, treasureFound)
            self.landInfo = wikipedia.summary("Arers Rock", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 17:
            print "Stone Henge"
            treasureCheck(treasureLandmark, arena, treasureFound)
            self.landInfo = wikipedia.summary("Stone Henge", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 18:
            print "City Hall"
            treasureCheck(treasureLandmark, arena, treasureFound)
            self.landInfo = wikipedia.summary("City Hall", sentences = 2)



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
        textFont = pygame.font.Font(None,36)
        landInfoText = textFont.render(landInfo,1,(10,10,10))
        textPos = landInfoText.get_rect()
        testPos.centerx = background.get_rect().centerx
        background.blit(landInfoText,textPos)

    def waitForLights(self):
        time.sleep(2)
        #make robot wait two seconds.
    
    def RobotPaulPoints(self):
        
    def RobotBarryPoints(self):
