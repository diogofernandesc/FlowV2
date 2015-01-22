import pygame
import Main
from Main import CheckPosition

# Orange Line:
def interfere():
    if Main.line_colour == Main.Orange:
        CheckPosition.pst()
        if Main.grid_position in [14,15,22,24,26,29,30,34]:
            print("false")
            Main.proceed = False #Proceed dictates whether the line will be drawn at the next centre of box (100x100)
        
        else:
            print("True")
            Main.proceed = True
            
            