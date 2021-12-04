"""
This module implements the snake class.
"""

from gui import Gui
from position import Position
from typing import List

global tailSize
tailSize = []
snakeShape = []
posList = []
posListTwo = []
entireBorderX = []
entireBorderY= []
pivotPoint = []
pivotPointTwo = []
tupList = []
tempList = []
class Snake:    
    def __init__(self,gui,size,tail = 0):
        self.size = size
        self.tail = tail
        tailSize.append(size)
        value = size+1
        for x in range(1,value):
            if x == size:
                snakeShape.append(">")
            else:
                snakeShape.append("+")
        #for x in range(1,size+1):
        #    if x == size:
        # #       snakeShape.append(">")
        #    else:
        #        snakeShape.append("+")
        #gui.log(snakeShape)
                
    def getCoords(self,gui):
        for x in range(gui.get_width()):
            entireBorderX.append(x)
        for y in range(gui.get_height()):
            entireBorderY.append(y)


    def borderHit(self,gui):
        gui.log("Game Over!")
        gui.quit()
        exit()
            
    def draw(self, gui,pos=None, posTwo=None):
        import apple
        import play
        self.size = self.size
        self.pos = pos
        self.posTwo = posTwo
        if len(entireBorderX) == 0:
            self.getCoords(gui)
        
        if pos == None and posTwo == None:
            if not tupList:
                self.pos = round(gui.get_width()/2)
                self.posTwo = round(gui.get_height()/2)
                tupList.append((self.pos,self.posTwo))
                for x in range(len(snakeShape)):
                    newPos = self.pos + (x+1)
                    newPosTwo = self.posTwo
                    tupList.append((newPos,newPosTwo))
                    #gui.log("This is tupList" + str(tupList))
                    #posList.append(newPos)
                    #posListTwo.append(newPosTwo)
                    self.gui = gui.draw_text(snakeShape[x],tupList[x][0],tupList[x][1],"WHITE","BLUE")
                
            else: 
                for x in range(len(snakeShape)):
                    
                    #import Apple
                    #gui.log(snakeShape)
                    #gui.log("THIS IS WHATS BEING DRAWN:" + str(tupList))
                    if tupList[0][0] > len(entireBorderX)-(self.size+1):
                        self.borderHit(gui)
                    if tupList[0][0] < 1:
                        self.borderHit(gui)
                    if tupList[0][1] > len(entireBorderY)-(self.size-1):
                        self.borderHit(gui)
                    if tupList[0][1] < 1:
                        self.borderHit(gui)
                    #for x in reversed(range(self.size)):
                    if tupList[self.size][0]-1 == apple.applePos[0] and tupList[self.size][1] == apple.applePosTwo[0]:
                        gui.log("Touch")
                        apple.trueList.clear()
                    self.gui = gui.draw_text(snakeShape[x],tupList[x][0],tupList[x][1],"WHITE","BLUE")

    def grow(self,s):
        self.size = self.size + 1
        

    def move(self,gui,up=0 ,down=0, left=0, right=0):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        
        if self.right == 1:
            snakeShape.pop()
            snakeShape.append(">")
            for x in range(0,len(snakeShape)+1):
                newDir = (tupList[x][0]+1,tupList[x][1])
                gui.log("NEWDIR" + str(newDir))
                tempList.append(newDir)
            gui.log(tempList[:4])
            for x in range(len(tempList[:4])):
                tupList.pop(x)
                tupList.insert(x,tempList[x])
            tempList.clear()
                
                
        if self.up == 1:
            snakeShape.pop()
            snakeShape.append("^")
            #pivotAmount = 0
            #newAmount = (-1,0)
            #tupList.insert(0,tupList[0][:]
            #tupList[0] = (tupList[0][0]+dir[0]),(tupList[0][1]+dir[1])
            for x in range(0,len(snakeShape)+1):
                #pivotAmount += 1
                newDir = (tupList[x][0],tupList[x][1]-1)
            #    gui.log("NEWDIR" + str(newDir))
                tempList.append(newDir)
            for x in range(len(tempList[:4])):
                tupList.pop(x)
                tupList.insert(x,tempList[x])
            tempList.clear()    
                    
        if self.left == 1:
            snakeShape.pop()
            snakeShape.append("<")
            for x in range(0,len(snakeShape)+1):
                newDir = (tupList[x][0]-1,tupList[x][1])
                gui.log("NEWDIR" + str(newDir))
                tempList.append(newDir)
            gui.log(tempList[:4])
            for x in range(len(tempList[:4])):
                tupList.pop(x)
                tupList.insert(x,tempList[x])
            tempList.clear()
            
        if self.down == 1:
            pivotAmount = 0
            snakeShape.pop()
            snakeShape.append("v")
            for x in range(0,len(snakeShape)+1):
                pivotAmount += 1
                newDir = (tupList[x][0],tupList[x][1]+1)
                gui.log("NEWDIR" + str(newDir))
                tempList.append(newDir)
            for x in range(len(tempList[:4])):
                tupList.pop(x)
                tupList.insert(x,tempList[x])
            tempList.clear() 
        
