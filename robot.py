import random   
class robot:
    

    locationX = 0 #The location location of the robot
    locationY = 0

    name = ""   #The name of the Robot

    image = None  #the image which represents the image. (Could make an image object?)

    points = 0    #The amount of points this robot has
    goal = ""   #???

    



    def __init__(self): #Constructor

        self.locationX = 0 
        self.locationY = 0 
        self.name = ""
        self.image = open("robot.png", 'r') #Open the robot image

        self.points = 0 
        self.goal = ""

    def moveUp(self): #Change the location of the robot to make it move up
        self.locationY -= 1
    def moveDown(self):
        self.locationY += !
    def moveLeft(self):
        self.locationY +=20
    def moveRight(self):
        self.locationX += 20
    def plotPath(self):
        print "find path"
        #insert DANNYS code.

    def checkLight(self):
        print "check light"
        #insert code to check if there is a traffic light near

    def passbyLandmark(self,arena):
        print "passby text display"
        #insert PHILS code for text display
        TreasureLandmark = random.randint(6,18)

        if self.arena[i] = 6:
            print "Pyramid"
            TreasureCheck()
        elif self.arena[i] = 7:
            print "Big Ben"
            TreasureCheck()
        elif self.arena[i] = 8:
            print "Taj Mahal"
            TreasureCheck()
        elif self.arena[i] = 9:
            print "Cloud Gate"
            TreasureCheck()
        elif self.arena[i] = 10:
            print "Arc De Triomphe"
            TreasureCheck()
        elif self.arena[i] = 11:
            print "Todaji temple"
            TreasureCheck()
        elif self.arena[i] = 12:
            print "The Gherkin"
            TreasureCheck()
        elif self.arena[i] = 13:
            print "The Shard"
            TreasureCheck()
        elif self.arena[i] = 14:
            print "The Statue Of Liberty"
            TreasureCheck()
        elif self.arena[i] = 15:
            print "Maracana Stadium"
            TreasureCheck()
        elif self.arena[i] = 16:
            print "Ayers Rock"
            TreasureCheck()
        elif self.arena[i] = 17:
            print "Stone Henge"
            TreasureCheck()
        elif self.arena[i] = 18:
            print "City Hall"
            TreasureCheck()

    def TreasureCheck(self, arena, TreasureLandmark):
        if arena[i] = TreasureLandmark:
            print "Treasure Found"

    def waitForLights(self):
        time.sleep(2)
        #make robot wait two seconds.
        
