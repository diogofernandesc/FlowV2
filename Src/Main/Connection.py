import pygame
import Main
from Main import CheckPosition

# Condition variables for clicks
Orange1Clicked = False
Orange2Clicked = False
Red1Clicked = False
Red2Clicked = False
Yellow1Clicked = False
Yellow2Clicked = False
Green1Clicked = False
Green2Clicked = False
Blue1Clicked = False
Blue2Clicked = False

# Condition variables for links
OrangeLink = False
RedLink = False
YellowLink = False
GreenLink = False
BlueLink = False


''' IN PROGRESS '''

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
    
    # Orange Pair
    if Main.grid_position == 6:
        #print("Orange button 1 clicked:", Orange1Clicked)
        Orange1Clicked = True 
    
    elif Main.grid_position == 28:
        #print("Orange button 2 clicked:", Orange2Clicked)
        Orange2Clicked = True

    # Red Pair
    elif Main.grid_position == 15:
        #print("Red button 1 clicked:", Red1Clicked)
        Red1Clicked = True
        
    elif Main.grid_position == 29:
        #print("Red button 2 clicked:", Red2Clicked)
        Red2Clicked = True
        
    # Yellow Pair
    elif Main.grid_position == 14:
        #print("Yellow button 1 clicked:", Yellow1Clicked)
        Yellow1Clicked = True
        
    elif Main.grid_position == 24:
        #print("Yellow button 2 clicked:", Yellow2Clicked)
        Yellow2Clicked = True
        
    # Green Pair
    elif Main.grid_position == 22:
        #print("Green button 1 clicked:", Green1Clicked)
        Green1Clicked = True
        
    elif Main.grid_position == 26:
        #print("Green button 2 clicked:", Green2Clicked)
        Green2Clicked = True
        
    # Blue Pair
    elif Main.grid_position ==  30:
        #print("Blue button 1 clicked:", Blue1Clicked)
        Blue1Clicked = True
        
    elif Main.grid_position == 34:
        #print("Blue button 2 clicked:", Blue2Clicked)
        Blue2Clicked = True

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
    CheckPosition.pst()
    
    # Orange Pair:
    if Orange1Clicked == True:
        # position of other circle
        if Main.grid_position == 28:
            print("link complete for Orange!")
            OrangeLink = True
            
            
    elif Orange2Clicked == True:
        if Main.grid_position == 6:
            print("link complete for Orange!")
            OrangeLink = True
    
    # Red Pair:     
    elif Red1Clicked == True:
        if Main.grid_position == 29:
            print("link complete for Red!")
            RedLink = True
            
    elif Red2Clicked == True:
        if Main.grid_position == 15:
            print("Link complete for Red!")
            RedLink = True
            
    # Yellow Pair:
    elif Yellow1Clicked == True:
        if Main.grid_position == 24:
            print("Link complete for Yellow!")
            YellowLink = True
            
    elif Yellow2Clicked == True:
        if Main.grid_position == 14:
            print("Link complete for Yellow!")
            YellowLink = True
            
    # Green Pair:
    elif Green1Clicked == True:
        if Main.grid_position == 26:
            print("Link complete for Green!")
            GreenLink = True
            
    elif Green2Clicked == True:
        if Main.grid_position == 22:
            print("Link complete for Green!")
            GreenLink = True
            
    # Blue Pair:
    elif Blue1Clicked == True:
        if Main.grid_position == 34:
            print("Link complete for Blue!")
            BlueLink = True
            
    elif Blue2Clicked == True:
        if Main.grid_position == 30:
            print("Link complete for Blue!")
            BlueLink = True
            
        

        
    