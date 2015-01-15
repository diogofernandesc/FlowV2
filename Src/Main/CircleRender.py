import Main
import pygame

ctr_x_list = []
ctr_y_list = []


class grid_circle(pygame.sprite.Sprite):
    # Stationary circles class you need a pair of each colour
    def __init__(self, ctr_x, ctr_y, colour):
        pygame.sprite.Sprite.__init__(self)
        self.ctr_x = ctr_x
        self.ctr_y = ctr_y
        self.radius = 40
        self.colour = colour
            
    def render(self):
        # Render method draws circles at the stated position and colour given by the parameters
        pygame.draw.circle(Main.screen, self.colour, (self.ctr_x, self.ctr_y), self.radius, 40)
        ctr_x_list.append(self.ctr_x)
        ctr_y_list.append(self.ctr_y)
        line_colour = self.colour
        
            

