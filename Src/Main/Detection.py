import pygame
import Main

# need to fix this to work to check which circle is being clicked


def click_detection(Circle):
    ''' Check whether the user is clicking within the area of the circle by taking the x and y centre coordinates
    and subtracting the radius - the user can click up to the last point on the circle'''
    if ((Circle.ctr_x - GridCircle.radius) <= Main.x) and ((Circle.ctr_x + Circle.radius) >= Main.x):
        if ((Circle.ctr_y - Circle.radius) <= Main.y) and ((Circle.ctr_y + Circle.radius) >= Main.y):
            return True
    else:
        return False