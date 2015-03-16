'''Include:

**********************
- Do I allow player to retry from current level or start all over again???
'''
# Defining colours for the circles, paths(lines) and grid background

import pygame
import pygame.time
import pygame.font
import pygame.gfxdraw
import time

from Main import Grid, CircleRender, GridPosition, Connection, CheckPosition
from Main import Line


Black = (0 , 0, 0)
White = (255, 255, 255)
Blue = (0 , 0, 255)
DarkBlue = (0, 0, 180)
Red = (255, 0, 0)
DarkRed = (200,0,0)
Yellow = (255, 255, 0)
DarkYellow = (225, 200, 0)
Orange = (255, 100, 0)
Green = (0, 255, 0)
DarkGreen = (0, 200, 0)
Grey = (122, 122, 122)
Lightblue = (50, 255, 200)
DarkLightblue = (50, 255, 170)
Grey = (150, 150, 150)
DarkGrey = (110, 110, 100)
VeryDarkGrey = (20, 20, 20)




# Setting the grid size through width and height of game window:

# Initialize pygame imported modules
pygame.init()

display_width = 600
display_height = 800
scr_size = (display_width, display_height)
screen = pygame.display.set_mode(scr_size)

clock = pygame.time.Clock()

# Loops until the user clicks the close Button
done = False

# Font + background used to create the popup message when level is complete
font = pygame.font.Font(None, 100)
background = pygame.Surface(screen.get_size())


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

# Used to evaluate whether circles have been connected in the Connection module
grid_position = ()

# List which can be appended to for the centre of the circles which will have to be drawn
coordinates = []


# Amount of resets available to player
nresets = 3


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


def text(text, text_x, text_y, size):
    TextFont = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, TextFont)
    TextRect.center = ((text_x),(text_y))
    screen.blit(TextSurf, TextRect)

def text_objects(text, font):
    textSurface = font.render(text, True, Black)
    return textSurface, textSurface.get_rect() 

def button(msg, button_x, button_y, button_w, button_h, icolour, acolour, fontsize, action= None): # icolour = inactive colour & acolour = active colour
    global nresets
    global current_level

    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    click = pygame.mouse.get_pressed()
    
    
    #Buttons:
    if button_x+button_w > mouse_x > button_x and button_y+button_h > mouse_y > button_y:
        pygame.draw.rect(screen, acolour, (button_x,button_y,button_w,button_h))
        if click[0] == 1 and action!= None:
            if action == "level 1":
                game_level("level 1", "level 2", "reset_level1", 2, 2, 4, 4, 5, 4, 3, 5, 3, 3, 1, 4, 5, 0, 3, 4, 1, 2, 5, 3, 5, 0, 3, 4, 2, 2, 4, 4, 1, 2, 5, 3, 3, 3, 1, 4, 5, 4, 3, 5, 6, 28, 15, 29, 14, 24, 22, 26, 30, 34)
            
            elif action == "instructions":
                instruction_menu()
                
            elif action == "quit":
                pygame.quit()
                quit()
                
            elif action == "main menu":
                game_intro()
                
            elif action == "reset_level1":
                if nresets == -1:
                    reset_font = pygame.font.SysFont(None, 25)
                    reset_text = reset_font.render("No more resets available", True, Red)
                    screen.blit(reset_text,(5,625))
                else:
                    game_level("level 1", "level 2", "reset_level1", 2, 2, 4, 4, 5, 4, 3, 5, 3, 3, 1, 4, 5, 0, 3, 4, 1, 2, 5, 3, 5, 0, 3, 4, 2, 2, 4, 4, 1, 2, 5, 3, 3, 3, 1, 4, 5, 4, 3, 5, 6, 28, 15, 29, 14, 24, 22, 26, 30, 34)

                    
            elif action == "reset_level2":
                if nresets == -1:
                    reset_font = pygame.font.SysFont(None, 25)
                    reset_text = reset_font.render("No more resets available", True, Red)
                    screen.blit(reset_text,(5,625))
                else:
                    game_level("level 2", "level 3", "reset_level2", 0, 1, 5, 3, 1, 1, 5, 4, 3, 1, 4, 4, 1, 3, 0, 5, 1, 2, 1, 4, 1, 3, 0, 5, 0, 1, 5, 3, 1, 2, 1, 4, 3, 1, 4, 4, 1, 1, 5, 4, 20, 31, 7, 24, 14, 26, 10, 29, 8, 30)
            
            elif action == "reset_level3":
                if nresets == -1:
                    reset_font = pygame.font.SysFont(None, 25)
                    reset_text = reset_font.render("No more resets available", True, Red)
                    screen.blit(reset_text,(5,625))
                else:
                    game_level("level 3", "level 4", "reset_level3", 4, 1, 4, 4, 4, 2, 4, 5, 5, 1, 3, 5, 0, 0, 1, 4, 0, 1, 2, 5, 0, 0, 1, 4, 4, 1, 4, 4, 0, 1, 1, 4, 5, 1, 3, 5, 4, 2, 4, 5, 1, 26, 11, 29, 7, 33, 12, 34, 17, 35)
                    
            elif action == "reset_level4":
                if nresets == -1:
                    reset_font = pygame.font.SysFont(None, 25)
                    reset_text = reset_font.render("No more resets available", True, Red)
                    screen.blit(reset_text,(5,625))
                else:
                    game_level("level 4", "level 5", "reset_level4", 5, 0, 0, 4, 0, 0, 3, 4, 1, 2, 2, 3, 0, 2, 2, 4, 0, 1, 3, 3, 0, 2, 2, 4, 5, 0, 0, 4, 0, 1, 3, 3, 1, 2, 2, 3, 0, 0, 3, 4, 13, 27, 6, 25, 7, 22, 14, 21, 1, 28)

            elif action == "reset_level5":
                if nresets == -1:
                    reset_font = pygame.font.SysFont(None, 25)
                    reset_text = reset_font.render("No more resets available", True, Red)
                    screen.blit(reset_text,(5,625))
                else:
                    game_level("level 5", "game complete", "reset_level5", 1, 2, 3, 2, 2, 4, 4, 4, 1, 1, 2, 5, 5, 0, 0, 5, 5, 1, 3, 5, 5, 0, 0, 5, 1, 2, 3, 2, 5, 1, 3, 5, 1, 1, 2, 5, 2, 4, 4, 4, 6, 31, 14, 16, 12, 34, 8, 33, 27, 29)

                
            elif action == "level 2":
                game_level("level 2", "level 3", "reset_level2", 0, 1, 5, 3, 1, 1, 5, 4, 3, 1, 4, 4, 1, 3, 0, 5, 1, 2, 1, 4, 1, 3, 0, 5, 0, 1, 5, 3, 1, 2, 1, 4, 3, 1, 4, 4, 1, 1, 5, 4, 20, 31, 7, 24, 14, 26, 10, 29, 8, 30)

            elif action == "level 3":
                game_level("level 3", "level 4", "reset_level3", 4, 1, 4, 4, 4, 2, 4, 5, 5, 1, 3, 5, 0, 0, 1, 4, 0, 1, 2, 5, 0, 0, 1, 4, 4, 1, 4, 4, 0, 1, 1, 4, 5, 1, 3, 5, 4, 2, 4, 5, 1, 26, 11, 29, 7, 33, 12, 34, 17, 35)
    
            elif action == "level 4":
                game_level("level 4", "level 5", "reset_level4", 5, 0, 0, 4, 0, 0, 3, 4, 1, 2, 2, 3, 0, 2, 2, 4, 0, 1, 3, 3, 0, 2, 2, 4, 5, 0, 0, 4, 0, 1, 3, 3, 1, 2, 2, 3, 0, 0, 3, 4, 13, 27, 6, 25, 7, 22, 14, 21, 1, 28)
            
            elif action == "level 5":
                game_level("level 5", "game complete", "reset_level5", 1, 2, 3, 2, 2, 4, 4, 4, 1, 1, 2, 5, 5, 0, 0, 5, 5, 1, 3, 5, 5, 0, 0, 5, 1, 2, 3, 2, 5, 1, 3, 5, 1, 1, 2, 5, 2, 4, 4, 4, 6, 31, 14, 16, 12, 34, 8, 33, 27, 29)

            elif action == "game complete":
                level_finished("game complete", action, current_level)
                pygame.display.update()
                time.sleep(1)
            
            elif action == "none":
                pass
                
                
    else:
        pygame.draw.rect(screen, icolour, (button_x,button_y,button_w,button_h))
    
    smallText = pygame.font.Font("freesansbold.ttf", fontsize)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((button_x+(button_w/2),(button_y+(100/2))))
    screen.blit(textSurf, textRect)



def level_finished(situation, nextlevel, current_level):
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Closes the game and exits the loop
        
        button("",20,170, 560, 150, Lightblue, Lightblue, 30, "none")
        button("",20,380, 560, 150, Lightblue, Lightblue, 30, "none")
        
        if situation == "level complete":
            # This will determine what will happen when the level is completed:
            # At this point a message comes up saying level complete after all have been linked
            text = font.render("Level Complete", True, Black)
            textpos = text.get_rect(centerx=background.get_width()/2)
            textpos.top = 210
            screen.blit(text, textpos)
            button("Next level",50,400, 200, 100, DarkGreen, Green, 30, nextlevel)
            button("Quit game",350,400, 200, 100, DarkGrey, Grey, 30, "quit")
            
        elif situation == "out of time":
            text = font.render("Out of time!", True, Black)
            textpos = text.get_rect(centerx=background.get_width()/2)
            textpos.top = 210
            screen.blit(text, textpos)
            # Making the retry button start the game over from level 1
            button("Retry",50,400, 200, 100, DarkGreen, Green, 30, "level 1")
            button("Quit game",350,400, 200, 100, DarkGrey, Grey, 30, "quit")
            
            
        elif situation == "game complete":
            text = font.render("Game Complete!", True, Black)
            textpos = text.get_rect(centerx=background.get_width()/2)
            textpos.top = 210
            screen.blit(text, textpos)
            button("Main Menu",50,400, 200, 100, DarkGreen, Green, 30, "main menu")
            button("Quit game",350,400, 200, 100, DarkGrey, Grey, 30, "quit")
            
        pygame.display.flip()

def timer(situation, nextlevel, current_level):
    
    '''
    At each frame seconds tick down at the same rate that a second ticks down
    '''
    
    global frame_count
    global frame_rate
    global level_time
    
    timer_font = pygame.font.SysFont(None, 25)
    
     
    total_seconds = level_time - (frame_count // frame_rate)
    
    if total_seconds < 0:
        # Statements executed when time runs out:
        total_seconds = 0
        level_finished(situation, nextlevel, current_level)
        
    else:
        # Need this to create a black background over the blitted text as to not overlap
        button("", 210, 605, 135, 20, Black, Black, 10, "none") 
        # Divide by 60 to get total minutes
        minutes = total_seconds // 60
         
        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60
         
        # Use python string formatting to format in leading zeros
        time_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
         
        # Blit to the screen
        time_text = timer_font.render(str(time_string), True, White)
        screen.blit(time_text, (210,605))
    
        # Controls the rate of change of frames 
        frame_count += 1
        
        # Control the second change of the timer to be equal to a second
        clock.tick(frame_rate)
    

                                
def reset_counter(nresets):
    '''
    Using variable nresets, blits the value of nresets each time it changes
    I had to have a condition for zero nresets otherwise the counter would not blit the last reset available as 0
    '''
    if nresets >= 0:
        reset_font = pygame.font.SysFont(None, 25)
        reset_text = reset_font.render("Resets available: "+str(nresets), True, White)
        screen.blit(reset_text,(5,605))
    else:
        reset_font = pygame.font.SysFont(None, 25)
        reset_text = reset_font.render("Resets available: "+str(0), True, White)
        screen.blit(reset_text,(5,605))
        
        
def instruction_menu():
    pygame.display.set_caption("Flow Instructions")
    instrMenu = True
    while instrMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        screen.fill(Yellow)
        text("Instructions", 300, 100, 70)
        text("The objective of flow is to connect all the circle pairs of the same colour, together:",300,200,15)
        text("- Click one of the circles to begin", 300, 250, 15)
        text("- Hold down the left mouse button and drag to its colour partner to complete the link", 300, 300, 15)
        text("- Once a link is complete, the link colour will light up at the bottom of the screen", 300, 350, 15)
        text("- You have 15 seconds to complete the level", 300, 400, 15)
        text("- You have three resets available to you, which also reset the time!", 300, 450, 15)
        text("- If you run out of time, you start all over again! Enjoy yourself!", 300,500, 15)
        
        button("Play", 50,600,200,100, DarkGreen, Green,30, "level 1")
        button("Quit",350,600,200,100, DarkRed, Red,30, "quit")
        
        pygame.display.update()


def game_intro():
    pygame.display.set_caption("Flow Main Menu")
    Gintro = True
    
    while Gintro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
        screen.fill(Yellow)
        largeText = pygame.font.Font('freesansbold.ttf', 150)
        TextSurf, TextRect = text_objects("Flow", largeText)
        TextRect.center = ((display_width/2),(display_height*0.25))
        screen.blit(TextSurf, TextRect)
        
        button("Play", 200,300,200,100, DarkGreen, Green,30, "level 1")
        button("Instructions",200,450,200,100, DarkBlue, Blue, 30, "instructions")
        button("Quit",200,600,200,100, DarkRed, Red, 30, "quit")
        
        
        pygame.display.update()
        

def game_level(current_level, action, rAction, R1x, R1y, R2x, R2y, B1x, B1y, B2x, B2y, G1x, G1y, G2x, G2y, O1x, O1y, O2x, O2y, Y1x, Y1y, Y2x, Y2y, o_x1, o_y1, o_x2, o_y2, r_x1, r_y1, r_x2, r_y2, yel_x1, yel_y1, yel_x2, yel_y2, g_x1, g_y1, g_x2, g_y2, b_x1, b_y1, b_x2, b_y2, orangegp1, orangegp2, redgp1, redgp2, yellowgp1, yellowgp2, greengp1, greengp2, bluegp1, bluegp2):
    '''
     Arguments: Big letters (R, B, G, Y, O) represent stationary circles, small letters (o, r, g, y, b) used to check connections complete or if clicked
     Arguments: action to say what happens after level complete, and rAction for action for the reset button
    '''
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
    global BlueLink
    global mouse_x
    global mouse_y
    global nresets
    global line_colour
    global frame_count
    global frame_rate
    global level_time
    
    # Naming the caption of the window opened for the Game
    pygame.display.set_caption("Flow " + current_level)
    
    
    frame_count = 0
    frame_rate = 60

    # Time for each level:
    level_time = 15
    
    # Fill Screen in black for background
    screen.fill(Black)
    
    circle_list = pygame.sprite.Group()

    # Red Circle Pair:
            
    RedCircle1 = CircleRender.grid_circle(grid[R1x], grid[R1y], Red)
    RedCircle2 = CircleRender.grid_circle(grid[R2x], grid[R2y], Red)
    RedCircle1.render()
    RedCircle2.render()
        
    # Blue Circle Pair:
            
    BlueCircle1 = CircleRender.grid_circle(grid[B1x], grid[B1y], Blue)
    BlueCircle2 = CircleRender.grid_circle(grid[B2x], grid[B2y], Blue)
    BlueCircle1.render()
    BlueCircle2.render()
            
    # Green Circle Pair:
            
    GreenCircle1 = CircleRender.grid_circle(grid[G1x], grid[G1y], Green)
    GreenCircle2 = CircleRender.grid_circle(grid[G2x], grid[G2y], Green)
    GreenCircle1.render()
    GreenCircle2.render()
            
    
    # Orange Circle Pair:
            
    OrangeCircle1 = CircleRender.grid_circle(grid[O1x], grid[O1y], Orange)
    OrangeCircle2 = CircleRender.grid_circle(grid[O2x], grid[O2y], Orange)
    OrangeCircle1.render()
    OrangeCircle2.render()
            
    # Yellow Circle Pair:
            
    YellowCircle1 = CircleRender.grid_circle(grid[Y1x], grid[Y1y], Yellow)
    YellowCircle2 = CircleRender.grid_circle(grid[Y2x], grid[Y2y], Yellow)
    YellowCircle1.render()
    YellowCircle2.render()
    
    
    # Sprite list with all the circles
    circle_list.add(RedCircle1, RedCircle2, BlueCircle1, BlueCircle2, GreenCircle1, GreenCircle2, OrangeCircle1, OrangeCircle2, YellowCircle1, YellowCircle2)
    
    
    # Grid built here:
    Grid.build_grid()

    reset_counter(nresets)
    Connection.complete_status()
    
    line_colour = ()
    
    
    # Condition variables for links
    OrangeLink = False
    RedLink = False
    YellowLink = False
    GreenLink = False
    BlueLink = False
    
    Red1Clicked = False
    Red2Clicked = False
    Orange1Clicked = False
    Orange2Clicked = False
    Yellow1Clicked = False
    Yellow2Clicked = False
    Green1Clicked = False
    Green2Clicked = False
    Blue1Clicked = False
    Blue2Clicked = False
    
    
    done = False
    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Closes the game and exits the loop
                    
                    #carry this on to check condition to be checked later for allowing to mouse to draw anywhere.
                        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # This stops program from crashing if user clicks anywhere but not the actual circle because line_colour would have no value
                GridPosition.no_linecolour_crash()
                Line.linecolour(o_x1, o_y1, o_x2, o_y2, r_x1, r_y1, r_x2, r_y2, yel_x1, yel_y1, yel_x2, yel_y2, g_x1, g_y1, g_x2, g_y2, b_x1, b_y1, b_x2, b_y2)
                CheckPosition.pst()
                Connection.clicked(orangegp1, orangegp2, redgp1, redgp2, yellowgp1, yellowgp2, greengp1, greengp2, bluegp1, bluegp2)
                # Checks whether user clicks the reset button:
                if 50+200 > mouse_x > 50 and 650+100 > mouse_y > 650:
                    if nresets == -1:
                        reset_counter(nresets)
                        
                    else:
                        nresets = nresets - 1
                        reset_counter(nresets)
                
            elif event.type == pygame.MOUSEMOTION:
                state = pygame.mouse.get_pressed()
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1]
                        
                if state[0] == 1:
                    #Line.check() # Gets the line colour by checking the position of where the user clicks
                    GridPosition.pst()
                    #click_movement(mouse_x, mouse_y)
                    CheckPosition.pst()
                    # checks whether
                    Connection.isConnected(orangegp1, orangegp2, redgp1, redgp2, yellowgp1, yellowgp2, greengp1, greengp2, bluegp1, bluegp2)
                            
            if ((OrangeLink == True) and (RedLink == True) and (YellowLink == True) and (GreenLink == True) and (BlueLink == True)):
                # Wait for 1 second because there seems to be a problem whereby if the user is still holding the mouse the program will continue evaluating in other circumstances, explained in project:
                time.sleep(1)
                if current_level == "level 5":
                    # Bring up game complete window if the 5th level is complete:
                    level_finished("game complete", action, current_level)
                    
                else:
                    # Bring up level complete screen if the current level is complete
                    level_finished("level complete", action, current_level)
                    
                    
                
                
         
        # Countdown timer: 
        timer("out of time", action, current_level)
        button("Reset Paths", 25,640,150,100, DarkBlue, Blue, 20, rAction)                  
        button("Main menu", 225,640,150,100, DarkGreen, Green, 20, "main menu")
        button("Quit game", 425,640,150,100, DarkRed, Red, 20, "quit")                       
        # Update screen with changes
        pygame.display.flip()



game_intro()
    
# Quit game
pygame.quit()