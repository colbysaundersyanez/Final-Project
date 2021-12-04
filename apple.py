"""
This module represents the apple that appears at random places on the screen.
"""
import random
from random import seed
from random import randint
from typing import List

from gui import Gui
from position import Position



maxValue = 50
posList = []
posListTwo = []
#global eaten
global redraw
redraw = False
lengthList = []
applePos = []
applePosTwo = []
global trueList
trueList = []

#applePos = position
def collides(p, positions):
    """Return true if p is any of the positions in the list."""
    for position in positions:
        if p.get_x() == position.get_x() and p.get_y == position.get_y():
            return True
    return False



class Apple:
    
    """The apple's location is randomly generated."""
    def __init__(self):
        pass

    def draw(self, gui):
        if bool(trueList) == False and redraw == False:
            applePos.clear()
            applePosTwo.clear()
            value = randint(4,gui.get_width()-4)
            valueTwo = randint(4,gui.get_height()-4)
            gui.draw_text("*",value,valueTwo,"WHITE","RED")
            applePos.append(value)
            applePosTwo.append(valueTwo)
            applePosition = Position(value,valueTwo)
            trueList.append(1)
        else:
            gui.draw_text("*",applePos[0],applePosTwo[0],"WHITE","RED")
