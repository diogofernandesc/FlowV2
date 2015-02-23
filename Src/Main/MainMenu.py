'''import pygame
import Main

# Screen for Main Menu:
display_width = 600
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Flow Main Menu")

def text_objects(text, font):
    textSurface = font.render(text, True, Main.Black)
    return textSurface, textSurface.get_rect()
    
def game_intro():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(Main.White)
        largeText = pygame.font.Font('freensansbold.ttf',115)
        TextSurf, TextRect = text_objects("FLOW", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()'''
        
        
import pygame
import time
import Main

pygame.init()

display_width = 600
display_height = 600


gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Flow Main Menu")
clock = pygame.time.Clock()

def crash():
    message_display("You Crashed")

def text_objects(text, font):
    textSurface = font.render(text, True, Main.Black)
    return textSurface, textSurface.get_rect() 

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def game_intro():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
        gameDisplay.fill(Main.White)
        largeText = pygame.font.Font('freensansbold.ttf', 115)
        TextSurf, TextRect = text_objects(Flow, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)