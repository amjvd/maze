from level import *                 #import libraries and level class to be used
from button import *
import pygame
import pygame._sdl2 as sdl2
import sys
import random
import time
import  pyodbc
pygame.init() 
conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=.\Database\data.accdb;')  

class MazeGame:                     #Maze class that will be called when user presses Maze on mainpage

    def __init__(self):
        self.y, self.x = 15, 20
        self.clock = pygame.time.Clock()                    #Setting clock variable that will allow us to change how fast the program runs (how fast the while loop iterates)
        self.screenSize = (960,720)
        self.screen = pygame.display.set_mode(self.screenSize)    #setting screen dimensions
        self.window = sdl2.Window.from_display_module()
        self.player = pygame.image.load(r'Images\guy.png').convert_alpha()    #Setting player image that will move on screen
        self.enemy = pygame.image.load(r'Images\enemy.png').convert_alpha()
        self.heart1 = pygame.image.load(r'Images\heart.png').convert_alpha()
        self.heart2 = pygame.image.load(r'Images\heart.png').convert_alpha()
        self.heart3 = pygame.image.load(r'Images\heart.png').convert_alpha()
        self.emptyHeart = pygame.image.load(r'Images\emptyHeart.png').convert_alpha()
        self.hearts = 3
        self.delay, self.enemyDelay = 320,0


        

    def font(self, size):
        return pygame.font.SysFont("Cambria", size)
    
    
    def run(self):
        self.imageSize = [self.screenSize[0]/self.x, self.screenSize[1]/self.y]
        self.level = Level(self.y, self.x, self.screenSize, self.imageSize)
        self.playerPos =  [0,self.level.entrance]
        self.enemyPos = [self.y-3,self.level.exit]
        

        self.player = pygame.transform.scale(self.player,(self.imageSize))
        self.enemy = pygame.transform.scale(self.enemy,(self.imageSize))
        self.heart1 = pygame.transform.scale (self.heart1,(48,48))
        self.heart2 = pygame.transform.scale (self.heart2,(48,48))
        self.heart3 = pygame.transform.scale (self.heart3,(48,48))


        while True:                                             
            self.time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:                       #If screen is closed pygame stops running and program stops
                    pygame.quit()                                   
                    sys.exit()


            
            self.screen.fill((0,0,0))                               #fills screen to white at the start of each iteration to clear any previous unwated images
            self.screen.blit(self.level.map, (0, 0))                #draws level surface on our display
            self.screen.blit(self.player,(self.playerPos[1] * (self.imageSize[0]), self.playerPos[0] * (self.imageSize[1])))  #draws player image where our pos variable is and *32 to get display coordinates
            self.screen.blit(self.enemy,(self.enemyPos[1] * self.imageSize[0], self.enemyPos[0] * self.imageSize[1]))
            self.screen.blit(self.heart1,(0 * 48, 0 * 48))
            self.screen.blit(self.heart2,(1 * 48, 0 * 48))
            self.screen.blit(self.heart3,(2 * 48, 0 * 48))

            key = pygame.key.get_pressed()                 #set variable to store key pressed
            if self.playerPos == self.enemyPos:
                self.hearts -= 1
                if self.hearts == 2:
                    self.heart3 = self.emptyHeart
                    
                    self.run()
                elif self.hearts ==1:
                    self.heart2 = self.emptyHeart
                
                    self.run()

            directions = ["up","down","left","right"]
            
            
            
            if self.time > self.enemyDelay:
                for i in directions:
                    i = random.choice(directions)
                
                    if i == "up" and self.level.mazeLevel[self.enemyPos[0]-1][self.enemyPos[1]]  != "1" :
                        if self.level.mazeLevel[self.enemyPos[0]-1][self.enemyPos[1]]  != "2":
                            self.enemyPos[0] -= 1
                            self.enemyDelay += self.delay

                        
                            
                    elif i == "down" and self.level.mazeLevel[self.enemyPos[0]+1][self.enemyPos[1]]  != "1":
                        if self.level.mazeLevel[self.enemyPos[0]+1][self.enemyPos[1]]  != "3":
                            self.enemyPos[0] += 1
                            self.enemyDelay += self.delay
                    
                    elif i == "left" and self.level.mazeLevel[self.enemyPos[0]][self.enemyPos[1]-1]  != "1" :                 
                        self.enemyPos[1] -= 1
                        self.enemyDelay += self.delay
                    
                    elif i == "right" and self.level.mazeLevel[self.enemyPos[0]][self.enemyPos[1]+1]  != "1" :
                        self.enemyPos[1] += 1
                        self.enemyDelay += self.delay

            

            if self.level.mazeLevel[self.playerPos[0]][self.playerPos[1]]  == "3":    #Check to see if our position is on end square 
                self.question()
            if key[pygame.K_a]:                                                     #Check what key was pressed and if possible to move in that direction (no walls in way)
                if self.level.mazeLevel[self.playerPos[0]][self.playerPos[1]-1]  != "1" :                 
                    self.playerPos[1] -= 1
            elif key[pygame.K_d]:
                if self.level.mazeLevel[self.playerPos[0]][self.playerPos[1]+1]  != "1" :
                    self.playerPos[1] += 1
            elif key[pygame.K_w]:
                if self.level.mazeLevel[self.playerPos[0]-1][self.playerPos[1]]  != "1" :
                    self.playerPos[0] -= 1
            elif key[pygame.K_s]: 
                if self.level.mazeLevel[self.playerPos[0]+1][self.playerPos[1]]  != "1" :
                    self.playerPos[0] += 1


            pygame.display.update()                                         #update display after everything is done
            self.clock.tick(32)                                             #speed of iteration (fps)

    def difficulty(self):
        while True:
            

            self.screen.fill((234,210,168))
            mousePos = pygame.mouse.get_pos()
            difficultyText = self.font(50).render("DIFFICULTY:", True, ("White"))
            difficlutyRect = difficultyText.get_rect(center = ((self.screenSize[0]/2), 42)) 
            easyButton = Button(pygame.image.load("Images\Button.png"), (self.screenSize[0]/2,150), "EASY", self.font(50), "#d7fcd4" , "Black")
            mediumButton = Button(pygame.image.load("Images\Button.png"), (self.screenSize[0]/2,275), "MEDIUM", self.font(50), "#d7fcd4" , "Black")
            hardButton = Button(pygame.image.load("Images\Button.png"), (self.screenSize[0]/2,400), "HARD", self.font(50), "#d7fcd4" , "Black")
            
            self.screen.blit(difficultyText, difficlutyRect)

            for button in [easyButton, mediumButton, hardButton]:
                button.changeColour(mousePos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN :
                    if easyButton.checkForInput(mousePos):
                        self.x = 20
                        self.y = 15
                        self.run()
                    if mediumButton.checkForInput(mousePos):
                        self.x = 40
                        self.y = 30
                        self.run()
                    if hardButton.checkForInput(mousePos):
                        self.x = 80
                        self.y = 60
                        self.run()


            pygame.display.update()
            self.clock.tick(32)

    def settings(self):

        while True:
            self.screen.fill((234,210,168))
            mousePos = pygame.mouse.get_pos()
            settingsText = self.font(50).render("SETTINGS", True, ("White"))
            settingsRect = settingsText.get_rect(center = (self.screenSize[0]/2, 42))
            size1280 = Button(pygame.image.load("Images\Button.png"), (self.screenSize[0]/2,150), "1280x960", self.font(50), "#d7fcd4" , "Black")
            size960 = Button(pygame.image.load("Images\Button.png"), (self.screenSize[0]/2,275), "960x720", self.font(50), "#d7fcd4" , "Black")
            size640 = Button(pygame.image.load("Images\Button.png"), (self.screenSize[0]/2,400), "640x480", self.font(50), "#d7fcd4" , "Black")
            backButton = Button(pygame.image.load("Images\Back.png").set_colorkey((0, 0, 0)), (self.screenSize[0]/2 -200,400), "BACK", self.font(50), "#d7fcd4" , "Black")

            self.screen.blit(settingsText, settingsRect)

            for button in [size1280, size960, size640,backButton]:
                button.changeColour(mousePos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN :
                    if size1280.checkForInput(mousePos):
                        self.screenSize = (1280,960)
                        self.screen = pygame.display.set_mode(self.screenSize)
                        self.window.position = sdl2.WINDOWPOS_CENTERED

                    if size960.checkForInput(mousePos):
                        self.screenSize = (960,720)
                        self.screen = pygame.display.set_mode(self.screenSize)
                        self.window.position = sdl2.WINDOWPOS_CENTERED
                
                    if size640.checkForInput(mousePos):
                        self.screenSize = (640,480)
                        self.screen = pygame.display.set_mode(self.screenSize)
                        self.window.position = sdl2.WINDOWPOS_CENTERED
                    if backButton.checkForInput(mousePos):
                        self.mainMenu()


            pygame.display.update()
            self.clock.tick(32)




    def mainMenu(self):

        while True:
            

            self.screen.fill((234,210,168))
            mousePos = pygame.mouse.get_pos()
            menuText = self.font(50).render("MAZE MENU", True, ("White"))
            menuRect = menuText.get_rect(center = (self.screenSize[0]/2, 42))
            startButton = Button(pygame.image.load("Images\Button.png"), (self.screenSize[0]/2,150), "PLAY", self.font(50), "#d7fcd4" , "Black")
            settingsButton = Button(pygame.image.load("Images\Button.png"), (self.screenSize[0]/2,275), "SETTINGS", self.font(50), "#d7fcd4" , "Black")
            backButton = Button(pygame.image.load("Images\Button.png"), (self.screenSize[0]/2,400), "BACK", self.font(50), "#d7fcd4" , "Black")

            self.screen.blit(menuText, menuRect)

            for button in [startButton, settingsButton, backButton]:
                button.changeColour(mousePos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN :
                    if startButton.checkForInput(mousePos):
                        self.difficulty()
                    if settingsButton.checkForInput(mousePos):
                        self.settings()
                    if backButton.checkForInput(mousePos):
                        pygame.quit()
                        #sys.exit()
                        return


            pygame.display.update()
            self.clock.tick(32)

    def question(self):
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()                                   #opens database
        cursor.execute('SELECT * From mathsQuestions')

        record = cursor.fetchall()
        conn.close()                                            #closes database

        uname = ""                                              #creates new variables to be used to save database info 
        pword = ""
        name = ""

        for i in record:                                        #sets name variable to first field which is name field, uname variable to the second field in the database which is the username field, and sets pword to the third field which is password field
            question = [random.randit(0,2)][0]
            uname = row[2]
            pword = row[3]

        userAnswer = ''
        answerBox = pygame.Rect(200,200,140,32)




        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        answer = answer[0:-1]
                    else:
                        answer += event.unicode

                                

            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen,(255,255,255),answerBox,2)
            answerSurface = self.font(32).render(answer,True,(255,255,255))
            self.screen.blit(answerSurface,(answerBox.x, answerBox.y))

            pygame.display.update()
            self.clock.tick(32)
        


maze = MazeGame()
maze.question()


