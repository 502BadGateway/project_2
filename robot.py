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

        
    def checkLight(self, arena): # object that checks if a traffic light is present 
       #When called will check for traffic lights around the robot. Returns true there is a light. Caller should skip moving the robot until this no longer returns true 

         print "check light" 
         if arena.ret_element_value(self.locationY + 2,self.locationX)  == 3: # checks if traffic light is green  
             print "Waiting...."
             return True
         if arena.ret_element_value(self.locationY - 2,self.locationX)  == 3:
             print "Waiting..."
             return True
         if arena.ret_element_value(self.locationY, self.locationX + 2) == 3:
             print "Waiting..."
             return True
         if arena.ret_element_value(self.locationY, self.locationX - 2) == 3:
             print "Waiting..."
             return True
         if arena.ret_element_value(self.locationY + 2, self.locationX) == 4: # checks if traffic light is red 
             print "Waiting..."
             return True
         if arena.ret_element_value(self.locationY - 2, self.locationX) == 4:
             print "Waiting..."
             return True
         if arena.ret_element_value(self.locationY, self.locationX + 2) == 4:
             print "Waiting..."
             return True
         if arena.ret_element_value(self.locationY, self.locationX - 2) == 4:
             print "Waiting..."
             return True
         else:
             return False
            

        

    def passbyLandmark(self,arena):
        print "passby text display"
        #insert PHILS code for text display
        self.treasureLandmark1 = random.randint(6,18) #these 3 lines create a random number between 6 - 18 that will deicide which landmarks have treasure
        self.treasureLandmark2 = random.randint(6,18)
        self.treasureLandmark3 = random.randint(6,18)
        
        self.treasureFound = 0
       
        if arena.ret_element_value(self.locationX, self.locationY) == 6:  # checks to see if the robot is at one of the landmarks
            return ("Great Pyramid", (sef.locationX, self.locationY))  #Return from call to passbylandmark to allow call to display.drawWikiText
            #TODO We need to make all the below, look similar to the above.


        elif arena.ret_element_value(self.locationX, self.locationY) == 7:
            return ("Big Ben", (self.locationX, self.locationY))


        elif arena.ret_element_value(self.locationX, self.locationY) == 8:
            return ("Taj Mahal", (self.locationX, self.locationY))


        elif arena.ret_element_value(self.locationX, self.locationY) == 9:
            return ("Cloud Gate", (self.locationX, self.locationY))


        elif arena.ret_element_value(self.locationX, self.locationY) == 10:
            return ("Arc De Triomphe", (self.locationX, self.locationY))


        elif arena.ret_element_value(self.locationX, self.locationY) == 11:
            return ("Todaji Temple", (self.locationX, self.locationY))


        elif arena.ret_element_value(self.locationX, self.locationY) == 12:
            return ("The Gherkin", (self.locationX,self.locationY))


        elif arena.ret_element_value(self.locationX, self.locationY) == 13:
            return ("The Shard", (self.locationX, self.locationY))


        elif arena.ret_element_value(self.locationX, self.locationY) == 14:
            return ("Statue Of Liberty", (self.locationX, self.locationY))


        elif arena.ret_element_value(self.locationX, self.locationY) == 15:
            return ("Maracana Statue", (self.locationX, self.locationY))


        elif arena.ret_element_value(self.locationX, self.locationY) == 16:
            return ("Ayers Rock", (self.locationX, self.locationY))


        elif arena.ret_element_value(self.locationX, self.locationY) == 17:
            return ("Stone Henge", (self.locationX, self.locationY))


        elif arena.ret_element_value(self.locationX, self.locationY) == 18:
            return ("City Hall", (self.locationX, self.locationY))

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









