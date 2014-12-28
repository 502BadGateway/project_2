#
#   This file contains all the code for the image recognition and arena generation systems
#
#   The arena method of the following class uses the following values to represent roads:
#       * 0 - Non-road. just generally something we don't care about.
#       * 1 - Normal road
#       * 2 - Fast Road

from multiprocessing import Process, Lock, Pipe    #We have to import this here so that if we run this script as a standalone for testing we get the required stuff
class arena:        #Class for the arena

    arena = None #Array which is the arena. Containing the road values 
    im_arr = None #Array containing all the images for the map.
    full_image = None   #Variable to contain a copy of the map image.
    grid_y = 0
    
    height = 0
    width = 0

    mutex = Lock()  #Lock object to control acsess to the arena variable for the threading thing.

    thread_stack = list()  #A list of threads for the threading bit

    def __init__(self,image):
        import multiprocessing   #import the threading module
        import multiprocessing    #We have to import this here so that if we run this script as a standalone for testing we get the required stuff
        import PIL #import python image lib
        import Image #Apparently Image is a seperate lib
        

        self.full_image = Image.open(image) #get a copy of the image
        im = self.full_image 
        print "Size of image:"
        print self.full_image.size
        image_size = self.full_image.size
       
        #break the image up into little squares
    
        width = image_size[0]
        height = image_size[1]
        print height, width 
        
        #Get the number of 20x20 boxes we should be able to get. TODO Does this actually need to be here?
        tmpwidth = width

        while tmpwidth % 20 != 0:  #Check that width is divisble by 20. If it isnt then take away one until it is.
            tmpwidth -= 1

        self.grid_y = tmpwidth / 20 #Once it is, then divide if by 20 and save that number.
   
        tmpheight = height

        while tmpheight % 20 != 0:  #Do the same for height
            tmpheight -= 1

        self.grid_x = tmpheight / 20
        
        #Now we have the amount of grid boxes we should have. We can create and array with that amount of values.
        self.im_arr = [[im for x in range(width)] for x in range(height)]  #We make sure to make each an object of type im (an image from the PIL)
        self.arena = [[im for x in range(width)] for x in range(height)]  #We make sure to make each an object of type im (an image from the PIL)
        print len(self.im_arr)

        row = 0
        column = 0
        row_count = 0 #Count variables here to increment by 1 instead of 20 each time. This counts the amount times we've looped
        column_count = 0
        mstr_count = 0
        num_threads = 0
        pipe = [None]  * (width*height)
        self.thread_stack = [] *(width*height)



        while row_count < height: #While we havent done all the rows
            while column_count < width: #While we havent done all the columns

                while num_threads != mstr_count:    #while the number of threads that have returned data is not equal to the amount of threads
                    while x < mstr_count:
                        if type(pipe[x]) == NoneType:
                            break
                        if pipe[x].poll() != False:                 #check if the current peice of data
                            tmp_dat = pipe[x].recv()
                            self.arena[tmp_dat[0],tmp_dat[1]] = tmp_dat[2] 
                            num_threads += 1
                        x += 1
                
                im = self.full_image    #refresh im with the full image
                if column_count == width or column >= width: #make sure we dont get "index out of range"
                    break
                else:
                    print row, column, row+20, column+20 #dbg
                    cp =  im.crop((row,column, row+20 , column+20)) #Crop a 20x20 square out of the image, specified by the column coods and row coords
                    self.im_arr[column_count][row_count] = im.crop((row,column, row+20 , column+20)) #Put that cropped image into the proper place in the array of parts.
                    print "into "+str(row_count)+":"+str(column_count)  #dbg
                    column = column+20 #Increase the column by 20
                    column_count += 1 #Increase the amount of columns we've worked with by 1
                    #Split off the analysing of a tile into a thread, add that thread to a new element of the thread stack. We don't call the start method of this yet.
                    print "master count: "+ str(mstr_count)
                    print "Pipe lenght: "+ str(len(pipe))
                    pipe[mstr_count] = Pipe() #Create a new pipe object
                    self.thread_stack.append(Process(target=self.analyse_tile, args=(pipe[mstr_count][0], column_count, row_count)))  #Call the analyse frame function on each of the tiles. Should fill the road array with data
                    #self.thread_stack[mstr_count].start()
                    #cp.save("/home/samathy/maptst/"+str(column_count)+"-"+str(row_count), "PNG") #Debugging line - Saves the produced images to disk
                    mstr_count += 1 #Counts everytime we add one thing. 

            row = row_count+20 #Once we've done one whole row, increase the row coords by 20
            column = column+20  #and also the count of rows we've done
            column_count = 0    #reset the columns coords
            column = 0          #TODO Thing seems to work but i think these are in error 
            row_count += 1

            print "wtf" 
#        for x in range(0, len(p)):  #For each element of the list of threads to be started 
#            self.thread_stack[x].start()        #start them
#
#        while num_threads != mstr_count:    #while the number of threads that have returned data is not equal to the amount of threads
#            while x < mstr_count:
#                if pipe[x].poll() != False:                 #check if the current peice of data
#                    tmp_dat = pipe[x].recv()
#                    self.arena[tmp_dat[0],tmp_dat[1]] = tmp_dat[2] 
#                    num_threads += 1
#                x += 1

        return




    def ret_element_value (self, column, row):  #Returns the value of the specified arena element. 
        return arena[column][row]
    
    def ret_element_image (self, column, row):    #Returns the array element image in given argument element.
        return self.arena[column][row]

    def analyse_tile (self,pipe,column, row):       #Puts the road value (is road, isnt road) into the arena array AND returns road value for the specified column/height element.
        print type(pipe) 
        print pipe
        self.mutex.acquire()
        tile_size = [self.im_arr[column][row].size[0],  self.im_arr[column][row].size[1]]   #Get the size of the tile to make sure we can get all the colours.
        self.mutex.release() 
        print "first"

        self.mutex.acquire()
        colors = self.im_arr[column][row].getcolors(tile_size[0]*tile_size[1]) #Should put all the colour data for the part of the image into the var colour.
        self.mutex.release() 

        print "second"
        
        colors.sort() #Sort the colours
        print "sorted"
        colors.reverse()    #Reverse so that the most used colours are at the start of the list.
        for x in range(0, 10):  #Check to of the top ranking colours to see if there is a large amount of road colours in that image
            print "looping"
            if colors[x][1] == (222,225,225): #The colour is the white of a road, so make it a road!
                pipe.send((column,row,1))   # Send the value through da pipe.
                break
            elif colors[x][1] == (255, 225, 104): #If the colour is the yellow of a fast road then make the arena value = a fast road!
                pipe.send((column,row,2))
                break
            elif x >=9 :                               #Else it must just be nothing we care about.
                pipe.send((column,row,0))
                break
        pipe.close()
        return self.arena[column][row]


ar = arena("/home/samathy/map.png") #This is here so one can run this script as a stand alone test. Might cause wacky behaviour if this is used as a module

