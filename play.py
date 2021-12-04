"""
This is the main program for the snake game.
"""

import time

from gui import Gui
from room import Room
from snake import Snake
from apple import Apple

ini = 0
def main():
    try:
        # Create the new Gui and start it. This clears the screen
        # and the Gui now controls the screen
        gui = Gui()
        # Create the room, the snake and the apple.
        # You will need to change the constructors later to pass more
        # information to the Snake and Apple constructors
        room = Room(gui.get_width(), gui.get_height(), "#", "WHITE", "BLUE")
        snake = Snake(gui)
        apple = Apple()
        right = True
        up = False
        down = False
        left = False
        #apple.redraw = False

        redraw = False
        # The main loop of the game. Use "break" to break out of the loop
        continuePlaying = True
        while continuePlaying:
            c = gui.get_keypress()
            if c == "KEY_UP":
                up = True
                right = False
                down = False
                left = False
            if c == "KEY_DOWN":
                right = False
                up = False
                down = True
                left = False
            if c == "KEY_LEFT":
                right = False
                up = False
                down = False
                left = True
                snake.move(gui,0,0,1,0)
            if c == "KEY_RIGHT":
                right = True
                up = False
                down = False
                left = False
                snake.move(gui,0,0,0,1)
            if c == "q":
                gui.quit()
                exit()

            
            gui.clear()
            
            room.draw(gui)
            #if snake.appleEaten(gui) == True:
            #    gui.log("SUCESSS")
            #    apple.trueList.clear()
            if redraw == False:
                apple.draw(gui)
        
            #if redraw == True:
            #    gui.log("TRUEEEEE")
            #    apple.trueList == False
            snake.draw(gui)
            if right == True:
                snake.move(gui,0,0,0,1)
            if left == True:
                snake.move(gui,0,0,1,0)
            if up == True:
                snake.move(gui,1,0,0,0)
            if down == True:
                snake.move(gui,0,1,0,0)

            # When done redrawing all the elements of the screen, refresh will
            # make the new graphic appear on the screen all at once
            gui.refresh()

            # Detect whether the snake ate the apple, or it hit the wall
            # or it hit its own tail here

            # This call makes the program go quiescent for some time, so
            # that it doesn't run so fast. If the value in the call to
            # time.sleep is decreased, the game will speed up.
            time.sleep(0.1)

    except Exception as e:
        gui.quit()
        raise e

    gui.quit()

    # The game has ended since we broke out of the main loop
    # Display the user's score here
    


if __name__ == "__main__":
    main()
