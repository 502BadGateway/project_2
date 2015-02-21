import random
import wikipedia
import sys
reload(sys)
class Robot:


    def __init__(self, name, x, y, arena, targetX, targetY, runPathfind = True): #Constructor

        self.locationX = x 
        self.locationY = y 
        self.name = name 
        rnd = random.randint(1,2)
        self.image = "ASSETS/car.png"  #Open the robot image

        self.points = 0 
        self.goal = ""

        if runPathfind == True:
            self.plotPath(arena, targetX, targetY )
        else:
            return


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

    def plotPath(self, arena, tX, tY, ): #define a method called plotPath, pass it self, arena and targets.

        arena1 = arena.ret_arena_copy() #pull the arena.

        targetX =  tX   #Target landmark MISSING
        targetY = tY 

        print targetX, targetY #DEBUG
        
        currentCheckingY = self.locationY #make the first Y ref checked to be the robots location.
        currentCheckingX = self.locationX #make the first X ref checked to be the robots location.
        
        parentListY = [] #List which contains the path of y ref's the robot will follow
        parentListX = [] #List which contains the path of x ref's the robot will follow
        
        openListY = [] #List of y ref's to be checked for path.
        openListX = [] #List of x ref's to be checked for path.
        
        stop = 0 #Iterator which counts how many times the loop has ran.

        while stop < 1000: #if the loop runs +1000.
        
            parentListY.append(currentCheckingX) #Add current Y point to path
            parentListX.append(currentCheckingY) #Add current X point to path
        
        
            if(currentCheckingY > 0): #If current square is not on the top row
                openListY.append(currentCheckingY - 1) #add UP1 Y reference to the openList
                openListX.append(currentCheckingX) #add UP1 X reference to the openList
        
            else:
                openListY.append(1000) #Otherwise, add a null to the Y list.
                openListX.append(1000) #Otherwise, add a null to the X list.
        
            if(currentCheckingY < 6): #If current square is not on the bottom row
                openListY.append(currentCheckingY + 1) #add DOWN1 reference to Y openlist
                openListX.append(currentCheckingX) #add DOWN1 reference to X openlist
        
            else:
                openListY.append(1000)#Otherwise, add a null to the Y list.
                openListX.append(1000)#Otherwise, add a null to the X list.
        
            if(currentCheckingX > 0): #If current square is not on the leftmost column
                openListY.append(currentCheckingY) #add currentcheckingY to openListY
                openListX.append(currentCheckingX - 1) #add currentcheckingx - 1 to openListX
        
            else:
                openListY.append(1000)#Otherwise, add a null to the Y list.
                openListX.append(1000)#Otherwise, add a null to the X List. 
        
            if(currentCheckingX < 6): #If current square is not on the rightmost column
                openListY.append(currentCheckingY)#add currentcheckingY to openListY
                openListX.append(currentCheckingX + 1)#add currentcheckingx - 1 to openListX
        
            else:
                openListY.append(1000)#Otherwise, add a null to the Y list.
                openListX.append(1000)#Otherwise, add a null to the X list.
        
            if(arena1[currentCheckingY - 1][currentCheckingX] == 1 or arena1[currentCheckingY - 1][currentCheckingX] == 2): #If UP square is a road. 
                 
        
                distY = openListY[0] - targetY #Calculate Distance Cost on Y axis
                distX = openListX[0] - targetX #Calculate Distance Cost on X axis
        
        
        
                if(distY < 0): #If distance cost is a negative int, reverse it.
                    distY = -distY + 0 #turn (-y) into y.
                if(distX < 0):
                    distX = -distX + 0 #turn (-x) into x.
        
                score = [] #Create a list to store scores in.
                score.append(distY + distX) #Append the list with distance of Y plus distance by X.
        
            else:
                score = [] #Create a list to store scores in.
                score.append(1000) #Add 1000 to the score, so it will never be the lowest score.
        
        
            if(arena1[currentCheckingY + 1][currentCheckingX] == 1 or arena1[currentCheckingY + 1][currentCheckingX] == 2):#if DOWN square is a road
        
                distY = openListY[1] - targetY #make distance Y = UP1 - the target Y
                distX = openListX[1] - targetX #make distance X = UP1 - the target X
        
        
                if(distY < 0): #If the distY is less than 0
                    distY = -distY + 0 #make (-y) = y.
                if(distX < 0): #If the distX is less than 0
                    distX = -distX + 0 #make (-x) = x,
        
                score.append(distY + distX) #Append the list with distance of Y plus distance by X.
        
            else:
                score.append(1000) #Add 1000 to the score, so it will never be the lowest score.
        
            if(arena1[currentCheckingY][currentCheckingX - 1] == 1 or arena1[currentCheckingY][currentCheckingX - 1] == 2):#if LEFT square is a road
        
                distY = openListY[2] - targetY #Make the distance Y = the current Y ref - the target Y reference.
                distX = openListX[2] - targetX #Make the distance X = the current X ref - the target X reference.
        
        
        
                if(distX < 0): #If the distance y is a negative int.
                    distY = -distY + 0 #make (-y) = y.
                if(distX < 0): #If the distance x is a negative int.
                    distX = -distX + 0 #make (-x) = x.
        
                score.append(distY + distX) #add the score to the list score.
        
            else: #if LEFT isnt a valid reference
                score.append(1000) #add 1000 to the score, so this reference isnt choosen.
        
            if(arena1[currentCheckingY][currentCheckingX + 1] == 1 or arena1[currentCheckingY][currentCheckingX + 1] == 2): #if Right Square is a road
        
                distY = openListY[3] - targetY #make the distY equal Right y ref - targety
                distX = openListX[3] - targetX #make the distX equal Right X ref - targetx
        
                if(distY < 0): #if the distY is a negative int.
                    distY = -distY + 0 #make (-y) = y.
                if(distX < 0): #if the distX is a negative int.
                    distX = -distX + 0 #make (-x) = x.
        
                score.append(distY + distX) #add the combined distance to the score list.
        
            else: #if the RIGHT reference is invalid.
                score.append(1000) #add 1000 to the score. 
        
        
            print currentCheckingY, currentCheckingX #DEBUG
               
            if(score[0] <= score[1] and score[0] < score[2] and score[0] <= score[3]): #If score[0] is lowest, add that coord to the parent list.
                parentListY.append(currentCheckingY - 1) #Add the UP y reference to the parent list.
                parentListX.append(currentCheckingX) #add the UP x reference to the parent list.
        
                currentCheckingY = currentCheckingY - 1 #move checking to that square on y.
                currentCheckingX = currentCheckingX #move checking to that square on x.
        
            if(score[1] < score[0] and score[1] < score[2] and score[1] <= score[3]): #if the score[1] right is lowest.
                parentListY.append(currentCheckingY + 1) #add the Right reference y to the parent list.
                parentListX.append(currentCheckingX) #add the Right reference x to the parent list.
        
                currentCheckingY = currentCheckingY + 1 #move the current Y checking to the RIGHT reference.
                currentCheckingX = currentCheckingX #move the current X checking to the RIGHT reference. 
        
            if(score[2] < score[0] and score[2] <= score[1] and score[2] <= score[3]): #if the lowest score is down.
                parentListY.append(currentCheckingY) #add the DOWN Y reference to the parent list.
                parentListX.append(currentCheckingX - 1) #add the DOWN X reference to the parent list. 
        
                currentCheckingY = currentCheckingY #make the current checking Y ref the DOWN y ref.
                currentCheckingX = currentCheckingX - 1 #make the current checking X ref the DOWN x ref.
        
            if(score[3] < score[0] and score[3] < score[1] and score[3] < score[2]): #if left is the lowest score.
                parentListY.append(currentCheckingY) #add the left y ref to the parent list.
                parentListX.append(currentCheckingX + 1) #add the left x ref to the parent list.
        
                currentCheckingY = currentCheckingY #make the current checking y the LEFT y reference.
                currentCheckingX = currentCheckingX + 1 #make the current checking X the LEFT x reference.
            #print "Currently Is", currentCheckingY, currentCheckingX
        
            if(currentCheckingX == targetX and currentCheckingY == targetY): #if we are checking the target square
                print currentCheckingY, currentCheckingX, targetY, targetX #print out debug info.
                break #leave the while loop.
            stop += 1 #count this loop.

        if stop >= 1000: #If no path can be made within 1000 loops.
            print "No path is possible location. Please retry or enter a different location." #print the error message.
            quit() #End the program.
        print "Path Found"
        self.pathListX = parentListX        #save the Y reference list.
        self.pathListY = parentListY        #save the X reference list.

        return parentListY, parentListX #pass it to the robot so it can follow the list.

        
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









