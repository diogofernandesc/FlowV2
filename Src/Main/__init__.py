import pygame
import pygame.gfxdraw
from Main import Grid, CircleRender, CircleMovement, CheckPos, GridPosition, Interference, Connection, CheckPosition


# Defining colours for the circles, paths(lines) and grid background

Black = (0 , 0, 0)
White = (255, 255, 255)
Blue = (0 , 0, 255)
Red = (255, 0, 0)
Yellow = (255, 255, 0)
Orange = (255, 100, 0)
Green = (0, 255, 0)

# Setting the grid size through width and height of game window
pygame.init()
scr_size = (600, 600)
screen = pygame.display.set_mode(scr_size)

# Loops until the user clicks the close Button
done = False

# Font + background used to create the popup message when level is complete
font = pygame.font.Font(None, 36)
background = pygame.Surface(screen.get_size())

# Fill Screen in black for background
screen.fill(Black)

# Naming the caption of the window opened for the Game
pygame.display.set_caption("Flow")



# Defining grid positions for circles
# Array storing different grid positions possible for circles (their center) for both x and y:
'''
Position in pixels: 
Position 0: 50
position 1: 150
position 2: 250 
position 3: 350 
position 4: 450
position 5: 550
'''
grid = [50, 150, 250, 350, 450, 550]


pygame.init()

'''
Rendering of circles on the screen:
Render method takes 3 arguments: x-coordinate for center, y-coordinate for center, colour (in that order)
This will allow me to change the position of the circles for each level
'''

#Necessary to keep track of what areas are covered with circles
ctr_x_list = []
ctr_y_list = []


circle_list = pygame.sprite.Group()

# Red Circle Pair:
        
RedCircle1 = CircleRender.grid_circle(grid[2], grid[2], Red)
RedCircle2 = CircleRender.grid_circle(grid[4], grid[4], Red)
RedCircle1.render()
RedCircle2.render()
        
# Blue Circle Pair:
        
BlueCircle1 = CircleRender.grid_circle(grid[5], grid[4], Blue)
BlueCircle2 = CircleRender.grid_circle(grid[3], grid[5], Blue)
BlueCircle1.render()
BlueCircle2.render()
        
# Green Circle Pair:
        
GreenCircle1 = CircleRender.grid_circle(grid[3], grid[3], Green)
GreenCircle2 = CircleRender.grid_circle(grid[1], grid[4], Green)
GreenCircle1.render()
GreenCircle2.render()
        

# Orange Circle Pair:
        
OrangeCircle1 = CircleRender.grid_circle(grid[5], grid[0], Orange)
OrangeCircle2 = CircleRender.grid_circle(grid[3], grid[4], Orange)
OrangeCircle1.render()
OrangeCircle2.render()
        
# Yellow Circle Pair:
        
YellowCircle1 = CircleRender.grid_circle(grid[1], grid[2], Yellow)
YellowCircle2 = CircleRender.grid_circle(grid[5], grid[3], Yellow)
YellowCircle1.render()
YellowCircle2.render()


# Sprite list with all the circles
circle_list.add(RedCircle1, RedCircle2, BlueCircle1, BlueCircle2, GreenCircle1, GreenCircle2, OrangeCircle1, OrangeCircle2, YellowCircle1, YellowCircle2)



# Grid built here:
Grid.build_grid()

line_colour = ()

# Used to evaluate the colour where the user clicks
clicked_colour = () 
#Proceed dictates whether the line will be drawn at the next centre of box (100x100)

proceed = ()

#Condition variable for checking if circle is being clicked
clicked = False

# Used to determine which circle is being clicked in other modules:
circle = ()

global ctr_coordinates
ctr_coordinates = []
coordinates = []

# Used for drawing lines when user clicks:
grid_position = ()
draw_ctr = ()

# def click_movement(x, y):

def click_movement(x, y):
    global coordinates
    mouse_pos = (x,y)
    coordinates.append(mouse_pos)
    #aalines(Surface, color, closed, pointlist, blend=1) 
    if len(coordinates) == 2:
        #pygame.draw.lines(screen, line_colour, True, [(coordinates[0]), (coordinates[1])], 30))
        #pygame.draw.aalines(screen, line_colour, False, [(coordinates[0]),(coordinates[1])], True)
        #coordinates = []
        #pygame.draw.aalines(screen, line_colour, False, [(coordinates[0]), (coordinates[1])], True)
        #pygame.draw.aalines(screen, line_colour, False, [(value1),(value2)], True)
        pygame.draw.aalines(screen, line_colour, False, [(coordinates[0]), (coordinates[1])], True)
        coordinates = []

# Condition variables for clicks
Orange1Clicked = False
Orange2Clicked = False
Red1Clicked = False
Red2Clicked = False
Yellow1Clicked = False
Yellow2Clicked = False
Green1Clicked = False
Green2Clicked = False
Blue1Clicked = False
Blue2Clicked = False

# Condition variables for links
OrangeLink = False
RedLink = False
YellowLink = False
GreenLink = False
BlueLink = False


''' *** IN PROGRESS *** '''
'''def program_loop():
    global done
    global Orange1Clicked
    global Orange2Clicked 
    global Red1Clicked
    global Red2Clicked
    global Yellow1Clicked
    global Yellow2Clicked
    global Green1Clicked
    global Green2Clicked
    global Blue1Clicked
    global Blue2Clicked
    global OrangeLink
    global RedLink
    global YellowLink
    global GreenLink
    global BlueLink'''
    
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # Closes the game and exits the loop
                
                #carry this on to check condition to be checked later for allowing to mouse to draw anywhere.
                    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            CheckPos.check()
            CheckPosition.pst()
            Connection.clicked()
                
    
    
        elif event.type == pygame.MOUSEMOTION:
            state = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
                    
            if state[0] == 1:
                #CheckPos.check() # Gets the line colour by checking the position of where the user clicks
                GridPosition.pst()
                click_movement(mouse_x, mouse_y)
                CheckPosition.pst()
                Connection.isConnected()
                #Connection.clicked()
    
            
    
                        
                                    
        if ((OrangeLink == True) and (RedLink == True) and (YellowLink == True) and (GreenLink == True) and (BlueLink == True)):
            # This will determine what will happen when the level is completed:
            # At this point a message comes up saying level complete after all have been linked
            text = font.render("Level Complete", True, White)
            textpos = text.get_rect(centerx=background.get_width()/2)
            textpos.top = 300
            screen.blit(text, textpos)
            #pygame.quit()
                        
                
                                    
        # Update screen with changes
        pygame.display.flip()
            
#program_loop()
    
# Quit game
pygame.quit()