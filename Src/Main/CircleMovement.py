import pygame
import Main

'''
def choose_circle():
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    Main.coordinates.append(mouse_x)
    Main.coordinates.append(mouse_y)
    
    # Orange Circle 1:
    if ((int(mouse_x/100) == 5) and (int(mouse_y/100) == 0)):
        pygame.draw.aalines(Main.screen, Main.line_colour, False, [(Main.OrangeCircle1.ctr_x, Main.OrangeCircle1.ctr_y),(Main.coordinates[0], Main.coordinates[1])], 40)
        if len(Main.coordinates) == 2:
            choose_circle()
    
    # Orange Circle 2:
    elif ((int(mouse_x/100) == 3) and (int(mouse_y/100) == 4)):
        Main.circle == "Orange2"
        print(int(mouse_x/100))
        print(int(mouse_y/100))
        Main.coordinates.append(mouse_x)
    
    if circle == "Orange":
        print("hello")
'''   
    
def click_movement():
    global coordinates
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    Main.coordinates.append(mouse_x)
    Main.coordinates.append(mouse_y)
    
    
    if len(Main.coordinates) == 2:
        pygame.draw.lines(Main.screen, Main.line_colour, False, [([Main.coordinates[0]]),([Main.coordinates[1], Main.coordinates[2]])], 40)
        Main.coordinates = []
        click_movement()