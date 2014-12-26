#
#   This file contains all the code for the image recognition and arena generation systems
#

class arena:        #Class for the arena

    arena = None #Array which is the arena. 2D array this time to make things easier.
    im_arr = None #Array containing all the images for the map.
    full_image = None   #Variable to contain a copy of the map image.
    grid_y = 0
    
    height = 0
    width = 0

    def __init__(self,image):
        import PIL #import python image lib
        import Image #Apparently Image is a seperate lib
        

        self.full_image = Image.open(image) #get a copy of the image
        
        print "Size of image:"
        print im.size
        image_size = im.size
       
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
        print len(self.im_arr)

        row = 0
        column = 0
        row_count = 0 #Count variables here to increment by 1 instead of 20 each time. This counts the amount times we've looped
        column_count = 0
        while row_count < height: #While we havent done all the rows
            while column_count < width: #While we havent done all the columns
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
                    #cp.save("/home/samathy/maptst/"+str(column_count)+"-"+str(row_count), "PNG") #Debugging line - Saves the produced images to disk

            row = row_count+20 #Once we've done one whole row, increase the row coords by 20
            column = column+20  #and also the count of rows we've done
            column_count = 0    #reset the columns coords
            column = 0          #TODO Thing seems to work but i think these are in error
            row_count += 1
        return




    def ret_element_value (self, width, height):  #Returns the value of the specified arena element. 
        
        return arena[width][height]
    
    def ret_element_image (self, width, height):    #Returns the array element image in given argument element.
        return self.arena[width][height]
    

ar = arena("/home/samathy/map.png") #This is here so one can run this script as a stand alone test. Might cause wacky behaviour if this is used as a module

