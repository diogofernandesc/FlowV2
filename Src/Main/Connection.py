import pygame
import Main
from Main import CheckPosition

Orange1Clicked = False
Orange2Clicked = False

''' IN PROGRESS '''

def clicked():
    global Orange1Clicked
    global Orange2Clicked 
    # Orange Pair
    if Main.grid_position == 6:
        print(Orange1Clicked)
        Orange1Clicked = True 
    
    elif (Main.line_colour == Main.Orange) and (Main.grid_position == 28):
        print(Orange2Clicked)
        Orange2Clicked = True

#WORKS:
def isConnected():
    clicked()
    global Orange1Clicked
    global Orange2Clicked 
    CheckPosition.pst()
    
    # Orange Pair
    if Orange1Clicked == True:
        if Main.grid_position == 28:
            print("link complete!")
            
    if Orange2Clicked == True:
        if Main.grid_position == 6:
            print("link complete!")
        

        
    