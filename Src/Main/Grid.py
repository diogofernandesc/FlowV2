import pygame


scr_size = (600, 600)
screen = pygame.display.set_mode(scr_size)
White = (255, 255, 255)

# --- grid built here:
    
def build_grid():
    ''' You need two arrays to define the starting and end positions of the line:
    Because it draws lines, they take two pairs of x-coordinates; one for the start of the line and one for the end'''
    
    x_grid_interval1 = [100, 0]
    x_grid_interval2 = [100, 600]  
        
    y_grid_interval1 = [0 , 100]
    y_grid_interval2 = [600, 100]
        
    i = 0  # Initiating control variable for the loop
    while i != 6:
        ''' ***Very important***:
        - This while loop is used to control the intervals in which the lines are drawn for the grid
        - 600x600 grid so divided by 6 gives 100px intervals
        - So it will draw the initial line at the initial coordinates above
        - Then increments by 100 which is the amount of pixels in both directions that the lines will be separated by
        - i is looped 5 times because 5 lines are drawn in each direction'''
        
        pygame.draw.line(screen, White, x_grid_interval1, x_grid_interval2)
        x_grid_interval1[0] += 100
        x_grid_interval2[0] += 100 
            
        # The above code deals with vertical lines - incrementing the x values of the coordinates of the lines
        # Means loop will draw a new line 100 pixels ahead of the previous
            
        pygame.draw.line(screen, White, y_grid_interval1, y_grid_interval2)
        y_grid_interval1[1] += 100
        y_grid_interval2[1] += 100
            
        i += 1  # increment control variable to continue looping
            

