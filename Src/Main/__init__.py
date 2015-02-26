'''Include:
- Crash function, what happens without colour?
- Counter for resets
- Countdown
- Tidy up functions

'''
# Defining colours for the circles, paths(lines) and grid background

import pygame
import pygame.font
import pygame.gfxdraw
import time

from Main import Grid, CircleRender, CircleMovement, GridPosition, Connection, CheckPosition
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



# Setting the grid size through width and height of game window
pygame.init()
display_width = 600
display_height = 800
scr_size = (600, 800)
screen = pygame.display.set_mode(scr_size)

# Loops until the user clicks the close Button
done = False

# Font + background used to create the popup message when level is complete
font = pygame.font.Font(None, 100)
background = pygame.Surface(screen.get_size())

# Defining grid positions for circles
# Array storing different grid positions possible for circles (their center) for both x and y:

pos = pygame.mouse.get_pos()
mouse_x = pos[0]
mouse_y = pos[1]

nresets = 3

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

# Used to check whether box is already in use (coloured in)
interference_list = []

# Used for drawing lines when user clicks:
grid_position = ()
draw_ctr = ()




def click_movement(x, y):
    global coordinates
    mouse_pos = (x,y)
    coordinates.append(mouse_pos)
    if len(coordinates) == 2:
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

def message_display(text):
    largeText = pygame.font.Font('freensansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_level1()

def crash():
    message_display("You Crashed")

def text(text, text_x, text_y, size):
    TextFont = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, TextFont)
    TextRect.center = ((text_x),(text_y))
    screen.blit(TextSurf, TextRect)

def text_objects(text, font):
    textSurface = font.render(text, True, Black)
    return textSurface, textSurface.get_rect() 

def button(msg, button_x, button_y, button_w, button_h, icolour, acolour, fontsize, action= None):
    global nresets
    # ( icolour = inactive colour & acolour = active colour) ( Width is 200) (height 100)
    
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    click = pygame.mouse.get_pressed()
    
    
    #Buttons:
    if button_x+button_w > mouse_x > button_x and button_y+button_h > mouse_y > button_y:
        pygame.draw.rect(screen, acolour, (button_x,button_y,button_w,button_h))
        if click[0] == 1 and action!= None:
            if action == "play":
                game_level1()
            
            elif action == "instructions":
                instruction_menu()
                
            elif action == "quit":
                pygame.quit()
                quit()
                
            elif action == "main menu":
                game_intro()
                
            elif action == "reset":
                if nresets == -1:
                    reset_font = pygame.font.SysFont(None, 25)
                    reset_text = reset_font.render("No more resets available", True, Red)
                    screen.blit(reset_text,(5,625))
                else:
                    line_colour = ()
                    game_level1()
                    
            elif action == "next level from level 1":
                game_level2()
                
            elif action == "none":
                pass
                
                
    else:
        pygame.draw.rect(screen, icolour, (button_x,button_y,button_w,button_h))
    
    smallText = pygame.font.Font("freesansbold.ttf", fontsize)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((button_x+(button_w/2),(button_y+(100/2))))
    screen.blit(textSurf, textRect)
  


                
                
                
def reset_counter(nresets):
    if nresets >= 0:
        reset_font = pygame.font.SysFont(None, 25)
        reset_text = reset_font.render("Resets available: "+str(nresets), True, White)
        screen.blit(reset_text,(5,605))
    else:
        reset_font = pygame.font.SysFont(None, 25)
        reset_text = reset_font.render("Resets available: "+str(0), True, White)
        screen.blit(reset_text,(5,605))
        
        
'''def level_complete():
    pygame.display.set_caption("Level Complete!")
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(Black)
        # This will determine what will happen when the level is completed:
        # At this point a message comes up saying level complete after all have been linked
        text = font.render("Level Complete", True, White)
        textpos = text.get_rect(centerx=background.get_width()/2)
        textpos.top = 250
        screen.blit(text, textpos)
        button("Next level",300,400, 150, 100, DarkGreen, Green, 30, "next level from level 1")
        
        pygame.display.update()'''
            
def instruction_menu():
    pygame.display.set_caption("Flow Instructions")
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        screen.fill(Grey)
        text("Instructions", 300, 100, 70)
        text("The objective of flow is to connect all the circle pairs together of the same colour:",300,200,15)
        text("1. Click a circle to choose that colour", 300, 300, 15)
        text("2. Click and drag from chosen circle to colour partner to complete link", 300, 350, 15)
        text("3. Try to complete the links before the timer runs out",300,400, 15)
        text("4. You can only reset the level a maximum of 3 times",300, 450, 15)
        text("5. Enjoy yourself!", 300,500, 15)
        
        button("Play", 50,600,200,100, DarkGreen, Green,30, "play")
        button("Quit",350,600,200,100, DarkRed, Red,30, "quit")
        
        pygame.display.update()

def game_intro():
    display_width = 600
    display_height = 600
    pygame.display.set_caption("Flow Main Menu")
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
        screen.fill(Yellow)
        largeText = pygame.font.Font('freesansbold.ttf', 150)
        TextSurf, TextRect = text_objects("Flow", largeText)
        TextRect.center = ((display_width/2),(display_height*0.25))
        screen.blit(TextSurf, TextRect)
        
        button("Play", 200,300,200,100, DarkGreen, Green,30, "play")
        button("Instructions",200,450,200,100, DarkBlue, Blue, 30, "instructions")
        button("Quit",200,600,200,100, DarkRed, Red, 30, "quit")
        
        
        pygame.display.update()
        


# First level:        
     
def game_level1():
    global Orange1Clicked, Orange2Clicked
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
    # Naming the caption of the window opened for the Game
    pygame.display.set_caption("Flow level 1")
    
    # Fill Screen in black for background
    screen.fill(Black)
    
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

    reset_counter(nresets)
    
    line_colour = ()
    print(line_colour)
    
    global ctr_coordinates
    ctr_coordinates = []
    coordinates = []

    
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
                GridPosition.no_linecolour_crash()
                Line.linecolour(5, 0, 3, 4, 2, 2, 4, 4, 1, 2, 5, 3, 3, 3, 1, 4, 5, 4, 3, 5)
                CheckPosition.pst()
                Connection.clicked(6,28,15,29,14,24,22,26,30,34)
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
                    Connection.isConnected(6,28,15,29,14,24,22,26,30,34)
                            
            if ((OrangeLink == True) and (RedLink == True) and (YellowLink == True) and (GreenLink == True) and (BlueLink == True)):
                button("",20,170, 560, 150, Lightblue, Lightblue, 30, "none")
                button("",20,380, 560, 150, Lightblue, Lightblue, 30, "none")
                # This will determine what will happen when the level is completed:
                # At this point a message comes up saying level complete after all have been linked
                text = font.render("Level Complete", True, Black)
                textpos = text.get_rect(centerx=background.get_width()/2)
                textpos.top = 210
                screen.blit(text, textpos)
                button("Next level",50,400, 200, 100, DarkGreen, Green, 30, "next level from level 1")
                button("Quit game",350,400, 200, 100, DarkGrey, Grey, 30, "quit")
                #pygame.quit()'''
        
              
        button("Reset Paths", 25,650,150,100, DarkBlue, Blue, 20, "reset")                  
        button("Main menu", 225,650,150,100, DarkGreen, Green, 20, "main menu")
        button("Quit game", 425,650,150,100, DarkRed, Red, 20, "quit")                       
        # Update screen with changes
        pygame.display.flip()
        
        
def game_level2():
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

    # Naming the caption of the window opened for the Game
    pygame.display.set_caption("Flow level 2")
    
    # Fill Screen in black for background
    screen.fill(Black)
    
    circle_list = pygame.sprite.Group()

    # Red Circle Pair:
            
    RedCircle1 = CircleRender.grid_circle(grid[0], grid[1], Red)
    RedCircle2 = CircleRender.grid_circle(grid[5], grid[3], Red)
    RedCircle1.render()
    RedCircle2.render()
        
    # Blue Circle Pair:
            
    BlueCircle1 = CircleRender.grid_circle(grid[1], grid[1], Blue)
    BlueCircle2 = CircleRender.grid_circle(grid[5], grid[4], Blue)
    BlueCircle1.render()
    BlueCircle2.render()
            
    # Green Circle Pair:
            
    GreenCircle1 = CircleRender.grid_circle(grid[3], grid[1], Green)
    GreenCircle2 = CircleRender.grid_circle(grid[4], grid[4], Green)
    GreenCircle1.render()
    GreenCircle2.render()
            
    
    # Orange Circle Pair:
            
    OrangeCircle1 = CircleRender.grid_circle(grid[1], grid[3], Orange)
    OrangeCircle2 = CircleRender.grid_circle(grid[0], grid[5], Orange)
    OrangeCircle1.render()
    OrangeCircle2.render()
            
    # Yellow Circle Pair:
            
    YellowCircle1 = CircleRender.grid_circle(grid[1], grid[2], Yellow)
    YellowCircle2 = CircleRender.grid_circle(grid[1], grid[4], Yellow)
    YellowCircle1.render()
    YellowCircle2.render()
    
    
    # Sprite list with all the circles
    circle_list.add(RedCircle1, RedCircle2, BlueCircle1, BlueCircle2, GreenCircle1, GreenCircle2, OrangeCircle1, OrangeCircle2, YellowCircle1, YellowCircle2)
    
    
    # Grid built here:
    Grid.build_grid()

    reset_counter(nresets)
    
    line_colour = ()

    
    global ctr_coordinates
    ctr_coordinates = []
    coordinates = []

    
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
                Line.linecolour(1, 3, 0, 5, 0, 1, 5, 3, 1, 2, 1, 4, 3, 1, 4, 4, 1, 1, 5, 4)
                CheckPosition.pst()
                Connection.clicked(20,31,7,24,14,26,10,29,8,30)
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
                    Connection.isConnected(20,31,7,24,14,26,10,29,8,30)
                            
            if ((OrangeLink == True) and (RedLink == True) and (YellowLink == True) and (GreenLink == True) and (BlueLink == True)):
                button("",20,170, 560, 150, Lightblue, Lightblue, 30, "none")
                button("",20,380, 560, 150, Lightblue, Lightblue, 30, "none")
                # This will determine what will happen when the level is completed:
                # At this point a message comes up saying level complete after all have been linked
                text = font.render("Level Complete", True, Black)
                textpos = text.get_rect(centerx=background.get_width()/2)
                textpos.top = 210
                screen.blit(text, textpos)
                button("Next level",50,400, 200, 100, DarkGreen, Green, 30, "next level from level 1")
                button("Quit game",350,400, 200, 100, DarkGrey, Grey, 30, "quit")
                #pygame.quit()'''
        
              
        button("Reset Paths", 25,650,150,100, DarkBlue, Blue, 20, "reset")                  
        button("Main menu", 225,650,150,100, DarkGreen, Green, 20, "main menu")
        button("Quit game", 425,650,150,100, DarkRed, Red, 20, "quit")                       
        # Update screen with changes
        pygame.display.flip()
        
        
            
game_intro()
    
# Quit game
pygame.quit()