import pygame
import Main
import CheckPos


def click_movement():
    global coordinates
    Main.coordinates.append(CheckPos.mouse_x)
    Main.coordinates.append(CheckPos.mouse_y)
    
    if len(Main.coordinates) == 2:
        pygame.draw.aalines(Main.screen, Main.line_colour, False, [(Main.coordinates[0]),(Main.coordinates[1])], 40)
        Main.coordinates = []
        click_movement()