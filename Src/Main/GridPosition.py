import pygame
import Main

def pst():
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    
    if ((int(mouse_x/100) == 0) and (int(mouse_y/100) == 0)):
        Main.grid_position = 1
        Main.draw_ctr = (50,50)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 1) and (int(mouse_y/100) == 0)):
        Main.grid_position = 2
        Main.draw_ctr = (150,50)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 2) and (int(mouse_y/100) == 0)):
        Main.grid_position = 3
        Main.draw_ctr = (250,50)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 3) and (int(mouse_y/100) == 0)):
        Main.grid_position = 4
        Main.draw_ctr = (350,50)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 4) and (int(mouse_y/100) == 0)):
        Main.grid_position = 5
        Main.draw_ctr = (450,50)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 5) and (int(mouse_y/100) == 0)):
        Main.grid_position = 6
        Main.draw_ctr = (550,50)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 0) and (int(mouse_y/100) == 1)):
        Main.grid_position = 7
        Main.draw_ctr = (50,150)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 1) and (int(mouse_y/100) == 1)):
        Main.grid_position = 8
        Main.draw_ctr = (150,150)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 2) and (int(mouse_y/100) == 1)):
        Main.grid_position = 9
        Main.draw_ctr = (250,150)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 3) and (int(mouse_y/100) == 1)):
        Main.grid_position = 10
        Main.draw_ctr = (350,150)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 4) and (int(mouse_y/100) == 1)):
        Main.grid_position = 11
        Main.draw_ctr = (450,150)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 5) and (int(mouse_y/100) == 1)):
        Main.grid_position = 12
        Main.draw_ctr = (550,150)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 0) and (int(mouse_y/100) == 2)):
        Main.grid_position = 13
        Main.draw_ctr = (50,250)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 1) and (int(mouse_y/100) == 2)):
        Main.grid_position = 14
        Main.draw_ctr = (150,250)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 2) and (int(mouse_y/100) == 2)):
        Main.grid_position = 15
        Main.draw_ctr = (250,250)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 3) and (int(mouse_y/100) == 2)):
        Main.grid_position = 16
        Main.draw_ctr = (350,250)
        Main.coordinates.append(Main.draw_ctr)
                
    elif ((int(mouse_x/100) == 4) and (int(mouse_y/100) == 2)):
        Main.grid_position = 17
        Main.draw_ctr = (450,250)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 5) and (int(mouse_y/100) == 2)):
        Main.grid_position = 18
        Main.draw_ctr = (550,250)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 0) and (int(mouse_y/100) == 3)):
        Main.grid_position = 19
        Main.draw_ctr = (50,350)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 1) and (int(mouse_y/100) == 3)):
        Main.grid_position = 20
        Main.draw_ctr = (150,350)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 2) and (int(mouse_y/100) == 3)):
        Main.grid_position = 21
        Main.draw_ctr = (250,350)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 3) and (int(mouse_y/100) == 3)):
        Main.grid_position = 22
        Main.draw_ctr = (350,350)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 4) and (int(mouse_y/100) == 3)):
        Main.grid_position = 23
        Main.draw_ctr = (450,350)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 5) and (int(mouse_y/100) == 3)):
        Main.grid_position = 24
        Main.draw_ctr = (550,350)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 0) and (int(mouse_y/100) == 4)):
        Main.grid_position = 25
        Main.draw_ctr = (50,450)
        Main.coordinates.append(Main.draw_ctr)
    
    elif ((int(mouse_x/100) == 1) and (int(mouse_y/100) == 4)):
        Main.grid_position = 26
        Main.draw_ctr = (150,450)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 2) and (int(mouse_y/100) == 4)):
        Main.grid_position = 27
        Main.draw_ctr = (250,450)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 3) and (int(mouse_y/100) == 4)):
        Main.grid_position = 28
        Main.draw_ctr = (350,450)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 4) and (int(mouse_y/100) == 4)):
        Main.grid_position = 29
        Main.draw_ctr = (450,450)
        Main.coordinates.append(Main.draw_ctr)
    
    elif ((int(mouse_x/100) == 5) and (int(mouse_y/100) == 4)):
        Main.grid_position = 30
        Main.draw_ctr = (550,450)
        Main.coordinates.append(Main.draw_ctr)
        
        
    elif ((int(mouse_x/100) == 0) and (int(mouse_y/100) == 5)):
        Main.grid_position = 31
        Main.draw_ctr = (50,550)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 1) and (int(mouse_y/100) == 5)):
        Main.grid_position = 32
        Main.draw_ctr = (150,550)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 2) and (int(mouse_y/100) == 5)):
        Main.grid_position = 33
        Main.draw_ctr = (250,550)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 3) and (int(mouse_y/100) == 5)):
        Main.grid_position = 34
        Main.draw_ctr = (350,550)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 4) and (int(mouse_y/100) == 5)):
        Main.grid_position = 35
        Main.draw_ctr = (450,550)
        Main.coordinates.append(Main.draw_ctr)
        
    elif ((int(mouse_x/100) == 5) and (int(mouse_y/100) == 5)):
        Main.grid_position = 36
        Main.draw_ctr = (550,550)
        Main.coordinates.append(Main.draw_ctr)
        
        