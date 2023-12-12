from pygame import *
from pygame import font
from pygame import math
import pygame
import os
import sys
from text import text
from button import Button
from recursion import Recursion

font_path = "Montserrat-Medium.ttf"

if getattr(sys, 'frozen', False):
    # If the script is run as a bundled executable
    base_path = sys._MEIPASS
else:
    
    # If the script is run as a regular Python script
    base_path = os.path.abspath(os.path.dirname(__file__))
#where our font is stored locally? idk?
font_path = os.path.join(base_path, font_path)





next_upgrade_1 = 10
next_upgrade_2 = 100

main_counter = 100000000000000000000
click_worth = 1

#passive income
passive_income = 0
#display initiation aswell as fonnt initiation
pygame.display.init()
pygame.font.init()
font1 = pygame.font.Font("Montserrat-Medium.ttf", 36)
font2 = pygame.font.Font("Montserrat-Medium.ttf", 28)

pygame.display.set_icon(pygame.image.load('D:\python projects\clicker pygame\sponge bob.png'))



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
score_display = text((300, 10), "you clicked: ", font1) 
until_next_upgrade_1 = text((600, 150), f"{next_upgrade_1}", font2)
until_next_upgrade_2 = text((600, 350), f"{next_upgrade_2}", font2)

# create a button object
main_button = Button((200, 200), (100, 100), button_color_pink, clicker)
upgrade_button_1 = Button((600, 200), (50, 50), button_color_red, clicker)
upgrade_button_2 = Button((600, 400), (50, 50), button_color_pink, clicker)



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
            print("main_counter:", main_counter)
            print(f"your click worth is {click_worth}")
           
        if upgrade_button_1.is_clicked((mousex, mousey), mousepress):
            upgrade_logic_1_sub_module = 2
            upgrade_logic_1_sub_module += 1
            upgrade_logic_1 = 3 ** upgrade_logic_1_sub_module         
            if main_counter >= next_upgrade_1:
                next_upgrade_1 += upgrade_logic_1
                click_worth += 1                
            until_next_upgrade_1.text = f"{next_upgrade_1}"
            print(f"next_upgrade_1: {next_upgrade_1}")
            print(f"your click worth: {click_worth}")
            print("upgrade_logic_1e:", next_upgrade_1)
            print(f" base  is equal to {upgrade_logic_1_sub_module}")
       
        if upgrade_button_2.is_clicked((mousex, mousey), mousepress):
            upgrade_logic_2 = Recursion(2,2)
            power_result = upgrade_logic_2.recursive_power(next_upgrade_2, upgrade_logic_2.exponent) 
            if main_counter >= next_upgrade_2:
                next_upgrade_2 += power_result  
                click_worth += 2
                print(f"Power Result: {power_result}")
                until_next_upgrade_2.text = f"{next_upgrade_2}"
            print(f"next_upgrade_1: {next_upgrade_2}")
            print(f"your click worth: {click_worth}")
            print("upgrade_logic:", next_upgrade_2)


    # Draw the text on the screen
    score_display.textrender(clicker)
    until_next_upgrade_1.textrender(clicker)
    until_next_upgrade_2.textrender(clicker)
        
        
    #draw the button on the screen
    main_button.button_render()
    upgrade_button_1.button_render()
    upgrade_button_2.button_render()
    
    #click amount display
    click_amoun_display = text((10, 500), "click worth: " + str(click_worth), font2)
    click_amoun_display.textrender(clicker)
    
    passive_income_display = text((10, 550), f"you have: {passive_income} passive income", font2)
    passive_income_display.textrender(clicker)
    
    
    clock.tick(60)    
    pygame.display.flip()
