import test_lists


def aStar():
    arena1 = test_lists.arena1
    targetX = 43    #Target landmark
    targetY = 10 
    
    locationX = 20  #Location Of the robot
    locationY = 20
    
    currentCheckingY = locationY
    currentCheckingX = locationX
    
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
           
        if(score[0] <= score[1] and score[0] < score[2] and score[0] <= score[3]):
            parentListY.append(currentCheckingY - 1)
            parentListX.append(currentCheckingX)
    
            currentCheckingY = currentCheckingY - 1
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
    
    print "complete"
    
           
    
    
    
    
    
           
