#
 #   This file contains all the code for the image recognition and arena generation systems
#
#   The arena method of the following class uses the following values to represent roads:
#       * 0 - Non-road. just generally something we don't care about.
#       * 1 - Normal road
#        * 2 - Fast Road
class arena:        #Class for the arena

    arena = None #Array which is the arena. Containing the road values 
    im_arr = None #Array containing all the images for the map.
    full_image = None   #Variable to contain a copy of the map image.
    grid_y = 0          #Variables holding the amount of tiles we can get out of an image.
    grid_x = 0 
    
    height = 0
    width = 0

    color_percentage = 5   #The percentage of color that must be in a tile for it to be counted as a road or not Higher means the roads must be bigger to register
    tile_size        = 10   #The size of individual tiles. 

    def __init__(self,image):
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

        while tmpwidth % self.tile_size != 0:  #Check that width is divisble by 20. If it isnt then take away one until it is.
            tmpwidth -= 1

        self.grid_y = tmpwidth / self.tile_size #Once it is, then divide if by 20 and save that number.
   
        tmpheight = height

        while tmpheight % self.tile_size != 0:  #Do the same for height
            tmpheight -= 1

        self.grid_x = tmpheight / self.tile_size

        print 
        print self.grid_y, self.grid_x
        
        #Now we have the amount of grid boxes we should have. We can create and array with that amount of values.
        #TODO Should save the tiles in an array for future referance. Will fix if have time.
        self.im_arr = [[im for x in range(self.grid_y)] for x in range(self.grid_x)]  #We make sure to make each an object of type im (an image from the PIL)
        self.arena = [[0 for x in range(self.grid_y)] for x in range(self.grid_x)]  #We make sure to make each an object of type im (an image from the PIL)

        print "Size of im_arr"
        print len(self.arena)

        left = 0 #Set the initial coordinates
        upper = 0 
        right = self.tile_size 
        lower = self.tile_size
        
        
        col = 0 #Set the counts
        row = 0
        
        while row < self.grid_x:  #While we havent reached the bottom of the image
            
            while col < self.grid_y: #While we havent reached the edge
                cp = im.crop((left,upper,lower,right)) #Crop the image into a tile
                self.im_arr[row][col] = cp  #Store the crop
                self.arena[row][col] = self.analyse_tile(cp, row, col) #Analyse the tile
                cp.save("/home/samathy/maptst/"+str(row)+"_"+str(col), "PNG")  #Here for debug
                left += self.tile_size  #Increase coordinates to move alone to the right
                lower += self.tile_size
                col += 1 #Store what col we're on
            upper += self.tile_size #Increase and reset coordinates to move to the next row.
            left =0
            lower = self.tile_size
            right += self.tile_size
            print col
            col = 0

            row += 1 #Make sure we store what row we're on. 


        return




    def ret_element_value (self, row, column):  #Returns the value of the specified arena element. 
        return arena[row][column]
    
    def ret_element_image (self, row, column):    #Returns the array element image in given argument element.
        return self.arena[row][column]
    
    def put(self, start_row, start_col, obj_val):   #Function to insert a given value into a given element.
        self.arena[start_row][start_col] = obj_val  #Insert the object value into the starting row for only one element.
        return

    def put(self, start_row, start_col, second_row, second_col, obj_val):
        self.arena[start_row][start_col] = obj_val
        self.arena[second_row][second_col] = obj_val
        return

    def put(self, start_row, start_col, end_row, end_col, obj_val):
        self.arena[start_row][start_col] = obj_val
        self.arena[start_row][end_col]
        self.arena[end_row][start_col]
        self.arena[end_row][end_col]
        return

    def analyse_tile (self,im, row, column):       #Puts the road value (is road, isnt road) into the arena array AND returns road value for the specified column/height element.
        
        colors = None
        tile_size = [im.size[0],  im.size[1]]   #Get the size of the tile to make sure we can get all the colours. We probs dont need this as we can use class data, but hey

        colors = im.getcolors(tile_size[0]*tile_size[1])
        
        colors.sort() #Sort the colours
        colors.reverse()    #Reverse so that the most used colours are at the start of the list.

        percentage = (len(colors) * self.color_percentage) / 100   #Calculate what the percentage of colours we need to pass to register the tile as something
      
        if len(colors) < 10:
            col_range = len(colors)
        else:
            col_range = 10


        for x in range(0, col_range):  #Check to of the top ranking colours to see if there is a large amount of road colours in that image
            if colors[x][1] == (222,225,225) or colors[x][1] == (255,255,255): #The colour is the white of a road, so make it a road!
                if colors[x][0] >= percentage:   #Make sure that the number of that colour type is more than what ever percentage of the whole tile
                    print 
                    self.arena[row][column] = 1
                    return 1
            elif colors[x][1] == (255, 225, 104): #If the colour is the yellow of a fast road then make the arena value = a fast road!
                if colors[x][0] >= percentage:   #Make sure that the number of that colour type is more than what ever percentage of the whole tile
                    self.arena[row][column] = 2
                    return 2
            else:                               #Else it must just be nothing we care about.
                self.arena[row][column] = 3
                return 0
        return

    
    def show_arena(self):
        inc = 0
        for row in self.arena:
            print inc,
            print row
            inc +=2
        return

ar = arena("screenshot1.png") #This is here so one can run this script as a stand alone test. Might cause wacky behaviour if this is used as a module
print "---------------------------------------------------------------------------------------------------------"
ar.show_arena()
