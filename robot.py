import random
import wikipedia
import sys
reload(sys)
class Robot:


    def __init__(self, name, x, y): #Constructor

        self.locationX = x 
        self.locationY = y 
        self.name = name 
        rnd = random.randint(1,2)
        self.image = "ASSETS/car.png"  #Open the robot image

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

    def plotPath(self, arena, tX, tY, ):

        arena1 = arena.ret_arena_copy()

        targetX =  tX   #Target landmark MISSING
        targetY = tY
        
        currentCheckingY = self.locationY
        currentCheckingX = self.locationX
        
        parentListY = []
        parentListX = []
        
        openListY = []
        openListX = []
        
        while 1:
        
            parentListY.append(currentCheckingX) #Add current point to path
            parentListX.append(currentCheckingY)
        
        
            if(currentCheckingY > 0): #If current square is not on the top row
                openListY.append(currentCheckingY - 1) #add UP1 reference to the openList
                openListX.append(currentCheckingX)
        
            else:
                openListY.append(1000) #Otherwise, add a null to the list.
                openListX.append(1000)
        
            if(currentCheckingY < 6): #If current square is not on the bottom row
                openListY.append(currentCheckingY + 1) #add DOWN1 reference to openlist
                openListX.append(currentCheckingX)
        
            else:
                openListY.append(1000)#Otherwise, add a null to the list.
                openListX.append(1000)
        
            if(currentCheckingX > 0): #If current square is not on the leftmost column
                openListY.append(currentCheckingY)
                openListX.append(currentCheckingX - 1)
        
            else:
                openListY.append(1000)#Otherwise, add a null to the list.
                openListX.append(1000)
        
            if(currentCheckingX < 6): #If current square is not on the rightmost column
                openListY.append(currentCheckingY)
                openListX.append(currentCheckingX + 1)
        
            else:
                openListY.append(1000)#Otherwise, add a null to the list.
                openListX.append(1000)
        
            if(arena1[currentCheckingY - 1][currentCheckingX] == 1 or arena1[currentCheckingY - 1][currentCheckingX] == 2): #If UP square is a road. 
                 
        
                distY = openListY[0] - targetY #Calculate Distance Cost
                distX = openListX[0] - targetX
        
        
        
                if(distY < 0): #If distance cost is a negative int, reverse it.
                    distY = -distY + 0
                if(distX < 0):
                    distX = -distX + 0
        
                score = []
                score.append(distY + distX)
        
            else:
                score = []
                score.append(1000)
        
        
            if(arena1[currentCheckingY + 1][currentCheckingX] == 1 or arena1[currentCheckingY + 1][currentCheckingX] == 2):#if DOWN square is a road
        
                distY = openListY[1] - targetY
                distX = openListX[1] - targetX
        
        
                if(distY < 0):
                    distY = -distY + 0
                if(distX < 0):
                    distX = -distX + 0
        
                score.append(distY + distX)
        
            else:
               score.append(1000)
        
            if(arena1[currentCheckingY][currentCheckingX - 1] == 1 or arena1[currentCheckingY][currentCheckingX - 1] == 2):#if LEFT square is a road
        
                distY = openListY[2] - targetY
                distX = openListX[2] - targetX
        
        
        
                if(distX < 0):
                    distY = -distY + 0
                if(distX < 0):
                    distX = -distX + 0
        
                score.append(distY + distX)
        
            else:
                score.append(1000)
        
            if(arena1[currentCheckingY][currentCheckingX + 1] == 1 or arena1[currentCheckingY][currentCheckingX + 1] == 2): #if Right Square is a road
        
                distY = openListY[3] - targetY
                distX = openListX[3] - targetX
        
                if(distY < 0):
                    distY = -distY + 0
                if(distX < 0):
                    distX = -distX + 0
        
                score.append(distY + distX)
        
            else:
                score.append(1000)
        
        
            print currentCheckingY, currentCheckingX
               
            if(score[0] <= score[1] and score[0] < score[2] and score[0] <= score[3]): #If score[0] is lowest, add that coord to the parent list.
                parentListY.append(currentCheckingY - 1)
                parentListX.append(currentCheckingX)
        
                currentCheckingY = currentCheckingY - 1 #move checking to that square.
                currentCheckingX = currentCheckingX
        
            if(score[1] < score[0] and score[1] < score[2] and score[1] <= score[3]):
                parentListY.append(currentCheckingY + 1)
                parentListX.append(currentCheckingX)
        
                currentCheckingY = currentCheckingY + 1
                currentCheckingX = currentCheckingX
        
            if(score[2] < score[0] and score[2] <= score[1] and score[2] <= score[3]):
                parentListY.append(currentCheckingY)
                parentListX.append(currentCheckingX - 1)
        
                currentCheckingY = currentCheckingY
                currentCheckingX = currentCheckingX - 1
        
            if(score[3] < score[0] and score[3] < score[1] and score[3] < score[2]):
                parentListY.append(currentCheckingY)
                parentListX.append(currentCheckingX + 1)
        
                currentCheckingY = currentCheckingY
                currentCheckingX = currentCheckingX + 1
            print "Currently Is", currentCheckingY, currentCheckingX
        
            if(currentCheckingX == targetX and currentCheckingY == targetY):
                print currentCheckingY, currentCheckingX, targetY, targetX
                break

        print "Path Found"
        return parentListY, parentListX

        
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
       
        if arena.ret_element_val(self.locationX, self.locationY) == 6:  # checks to see if the robot is at one of the landmarks
            self.landmarkVar = "Pyramid"                                     # this is what will search wikipedia
            self.landInfo = wikipedia.summary(self.ladmarkVar, sentences = 2) #puts what wikipedia outputs under thr landInfo variable to be used later
            self.font = pygame.font.Font("Comic Sans MS", 20) #this is the font handed to the render_textrect method
            treasureCheck(treasureLandmark, arena, treasureFound) #calls the treasrueCheck methof and hands it the parameters treasureLandmark, arena and treasureFound
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0) # this calls the method that does the word wrap, this may need to be modified becuse I think it will create a new display.


        elif self.ret_element_val(self.locationX, self.locationY) == 7:
            self.landmarkVar = "Big Ben"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            self.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)



        elif self.ret_element_val(self.locationX, self.locationY) == 8:
            self.landmarkVar = "Taj Mahal"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            self.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) == 9:
            self.landmarkVar = "Cloud Gate"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            self.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) == 10:
            self.landmarkVar = "Arc De Triomphe"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            self.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) == 11:
            ladmarkVar = "Todaji Temple"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            self.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) == 12:
            self.landmarkVar = "The Gherkin"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            self.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) == 13:
            self.landmarkVar = "The Shard"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            self.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) == 14:
            self.landmarkVar = "The Statue Of Liberty"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            self.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) == 15:
            self.landmarkVar = "Maracana Stadium"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            self.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) == 16:
            self.landmarkVar = "Ayers Rock"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            self.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) == 17:
            self.landmarkVar = "Stone Henge"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            self.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)


        elif self.ret_element_val(self.locationX, self.locationY) == 18:
            self.landmarkVar = "City Hall"
            self.landInfo = wikipedia.summary(self.landmarkVar, sentences = 2)
            self.font = pygame.font.Font("Comic Sans MS", 20)
            self.rect = pygame.Rect((0, 300, 200, 300)) #this will needed to be modified to see how the text apears on the page when the actual program is running
            treasureCheck(treasureLandmark, arena, treasureFound)
            render_textrect(landInfo, font, rect, (250,250,250), (0,0,0), 0)

    #TODO Why does this still use paulpoints variables? They don't exist.
    def treasureCheck(self, arena, treasureLandmark, treasureLandmark1, treasureLandmark2, treasureLandmark3, paulPoints): #this method checks to see if the landmark that the robot has arrived at has any treasure
            if self.ret_element_val(self.locationX,self.locationY) == treasureLandmark1: #if the coodinates the robot is at is what has been selected to be treasrueLandmark1 then add a point to robots score
                print "Treasure 1 Found"
                self.points += 1 #adds points to robot. not sure if I need to do this for both robots.

            elif self.ret_element_val(self.locationX,self.locationY) == treasureLandmark2: #if the coodinates the robot is at is what has been selected to be treasrueLandmark2 then add a point to robots score
                print "Treasure 2 Found"
                self.points += 1


            elif self.ret_element_val(self.locationX,self.locationY) == treasureLandmark3: #if the coodinates the robot is at is what has been selected to be treasrueLandmark3 then add a point to robots score
                print "Treasure 3 Found"
                self.points += 1
            else:
                print "No Treasrue at this landmark"


    
    def returnLocationX(self):
        return self.locationX
    def returnLocationY(self):
        return self.locationY
    def returnImage(self):
        return self.image









