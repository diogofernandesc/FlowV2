import pygame

import Main


def pst():
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    
    '''
    Carries out a calculation to check that if the mouse is inside one of the desired squares:
    Dividing by 100 returning an integer gives one value like so with this matrix:
    
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
    
    '''
    
    if ((int(mouse_x/100) == 0) and (int(mouse_y/100) == 0)):
        Main.grid_position = 1

    elif ((int(mouse_x/100) == 1) and (int(mouse_y/100) == 0)):
        Main.grid_position = 2

    elif ((int(mouse_x/100) == 2) and (int(mouse_y/100) == 0)):
        Main.grid_position = 3

    elif ((int(mouse_x/100) == 3) and (int(mouse_y/100) == 0)):
        Main.grid_position = 4

    elif ((int(mouse_x/100) == 4) and (int(mouse_y/100) == 0)):
        Main.grid_position = 5
        
    elif ((int(mouse_x/100) == 5) and (int(mouse_y/100) == 0)):
        Main.grid_position = 6

        
    elif ((int(mouse_x/100) == 0) and (int(mouse_y/100) == 1)):
        Main.grid_position = 7
        
    elif ((int(mouse_x/100) == 1) and (int(mouse_y/100) == 1)):
        Main.grid_position = 8

    elif ((int(mouse_x/100) == 2) and (int(mouse_y/100) == 1)):
        Main.grid_position = 9

        
    elif ((int(mouse_x/100) == 3) and (int(mouse_y/100) == 1)):
        Main.grid_position = 10

        
    elif ((int(mouse_x/100) == 4) and (int(mouse_y/100) == 1)):
        Main.grid_position = 11

    elif ((int(mouse_x/100) == 5) and (int(mouse_y/100) == 1)):
        Main.grid_position = 12

        
    elif ((int(mouse_x/100) == 0) and (int(mouse_y/100) == 2)):
        Main.grid_position = 13
        
    elif ((int(mouse_x/100) == 1) and (int(mouse_y/100) == 2)):
        Main.grid_position = 14


        
    elif ((int(mouse_x/100) == 2) and (int(mouse_y/100) == 2)):
        Main.grid_position = 15

        
    elif ((int(mouse_x/100) == 3) and (int(mouse_y/100) == 2)):
        Main.grid_position = 16

                
    elif ((int(mouse_x/100) == 4) and (int(mouse_y/100) == 2)):
        Main.grid_position = 17
        
    elif ((int(mouse_x/100) == 5) and (int(mouse_y/100) == 2)):
        Main.grid_position = 18

    elif ((int(mouse_x/100) == 0) and (int(mouse_y/100) == 3)):
        Main.grid_position = 19

    elif ((int(mouse_x/100) == 1) and (int(mouse_y/100) == 3)):
        Main.grid_position = 20

    elif ((int(mouse_x/100) == 2) and (int(mouse_y/100) == 3)):
        Main.grid_position = 21
        
    elif ((int(mouse_x/100) == 3) and (int(mouse_y/100) == 3)):
        Main.grid_position = 22

        
    elif ((int(mouse_x/100) == 4) and (int(mouse_y/100) == 3)):
        Main.grid_position = 23
        
    elif ((int(mouse_x/100) == 5) and (int(mouse_y/100) == 3)):
        Main.grid_position = 24
        
    elif ((int(mouse_x/100) == 0) and (int(mouse_y/100) == 4)):
        Main.grid_position = 25
    
    elif ((int(mouse_x/100) == 1) and (int(mouse_y/100) == 4)):
        Main.grid_position = 26

    elif ((int(mouse_x/100) == 2) and (int(mouse_y/100) == 4)):
        Main.grid_position = 27
        
    elif ((int(mouse_x/100) == 3) and (int(mouse_y/100) == 4)):
        Main.grid_position = 28

        
    elif ((int(mouse_x/100) == 4) and (int(mouse_y/100) == 4)):
        Main.grid_position = 29

    elif ((int(mouse_x/100) == 5) and (int(mouse_y/100) == 4)):
        Main.grid_position = 30

        
    elif ((int(mouse_x/100) == 0) and (int(mouse_y/100) == 5)):
        Main.grid_position = 31
        
    elif ((int(mouse_x/100) == 1) and (int(mouse_y/100) == 5)):
        Main.grid_position = 32

        
    elif ((int(mouse_x/100) == 2) and (int(mouse_y/100) == 5)):
        Main.grid_position = 33
        
    elif ((int(mouse_x/100) == 3) and (int(mouse_y/100) == 5)):
        Main.grid_position = 34
        
    elif ((int(mouse_x/100) == 4) and (int(mouse_y/100) == 5)):
        Main.grid_position = 35
        
    elif ((int(mouse_x/100) == 5) and (int(mouse_y/100) == 5)):
        Main.grid_position = 36
