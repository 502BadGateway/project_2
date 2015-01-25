import random
import wikipedia
import sys
reload(sys)
class robot:


    def __init__(self, name, x, y): #Constructor

        self.locationX = x 
        self.locationY = y 
        self.name = name 
        rnd = random.randint(1,2)
        self.image = "ASSETS/chuckle-"+str(rnd)+".png"  #Open the robot image

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


    def treasureCheck(self, arena, treasureLandmark, treasureLandmark1, treasureLandmark2, treasureLandmark3, paulPoints): #this method checks to see if the landmark that the robot has arrived at has any treasure
            if self.ret_element_val(self.locationX,self.locationY) == treasureLandmark1: #if the coodinates the robot is at is what has been selected to be treasrueLandmark1 then add a point to robots score
                print "Treasure 1 Found"
                self.paulPoints = self.paulPoints + 1 #adds points to robot. not sure if I need to do this for both robots.

            elif self.ret_element_val(self.locationX,self.locationY) == treasureLandmark2: #if the coodinates the robot is at is what has been selected to be treasrueLandmark2 then add a point to robots score
                print "Treasure 2 Found"
                self.paulPoints = self.paulPoints + 1


            elif self.ret_element_val(self.locationX,self.locationY) == treasureLandmark3: #if the coodinates the robot is at is what has been selected to be treasrueLandmark3 then add a point to robots score
                print "Treasure 3 Found"
                self.paulPoints = self.paulPoints + 1
            else:
                print "No Treasrue at this landmark"


    
    def returnLocationX(self):
        return self.locationX
    def returnLocationY(self):
        return self.locationY
    def returnImage(self):
        return self.image









