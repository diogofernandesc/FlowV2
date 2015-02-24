import pygame

import Main


def click_movement():
    global coordinates
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    mouse_coordinates = (mouse_x, mouse_y)
    Main.coordinates.append(mouse_coordinates)
    
    
    if len(Main.coordinates) == 2:
        pygame.draw.lines(Main.screen, Main.line_colour, False, [[Main.coordinates[0]], [Main.coordinates[1]]], 40)
        Main.coordinates = []
        click_movement()
        
        