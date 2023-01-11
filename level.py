import pygame                                                                       #import library
from mazeGen import *

class Level:                                                                        #level class so later can be called with different numbers to create different mazes
    
    def __init__(self, y, x, screenSize, imageSize):
        self.mazeLevel = LevelGen(y,x).createLevel()
        self.entrance  = self.mazeLevel[0].index(2)

        
        
        self.tile = {"0":pygame.image.load(r'Images\white.png').convert(), "1":pygame.image.load(r'Images\brick.png').convert(), 
                    "2":pygame.image.load(r'Images\door.jpg').convert_alpha(), "3":pygame.image.load(r'Images\opendoor.jpg').convert()}                #images that will be created on surface

        for i in self.tile:
            self.tile[i] = pygame.transform.scale(self.tile[i],(imageSize))
        self.map = pygame.Surface((screenSize[0], screenSize[1]))                                           #creation of surface
        

        for i in range(y):                                                     #for in a foor loop that will change every number in list of lists to an image and draw it on surface (our level)
            for j in range(x):
                self.mazeLevel[i][j] = str(self.mazeLevel[i][j])
                self.map.blit(self.tile[self.mazeLevel[i][j]], (j * (imageSize[0]), i * (imageSize[1])))   



  