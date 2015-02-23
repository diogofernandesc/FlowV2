''' IN PROGRESS'''

import pygame

from Main import CheckPosition
import Main


def clicked():
    
    global Orange1Clicked
    global Orange2Clicked 
    global Red1Clicked
    global Red2Clicked
    global Yellow1Clicked
    global Yellow2Clicked
    global Green1Clicked
    global Green2Clicked
    global Blue1Clicked
    global Blue2Clicked
    global OrangeLink
    global RedLink
    global YellowLink
    global GreenLink
    global BlueLink
    CheckPosition.pst()
    print(Main.grid_position)
    
    # Orange Pair
    if Main.grid_position == 6:
        #print("Orange button 1 clicked:", Orange1Clicked)
        Main.Orange1Clicked = True
    
    elif Main.grid_position == 28:
        #print("Orange button 2 clicked:", Orange2Clicked)
        Main.Orange2Clicked = True
        
    # Red Pair
    elif Main.grid_position == 15:
        #print("Red button 1 clicked:", Red1Clicked)
        Main.Red1Clicked = True

        
    elif Main.grid_position == 29:
        #print("Red button 2 clicked:", Red2Clicked)
        Main.Red2Clicked = True
        
    # Yellow Pair
    elif Main.grid_position == 14:
        #print("Yellow button 1 clicked:", Yellow1Clicked)
        Main.Yellow1Clicked = True
        
    elif Main.grid_position == 24:
        #print("Yellow button 2 clicked:", Yellow2Clicked)
        Main.Yellow2Clicked = True
        
    # Green Pair
    elif Main.grid_position == 22:
        #print("Green button 1 clicked:", Green1Clicked)
        Main.Green1Clicked = True
        
    elif Main.grid_position == 26:
        #print("Green button 2 clicked:", Green2Clicked)
        Main.Green2Clicked = True
        
    # Blue Pair
    elif Main.grid_position ==  30:
        #print("Blue button 1 clicked:", Blue1Clicked)
        Main.Blue1Clicked = True
        
    elif Main.grid_position == 34:
        #print("Blue button 2 clicked:", Blue2Clicked)
        Main.Blue2Clicked = True
        
#WORKS:
def isConnected():
    global Orange1Clicked
    global Orange2Clicked 
    global Red1Clicked
    global Red2Clicked
    global Yellow1Clicked
    global Yellow2Clicked
    global Green1Clicked
    global Green2Clicked
    global Blue1Clicked
    global Blue2Clicked
    global OrangeLink
    global RedLink
    global YellowLink
    global GreenLink
    global BlueLink
    
    # Orange Pair:
    if Main.Orange1Clicked == True:
        # position of other circle
        if Main.grid_position == 28:
            print("link complete for Orange!")
            Main.OrangeLink = True

            
            
    if Main.Orange2Clicked == True:
        if Main.grid_position == 6:
            print("link complete for Orange!")
            Main.OrangeLink = True

            
    # Red Pair:     
    if Main.Red1Clicked == True:
        if Main.grid_position == 29:
            print("link complete for Red!")
            Main.RedLink = True

            
    if Main.Red2Clicked == True:
        if Main.grid_position == 15:
            print("Link complete for Red!")
            Main.RedLink = True

            
    # Yellow Pair:
    if Main.Yellow1Clicked == True:
        if Main.grid_position == 24:
            print("Link complete for Yellow!")
            Main.YellowLink = True

            
    if Main.Yellow2Clicked == True:
        if Main.grid_position == 14:
            print("Link complete for Yellow!")
            Main.YellowLink = True
            
    # Green Pair:
    if Main.Green1Clicked == True:
        if Main.grid_position == 26:
            print("Link complete for Green!")
            Main.GreenLink = True

            
            
    if Main.Green2Clicked == True:
        if Main.grid_position == 22:
            print("Link complete for Green!")
            Main.GreenLink = True

            
    # Blue Pair:
    if Main.Blue1Clicked == True:
        if Main.grid_position == 34:
            print("Link complete for Blue!")
            Main.BlueLink = True

            
    if Main.Blue2Clicked == True:
        if Main.grid_position == 30:
            print("Link complete for Blue!")
            Main.BlueLink = True

        
    