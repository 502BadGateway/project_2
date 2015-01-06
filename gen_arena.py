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
    grid_y = 0
    
    height = 0
    width = 0

    color_percentage = 15   #The percentage of color that must be in a tile for it to be counted as a road or not Higher means the roads must be bigger to register
    tile_size        = 20   #The size of individual tiles. 

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

        while tmpwidth % 20 != 0:  #Check that width is divisble by 20. If it isnt then take away one until it is.
            tmpwidth -= 1

        self.grid_y = tmpwidth / 20 #Once it is, then divide if by 20 and save that number.
   
        tmpheight = height

        while tmpheight % 20 != 0:  #Do the same for height
            tmpheight -= 1

        self.grid_x = tmpheight / 20
        
        #Now we have the amount of grid boxes we should have. We can create and array with that amount of values.
        self.im_arr = [[im for x in range(width)] for x in range(height)]  #We make sure to make each an object of type im (an image from the PIL)
        self.arena = [[0 for x in range(width)] for x in range(height)]  #We make sure to make each an object of type im (an image from the PIL)
        print len(self.im_arr)

        left = 0 #Set the initial coordinates
        upper = 0 
        right = self.tile_size 
        lower = self.tile_size
        
        
        col = 0 #Set the counts
        row = 0
        
        while upper < height:  #While we havent reached the bottom of the image
            while left < width: #While we havent reached the edge
                cp = im.crop((left,upper,lower,right)) #Crop the image into a tile
                self.im_arr[col][row] = cp  #Store the crop
                #self.arena[col][row] = self.analyse_tile(cp, col, row) #Analyse the tile
                cp.save("/home/samathy/maptst/"+str(row)+"_"+str(col), "PNG")  #Here for debug
                left += self.tile_size  #Increase coordinates to move alone to the right
                lower += self.tile_size
                col += 1 #Store what col we're on
            upper += self.tile_size #Increase and reset coordinates to move to the next row.
            left =0
            lower = self.tile_size
            right += self.tile_size

            row += 1 #Make sure we store what row we're on. 


        return




    def ret_element_value (self, column, row):  #Returns the value of the specified arena element. 
        return arena[column][row]
    
    def ret_element_image (self, column, row):    #Returns the array element image in given argument element.
        return self.arena[column][row]

    def analyse_tile (self,im, column, row):       #Puts the road value (is road, isnt road) into the arena array AND returns road value for the specified column/height element.
        
        colors = None
        tile_size = [im.size[0],  im.size[1]]   #Get the size of the tile to make sure we can get all the colours. We probs dont need this as we can use class data, but hey

        #colors = self.im_arr[column][row].getcolors(tile_size[0]*tile_size[1]) #Should put all the colour data for the part of the image into the var colour.
        colors = im.getcolors(tile_size[0]*tile_size[1])
        print "colors"
        print colors
        
        colors.sort() #Sort the colours
        colors.reverse()    #Reverse so that the most used colours are at the start of the list.

        percentage = (len(colors) * self.color_percentage) / 100   #Calculate what the percentage of colours we need to pass to register the tile as something
        print "Length of colours: "+str(len(colors))
        print "percentage: "+str(percentage)
        
        if len(colors) < 10:
            col_range = len(colors)
        else:
            col_range = 10


        for x in range(0, col_range):  #Check to of the top ranking colours to see if there is a large amount of road colours in that image
            print colors[0][1]
            if colors[x][1] == (222,225,225) or colors[x][1] == (255,255,255): #The colour is the white of a road, so make it a road!
                print "Colors are equal to a ROAD"
                if colors[x][0] >= percentage:   #Make sure that the number of that colour type is more than what ever percentage of the whole tile
                    print "Road"
                    self.arena[column][row] = 1
                    print "into: "+ str((column, row))
                    print self.arena[column][row]
                    return 1
            elif colors[x][1] == (255, 225, 104): #If the colour is the yellow of a fast road then make the arena value = a fast road!
                print "Colors are equal to a Fast ROAD"
                print colors[x]
                if colors[x][0] >= percentage:   #Make sure that the number of that colour type is more than what ever percentage of the whole tile
                    print "Fast Road"
                    self.arena[column][row] = 2
                    return 2
            else:                               #Else it must just be nothing we care about.
                self.arena[column][row] = 0
                return 0
        return

    
    def show_arena(self):
        inc = 0
        for row in self.arena:
            print inc,
            print row
            inc +=2
        return

ar = arena("/home/samathy/not_a_map_test.png") #This is here so one can run this script as a stand alone test. Might cause wacky behaviour if this is used as a module
print "---------------------------------------------------------------------------------------------------------"
#ar.show_arena()
