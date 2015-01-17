import random
import wikipedia
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
        self.locationX +=20
        arena.put(self.locationX-1, self.locationY)
        self.check()
    def moveRight(self):
        self.locationX += 20
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
        self.TreasureLandmark1 = random.randint(6,18)
        self.TreasureLandmark2 = random.randint(6,18)
        self.TreasureLandmark3 = random.randint(6,18)
        
        self.TreasureFound = 0
        
        if self.arena[self.locationX,self.locationY] = 6:
            print "Pyramid"
            TreasureCheck(TreasureLandmark, arena, TreasureFound)
            self.LandmInfo = wikipedia.summary("Pyramids", sentences = 2)
        elif self.arena[,] = 7:
            print "Big Ben"
            TreasureCheck(TreasureLandmark, arena, TreasureFound)
            self.LandmInfo = wikipedia.summary("Big Ben", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 8:
            print "Taj Mahal"
            TreasureCheck(TreasureLandmark, arena, TreasureFound)
            self.LandmInfo = wikipedia.summary("Taj Mahal", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 9:
            print "Cloud Gate"
            TreasureCheck(TreasureLandmark, arena, TreasureFound)
            self.LandmInfo = wikipedia.summary("Cloud Gate", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 10:
            print "Arc De Triomphe"
            TreasureCheck(TreasureLandmark, arena, TreasureFound)
            self.LandmInfo = wikipedia.summary("Arc De Triophe", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 11:
            print "Todaji Temple"
            TreasureCheck(TreasureLandmark, arena, TreasureFound)
            self.LandmInfo = wikipedia.summary("Todaji Temple", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 12:
            print "The Gherkin"
            TreasureCheck(TreasureLandmark, arena, TreasureFound)
            self.LandmInfo = wikipedia.summary("The Gherkin", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 13:
            print "The Shard"
            TreasureCheck(TreasureLandmark, arena, TreasureFound)
            self.LandmInfo = wikipedia.summary("The Shard", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 14:
            print "The Statue Of Liberty"
            TreasureCheck(TreasureLandmark, arena, TreasureFound)
            self.LandmInfo = wikipedia.summ ary("The Statue Of Liberty", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 15:
            print "Maracana Stadium"
            TreasureCheck(TreasureLandmark, arena, TreasureFound)
            self.LandmInfo = wikipedia.summary("Maracana Stadium", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 16:
            print "Ayers Rock"
            TreasureCheck(TreasureLandmark, arena, TreasureFound)
            self.LandmInfo = wikipedia.summary("Arers Rock", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 17:
            print "Stone Henge"
            TreasureCheck(TreasureLandmark, arena, TreasureFound)
            self.LandmInfo = wikipedia.summary("Stone Henge", sentences = 2)
        elif self.arena[self.locationX,self.locationY] = 18:
            print "City Hall"
            TreasureCheck(TreasureLandmark, arena, TreasureFound)
            self.LandmInfo = wikipedia.summary("City Hall", sentences = 2)



    def TreasureCheck(self, arena, TreasureLandmark, TreasureLandmark1, TreasureLandmark2, TreasureLandmark3):
        if arena[self.locationX,self.locationY] = TreasureLandmark1:
            print "Treasure 1 Found"
            self.TreasureFound = self.TreasureFound + 1
        elif arena[self.locationX,self.locationY] = TreasureLandmark2:
            print "Treasure 2 Found"
            self.TreasureFound = self.TreasureFound + 1
        elif arena[self.locationX,self.locationY] = TreasureLandmark3:
            print "Treasure 3 Found"
            self.TreasureFound = self.TreasureFound + 1
    def CreateText(sefl, arena, TreasureLandmark, LandInfo)
    def waitForLights(self):
        time.sleep(2)
        #make robot wait two seconds.
    
    def RobotPaulPoints(self):
        
    def RobotBarryPoints(self):
