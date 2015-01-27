import pygame
import Main

def pst():
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    
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
        Main.line_colour = Main.Orange
        
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
        Main.line_colour = Main.Yellow

        
    elif ((int(mouse_x/100) == 2) and (int(mouse_y/100) == 2)):
        Main.line_colour = Main.Red
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
        Main.line_colour = Main.Green
        
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
