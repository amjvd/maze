import random                                   #Importing random library to be used

class LevelGen(object):                       #declaring LevelGen class to carry out level generation algorithm which will create a random level for maze
    def __init__(self, height, width):       #will be called with LevelGen(height,width)     
        self.height = height                 #variables needed in functions
        self.width = width                  
        self.level = []                     #creating 3 lists, level being for the level map(list of lists)
        self.walls = []                     #walls to store walls temporiarly to implement algorithm
        
        

        

    def surroundingSpace(self, randomWall):        # function to find how much empty space a wall is surronded by (to be used to make only one exit path in level)
        emptySpace = 0
        if (self.level[randomWall[0]-1][randomWall[1]] == 0):
            emptySpace += 1
        if (self.level[randomWall[0]+1][randomWall[1]] == 0):
            emptySpace += 1
        if (self.level[randomWall[0]][randomWall[1]-1] == 0):
            emptySpace +=1
        if (self.level[randomWall[0]][randomWall[1]+1] == 0):
            emptySpace += 1
        return emptySpace

    def deleteWall(self, randomWall):                   #function to delete  random wall from list of walls after its been used to not repeat walls and create maze
        for self.wall in self.walls:
            if (self.wall[0] == randomWall[0] and self.wall[1] == randomWall[1]):
                self.walls.remove(self.wall)  


    def createLevel(self):
        for i in range(self.height):                  #create a  level list of lists full of 4s (4 to show prims algorithm not used)
            self.line = []                      #line being for each list in level map
            for j in range(self.width):                    #and lists size depandant on height and width when calling class
                self.line.append(4)
            self.level.append(self.line)
            #print(self.level)

        self.wall = 1

        starty = random.randint(0, self.height - 1)                                #picks random starting postion(y component) (picks which list from the list of lists)
        startx = random.randint(0, self.width - 1)                               #picks random starting postion(x component) (picks which value in list)
        if starty == 0:                                                     #makes sure starting position is not the first list, as we want a border of walls around level
            starty += 1
        if starty == self.height-1:                                              #makes sure starting position is not last list as we want a border of walls around level
            starty -= 1
        if startx == 0:                                                     #makes sure starting position is not first value in any list as we want border of walls
            startx += 1
        if startx == self.width-1:                                               #makes sure starting position is not last value in any list as we want border of walls
            startx -= 1

        self.level[starty][startx] = 0                                      #stores starting position of level as 0 (empty space) and values around it as walls in wall list for prims algorithm
        self.walls.append([starty+1,startx])
        self.walls.append([starty-1,startx])
        self.walls.append([starty,startx+1])
        self.walls.append([starty,startx-1])

        self.level[starty+1][startx] = 1                                    #saves new walls in level list temporarily
        self.level[starty-1][startx] = 1
        self.level[starty][startx+1] = 1
        self.level[starty][startx-1] = 1

        while self.walls:                                                               #prims algorithm to find Min spanning tree, we know to still carry on while loop if temp list of walls still has values
            randomWall = self.walls[random.randint(0, len(self.walls)-1)]                  #Pick random wall
                
            if randomWall[1] != 0:                                                      #If random wall is LEFT WALL and if space to left still hasnt been converted from 4
                if self.level[randomWall[0]][randomWall[1]-1] == 4 and self.level[randomWall[0]][randomWall[1]+1] == 1:
                    self.emptySpace = self.surroundingSpace(randomWall)   #surronding space of specfic random wall
                    if self.emptySpace < 2:                         
                        self.level[randomWall[0]][randomWall[1]] = 0 #If theres less than 2 surronding space turn wall into empty space in level (path)
                            
                        if randomWall[0] != 0:                                      #Checking space above the wall and making more walls
                            if self.level[randomWall[0]-1][randomWall[1]] != 0:
                                self.level[randomWall[0]-1][randomWall[1]] = 1
                            if [randomWall[0]-1, randomWall[1]] not in self.walls:
                                self.walls.append([randomWall[0]-1, randomWall[1]])

                        
                        if (randomWall[0] != self.height-1):                        #Checking space below the wall and making more walls
                            if (self.level[randomWall[0]+1][randomWall[1]] != 0):
                                self.level[randomWall[0]+1][randomWall[1]] = 1
                            if ([randomWall[0]+1, randomWall[1]] not in self.walls):
                                self.walls.append([randomWall[0]+1, randomWall[1]])

                        
                        if (randomWall[1] != 0):                                    #Checking space left to wall
                            if (self.level[randomWall[0]][randomWall[1]-1] != 0):
                                self.level[randomWall[0]][randomWall[1]-1] = 1
                            if ([randomWall[0], randomWall[1]-1] not in self.walls):
                                self.walls.append([randomWall[0], randomWall[1]-1])
            

                    
                    self.deleteWall(randomWall)         #DELETE WALL FROM WALL LIST TO NOT REPEAT

                    continue

            
            if (randomWall[0] != 0):                        #CHECK FOR UP WALL SAME FOR FIRST WALL BUT DIFFERENT SPACES HAVE TO BE CHECKED
                if (self.level[randomWall[0]-1][randomWall[1]] == 4 and self.level[randomWall[0]+1][randomWall[1]] == 0):

                    self.emptySpace = self.surroundingSpace(randomWall)
                    if (self.emptySpace < 2):
                        
                        self.level[randomWall[0]][randomWall[1]] = 0

                        
                        
                        if (randomWall[0] != 0):                                #CHECK SPACE ABOVE WALL
                            if (self.level[randomWall[0]-1][randomWall[1]] != 0):
                                self.level[randomWall[0]-1][randomWall[1]] = 1
                            if ([randomWall[0]-1, randomWall[1]] not in self.walls):
                                self.walls.append([randomWall[0]-1, randomWall[1]])

                        
                        if (randomWall[1] != 0):                                #CHECK LEFT SPACE TO WALL
                            if (self.level[randomWall[0]][randomWall[1]-1] != 0):
                                self.level[randomWall[0]][randomWall[1]-1] = 1
                            if ([randomWall[0], randomWall[1]-1] not in self.walls):
                                self.walls.append([randomWall[0], randomWall[1]-1])

                        
                        if (randomWall[1] != self.width-1):                     #CHECK RIGHT SPACE TO WALL
                            if (self.level[randomWall[0]][randomWall[1]+1] != 0):
                                self.level[randomWall[0]][randomWall[1]+1] = 1
                            if ([randomWall[0], randomWall[1]+1] not in self.walls):
                                self.walls.append([randomWall[0], randomWall[1]+1])

                    
                    self.deleteWall(randomWall)                             #DELETE WALL AFTER USE
                    
                    continue

            
            if (randomWall[0] != self.height-1):                    #FOR BOTTOM WALL
                if (self.level[randomWall[0]+1][randomWall[1]] == 4 and self.level[randomWall[0]-1][randomWall[1]] == 0):

                    self.emptySpace = self.surroundingSpace(randomWall)
                    if (self.emptySpace < 2):
                        
                        self.level[randomWall[0]][randomWall[1]] = 0

                        
                        if (randomWall[0] != self.height-1):
                            if (self.level[randomWall[0]+1][randomWall[1]] != 0):
                                self.level[randomWall[0]+1][randomWall[1]] = 1
                            if ([randomWall[0]+1, randomWall[1]] not in self.walls):
                                self.walls.append([randomWall[0]+1, randomWall[1]])
                        if (randomWall[1] != 0):
                            if (self.level[randomWall[0]][randomWall[1]-1] != 0):
                                self.level[randomWall[0]][randomWall[1]-1] = 1
                            if ([randomWall[0], randomWall[1]-1] not in self.walls):
                                self.walls.append([randomWall[0], randomWall[1]-1])
                        if (randomWall[1] != self.width-1):
                            if (self.level[randomWall[0]][randomWall[1]+1] != 0):
                                self.level[randomWall[0]][randomWall[1]+1] = 1
                            if ([randomWall[0], randomWall[1]+1] not in self.walls):
                                self.walls.append([randomWall[0], randomWall[1]+1])

                    
                    self.deleteWall(randomWall)     #DELETE WALL AFTER USE


                    continue

            # Check the right wall
            if (randomWall[1] != self.width-1):                 #FOR RIGHT WALL
                if (self.level[randomWall[0]][randomWall[1]+1] == 4 and self.level[randomWall[0]][randomWall[1]-1] == 0):

                    self.emptySpace = self.surroundingSpace(randomWall)
                    if (self.emptySpace < 2):
                        
                        self.level[randomWall[0]][randomWall[1]] = 0

                        
                        if (randomWall[1] != self.width-1):
                            if (self.level[randomWall[0]][randomWall[1]+1] != 0):
                                self.level[randomWall[0]][randomWall[1]+1] = 1
                            if ([randomWall[0], randomWall[1]+1] not in self.walls):
                                self.walls.append([randomWall[0], randomWall[1]+1])
                        if (randomWall[0] != self.height-1):
                            if (self.level[randomWall[0]+1][randomWall[1]] != 0):
                                self.level[randomWall[0]+1][randomWall[1]] = 1
                            if ([randomWall[0]+1, randomWall[1]] not in self.walls):
                                self.walls.append([randomWall[0]+1, randomWall[1]])
                        if (randomWall[0] != 0): 
                            if (self.level[randomWall[0]-1][randomWall[1]] != 0):
                                self.level[randomWall[0]-1][randomWall[1]] = 1
                            if ([randomWall[0]-1, randomWall[1]] not in self.walls):
                                self.walls.append([randomWall[0]-1, randomWall[1]])
                    
                    self.deleteWall(randomWall)     #DELETE WALL AFTER USE
    


            self.deleteWall(randomWall)   #delete wall anyway to end algorithm

            
           
            

        for i in range(0, self.height):                              #any values in lists that have not been converted to wall or empty space, convert to wall as not needed.
            for j in range(0, self.width):
                if self.level[i][j] == 4:
                    self.level[i][j] = 1





        for i in range(0, self.width):                           #Takes one of the top border wall values that is connected to empty space as entrance/exit 
            if self.level[1][i] == 0:
                self.level[0][i] = 2
                break

        for i in range(self.width-1, 0, -1):                     #Takes one of the bottom border wall values that is connected to empty space as entrance/exit (CHOOSES FROM THE END FIRST TO ENSURE BEST MAZE)
            if self.level[self.height-2][i] == 0:
                self.level[self.height-1][i] = 3
                break


        return self.level

        

        










