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

    def passbyLandmark(self):
        print "passby text display"
        #insert PHILS code for text display

    def waitForLights(self):
        time.sleep(2)
        #make robot wait two seconds.
        
