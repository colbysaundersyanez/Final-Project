from gui import Gui

gui = Gui()
def main():
                      

    continuePlaying = True
    while continuePlaying:       
        c = gui.get_keyPress()   
        if c == "KEY_UP":
            break                           
    gui.clear()                                 
    gui.refresh()             
    time.sleep(0.1)          

                           
gui.quit()    
