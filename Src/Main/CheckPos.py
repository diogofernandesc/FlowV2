import pygame
import Main

Black = (0 , 0, 0)
White = (255, 255, 255)
Blue = (0 , 0, 255)
Red = (255, 0, 0)
Yellow = (255, 255, 0)
Orange = (255, 100, 0)
Green = (0, 255, 0)

pos = pygame.mouse.get_pos()
mouse_x = pos[0]
mouse_y = pos[1]


def check():
    global line_colour
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    if ((int(mouse_x/100) == 5) and (int(mouse_y/100) == 0)) or ((int(mouse_x/100) == 3) and (int(mouse_y/100) == 4)):
        Main.line_colour = Main.Orange
        print("Orange")
        
    elif ((int(mouse_x/100) == 2) and (int(mouse_y/100) == 2)) or ((int(mouse_x/100) == 4) and (int(mouse_y/100) == 4)):
        Main.line_colour = Main.Red
        print("Red")
        
    elif ((int(mouse_x/100) == 1) and (int(mouse_y/100) == 2)) or ((int(mouse_x/100) == 5) and (int(mouse_y/100) == 3)):
        Main.line_colour = Main.Yellow
        print("Yellow")

        
    elif ((int(mouse_x/100) == 3) and (int(mouse_y/100) == 3)) or ((int(mouse_x/100) == 1) and (int(mouse_y/100) == 4)):
        Main.line_colour = Main.Green
        print("Green")

        
    elif ((int(mouse_x/100) == 5) and (int(mouse_y/100) == 4)) or ((int(mouse_x/100) == 3) and (int(mouse_y/100) == 5)):
        Main.line_colour = Main.Blue
        print("Blue")
