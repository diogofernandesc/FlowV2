''' IN PROGRESS'''

import pygame

from Main import CheckPosition
import Main


def clicked(orangegp1, orangegp2, redgp1, redgp2, yellowgp1, yellowgp2, greengp1, greengp2, bluegp1, bluegp2):  # colour grid position 1 and colour grid position 2
    
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
    
    
    # Red Pair
    if Main.grid_position == redgp1:
        Main.Red1Clicked = True
        print("Red button 1 clicked:", Main.Red1Clicked)
        
    elif Main.grid_position == redgp2:
        Main.Red2Clicked = True
        print("Red button 2 clicked:", Main.Red2Clicked)

    # Orange Pair
    elif Main.grid_position == orangegp1:
        Main.Orange1Clicked = True
        print("Orange button 1 clicked:", Main.Orange1Clicked)
        
    elif Main.grid_position == orangegp2:
        Main.Orange2Clicked = True
        print("Orange button 2 clicked:", Main.Orange2Clicked)
            
    # Yellow Pair
    elif Main.grid_position == yellowgp1:
        Main.Yellow1Clicked = True
        print("Yellow button 1 clicked:", Main.Yellow1Clicked)
        
    elif Main.grid_position == yellowgp2:
        Main.Yellow2Clicked = True
        print("Yellow button 2 clicked:", Main.Yellow2Clicked)
        
    # Green Pair
    elif Main.grid_position == greengp1:
        Main.Green1Clicked = True
        print("Green button 1 clicked:", Main.Green1Clicked)
        
    elif Main.grid_position == greengp2:
        Main.Green2Clicked = True
        print("Green button 2 clicked:", Main.Green2Clicked)

    # Blue Pair
    elif Main.grid_position ==  bluegp1:
        Main.Blue1Clicked = True 
        print("Blue button 1 clicked:", Main.Blue1Clicked)
        
    elif Main.grid_position == bluegp2:
        Main.Blue2Clicked = True
        print("Blue button 2 clicked:", Main.Blue2Clicked)
    
#WORKS:
def isConnected(orangegp1, orangegp2, redgp1, redgp2, yellowgp1, yellowgp2, greengp1, greengp2, bluegp1, bluegp2):
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
        if Main.grid_position == orangegp2:
            print("link complete for Orange!")
            Main.OrangeLink = True

            
            
    if Main.Orange2Clicked == True:
        if Main.grid_position == orangegp1:
            print("link complete for Orange!")
            Main.OrangeLink = True

            
    # Red Pair:     
    if Main.Red1Clicked == True:
        if Main.grid_position == redgp2:
            print("link complete for Red!")
            Main.RedLink = True

            
    if Main.Red2Clicked == True:
        if Main.grid_position == redgp1:
            print("Link complete for Red!")
            Main.RedLink = True

            
    # Yellow Pair:
    if Main.Yellow1Clicked == True:
        if Main.grid_position == yellowgp2:
            print("Link complete for Yellow!")
            Main.YellowLink = True

            
    if Main.Yellow2Clicked == True:
        if Main.grid_position == yellowgp1:
            print("Link complete for Yellow!")
            Main.YellowLink = True
            
    # Green Pair:
    if Main.Green1Clicked == True:
        if Main.grid_position == greengp2:
            print("Link complete for Green!")
            Main.GreenLink = True

            
            
    if Main.Green2Clicked == True:
        if Main.grid_position == greengp1:
            print("Link complete for Green!")
            Main.GreenLink = True

            
    # Blue Pair:
    if Main.Blue1Clicked == True:
        if Main.grid_position == bluegp2:
            print("Link complete for Blue!")
            Main.BlueLink = True

            
    if Main.Blue2Clicked == True:
        if Main.grid_position == bluegp1:
            print("Link complete for Blue!")
            Main.BlueLink = True

        
    