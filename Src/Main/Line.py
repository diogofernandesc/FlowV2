import pygame

import Main


def linecolour(o_x1, o_y1, o_x2, o_y2, r_x1, r_y1, r_x2, r_y2, yel_x1, yel_y1, yel_x2, yel_y2, g_x1, g_y1, g_x2, g_y2, b_x1, b_y1, b_x2, b_y2):
    '''
    Determines the colour of the link to be used based on where the user clicks
    After previously getting levels from the actual Flow game, I use that to create what essentially builds a whole new level using this function:
    '''
    global line_colour
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    
    ''''t checks to see whether the grid position determined by dividing the x coordinate of the mouse and y coordinate of the mouse match with the box in which the circles should be
    If they are clicked then the line_colour variable becomes equal to the stated colour
    I got levels from the original Flow game and used the logic of this matrix:
    
    -------------------------------
    | 1  | 2  | 3  | 4  | 5  | 6  |
    -------------------------------
    | 7  | 8  | 9  | 10 | 11 | 12 |
    -------------------------------
    | 13 | 14 | 15 | 16 | 17 | 18 |
    -------------------------------
    | 19 | 20 | 21 | 22 | 23 | 24 |
    -------------------------------
    | 25 | 26 | 27 | 28 | 29 | 30 |
    -------------------------------
    | 31 | 32 | 33 | 34 | 35 | 36 |
    -------------------------------
    
    This would mean I would have circles at any one of these positions which I then enter as arguments'''
    
    if ((int(mouse_x/100) == o_x1) and (int(mouse_y/100) == o_y1)) or ((int(mouse_x/100) == o_x2) and (int(mouse_y/100) == o_y2)):
        Main.line_colour = Main.Orange
        
    elif ((int(mouse_x/100) == r_x1) and (int(mouse_y/100) == r_y1)) or ((int(mouse_x/100) == r_x2) and (int(mouse_y/100) == r_y2)):
        Main.line_colour = Main.Red
        
    elif ((int(mouse_x/100) == yel_x1) and (int(mouse_y/100) == yel_y1)) or ((int(mouse_x/100) == yel_x2) and (int(mouse_y/100) == yel_y2)):
        Main.line_colour = Main.Yellow

    elif ((int(mouse_x/100) == g_x1) and (int(mouse_y/100) == g_y1)) or ((int(mouse_x/100) == g_x2) and (int(mouse_y/100) == g_y2)):
        Main.line_colour = Main.Green

        
    elif ((int(mouse_x/100) == b_x1) and (int(mouse_y/100) == b_y1)) or ((int(mouse_x/100) == b_x2) and (int(mouse_y/100) == b_y2)):
        Main.line_colour = Main.Blue

