''' IN PROGRESS'''

import pygame

import Main


# Function used to tell player that a specific link has been complete
# Will work by creating greyed out text for each link, as it is completed it will be coloured in to the correct colour
def complete_status():
    
    # Link complete text:
    linkcomplete_font = pygame.font.SysFont(None, 25)
    linkcomplete_text = linkcomplete_font.render("Links complete:", True, Main.White)
    Main.screen.blit(linkcomplete_text,(5,755))
    
    #Greyed out:
    
    # Red Link:
    REDgrey_font = pygame.font.SysFont(None, 25)
    REDgrey_text = REDgrey_font.render("Red Link", True, Main.VeryDarkGrey)
    Main.screen.blit(REDgrey_text,(25,777))
    
    # Orange Link:
    ORANGEgrey_font = pygame.font.SysFont(None, 25)
    ORANGEgrey_text = ORANGEgrey_font.render("Orange Link", True, Main.VeryDarkGrey)
    Main.screen.blit(ORANGEgrey_text,(125,777))
    
    # Yellow Link:
    YELLOWgrey_font = pygame.font.SysFont(None, 25)
    YELLOWgrey_text = YELLOWgrey_font.render("Yellow Link", True, Main.VeryDarkGrey)
    Main.screen.blit(YELLOWgrey_text,(255,777))
    
    # Green Link:
    GREENgrey_font = pygame.font.SysFont(None, 25)
    GREENgrey_text = GREENgrey_font.render("Green Link", True, Main.VeryDarkGrey)
    Main.screen.blit(GREENgrey_text,(375,777))
    
    # Blue Link:
    BLUEgrey_font = pygame.font.SysFont(None, 25)
    BLUEgrey_text = BLUEgrey_font.render("Blue Link", True, Main.VeryDarkGrey)
    Main.screen.blit(BLUEgrey_text,(485,777))
    
    
def link_complete(link_colour):
    
    if link_colour == "red":
        # Red Link:
        REDgrey_font = pygame.font.SysFont(None, 25)
        REDgrey_text = REDgrey_font.render("Red Link", True, Main.Red)
        Main.screen.blit(REDgrey_text,(25,777))
    
    elif link_colour == "orange":
        # Orange Link:
        ORANGEgrey_font = pygame.font.SysFont(None, 25)
        ORANGEgrey_text = ORANGEgrey_font.render("Orange Link", True, Main.Orange)
        Main.screen.blit(ORANGEgrey_text,(125,777))
    
    elif link_colour == "yellow":
        # Yellow Link:
        YELLOWgrey_font = pygame.font.SysFont(None, 25)
        YELLOWgrey_text = YELLOWgrey_font.render("Yellow Link", True, Main.Yellow)
        Main.screen.blit(YELLOWgrey_text,(255,777))
    
    elif link_colour == "green":
        # Green Link:
        GREENgrey_font = pygame.font.SysFont(None, 25)
        GREENgrey_text = GREENgrey_font.render("Green Link", True, Main.Green)
        Main.screen.blit(GREENgrey_text,(375,777))
    
    elif link_colour == "blue":
        # Blue Link:
        BLUEgrey_font = pygame.font.SysFont(None, 25)
        BLUEgrey_text = BLUEgrey_font.render("Blue Link", True, Main.Blue)
        Main.screen.blit(BLUEgrey_text,(485,777))
    
    


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
        
    elif Main.grid_position == redgp2:
        Main.Red2Clicked = True

    # Orange Pair
    elif Main.grid_position == orangegp1:
        Main.Orange1Clicked = True
        
    elif Main.grid_position == orangegp2:
        Main.Orange2Clicked = True
            
    # Yellow Pair
    elif Main.grid_position == yellowgp1:
        Main.Yellow1Clicked = True
        
    elif Main.grid_position == yellowgp2:
        Main.Yellow2Clicked = True
        
    # Green Pair
    elif Main.grid_position == greengp1:
        Main.Green1Clicked = True
        
    elif Main.grid_position == greengp2:
        Main.Green2Clicked = True

    # Blue Pair
    elif Main.grid_position ==  bluegp1:
        Main.Blue1Clicked = True 
        
    elif Main.grid_position == bluegp2:
        Main.Blue2Clicked = True
    
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
            Main.OrangeLink = True
            link_complete("orange")

            
            
    if Main.Orange2Clicked == True:
        if Main.grid_position == orangegp1:
            Main.OrangeLink = True
            link_complete("orange")

            
    # Red Pair:     
    if Main.Red1Clicked == True:
        if Main.grid_position == redgp2:
            Main.RedLink = True
            link_complete("red")

            
    if Main.Red2Clicked == True:
        if Main.grid_position == redgp1:
            Main.RedLink = True
            link_complete("red")

            
    # Yellow Pair:
    if Main.Yellow1Clicked == True:
        if Main.grid_position == yellowgp2:
            Main.YellowLink = True
            link_complete("yellow")

            
    if Main.Yellow2Clicked == True:
        if Main.grid_position == yellowgp1:
            Main.YellowLink = True
            link_complete("yellow")
            
    # Green Pair:
    if Main.Green1Clicked == True:
        if Main.grid_position == greengp2:
            Main.GreenLink = True
            link_complete("green")

            
            
    if Main.Green2Clicked == True:
        if Main.grid_position == greengp1:
            Main.GreenLink = True
            link_complete("green")

            
    # Blue Pair:
    if Main.Blue1Clicked == True:
        if Main.grid_position == bluegp2:
            Main.BlueLink = True
            link_complete("blue")

            
    if Main.Blue2Clicked == True:
        if Main.grid_position == bluegp1:
            Main.BlueLink = True
            link_complete("blue")

        
    