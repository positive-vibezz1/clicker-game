from pygame import *
from pygame import font
from pygame import math
import pygame
import os
import sys
from text import text
from button import Button


font_path = "Montserrat-Medium.ttf"

if getattr(sys, 'frozen', False):
    # If the script is run as a bundled executable
    base_path = sys._MEIPASS
else:
    
    # If the script is run as a regular Python script
    base_path = os.path.abspath(os.path.dirname(__file__))
#where our font is stored locally? idk?
font_path = os.path.join(base_path, font_path)


#click logic
upgrade_logic_1 = 3*4-6
next_upgrade_1 = 10
main_counter = 0
click_worth = 1

#display initiation aswell as fonnt initiation
pygame.display.init()
pygame.font.init()
font1 = pygame.font.Font("Montserrat-Medium.ttf", 36)
font2 = pygame.font.Font("Montserrat-Medium.ttf", 28)

#colours
button_color_pink = (255, 0, 255)
button_color_black = (0, 0, 0)
button_color_white = (255, 255, 255)
button_color_red = (255, 30, 0)

      
#window properties
size = 800, 600
clicker = pygame.display.set_mode((size))
surface = pygame.Surface(size)
pygame.display.set_caption("clicker game")
pygame.display.flip()


# Create the text object
score_display = text((10, 10), "you clicked: ", font1) 
until_next_upgrade = text((500, 200), "next upgrade in: " + str(next_upgrade_1), font2)

# create a button object
main_button = Button((100, 100), (50, 50), button_color_pink, clicker)
upgrade_button_1 = Button((600, 300), (50, 50), button_color_red, clicker)

clock = pygame.time.Clock()
running = True
while True:
    clicker.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        (mousex, mousey) = pygame.mouse.get_pos()
        mousepress = event.type == MOUSEBUTTONDOWN
        
        if main_button.is_clicked((mousex, mousey), mousepress):
            main_counter += click_worth
            score_display.text = "you clicked: " + str(main_counter)

            
        if upgrade_button_1.is_clicked((mousex, mousey), mousepress):
            if main_counter >= next_upgrade_1:
                next_upgrade_1 += upgrade_logic_1      
                click_worth += 1
            until_next_upgrade.text = "next upgrade in: " + str(next_upgrade_1)



        # Draw the text on the screen
        score_display.textrender(clicker)
        until_next_upgrade.textrender(clicker)
        
        #draw the button on the screen
        main_button.button_render()
        upgrade_button_1.button_render()
        
    
        clock.tick(60)    
        pygame.display.flip()
