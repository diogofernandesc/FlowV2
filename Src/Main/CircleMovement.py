import pygame

def click_movement():
    global coordinates
    [x, y] = event.pos
    print(event.pos)
    coordinates.append(event.pos)
    if len(coordinates) == 2:
        pygame.draw.lines(screen, line_colour, False, [(coordinates[0]),(coordinates[1])], 20)
        coordinates = []
        click_movement()