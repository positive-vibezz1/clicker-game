import pygame
from pygame import *
from pygame import time
from pygame import math
from pygame import font
import sys
from text import text
from button import Button
from recursion import Recursion
from passive_income import Passiveincome

button_size_changed = False

upgrade_logic_1_sub_module = 2
upgrade_logic_2 = Recursion(2,2)
upgrade_logic_3 = 2 * 5 + 3


next_upgrade_1 = 10
next_upgrade_2 = 100
next_upgrade_3 = 500

main_counter = 1000000000000
click_worth = 1

#passive income
input_passive_income = Passiveincome(0)


#display initiation aswell as fonnt initiation
pygame.display.init()
pygame.font.init()
font1 = pygame.font.SysFont("Arial", 36)
font2 = pygame.font.SysFont("Arial", 28)


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
until_next_upgrade_2 = text((600, 300), f"{next_upgrade_2}", font2)
until_passive_income_upgrade_1 = text((600, 450), f"{next_upgrade_3}", font2) 

# create a button object
main_button = Button((200, 200), (100, 100), button_color_pink, clicker)
upgrade_button_1 = Button((600, 200), (50, 50), button_color_red, clicker)
upgrade_button_2 = Button((600, 350), (50, 50), button_color_pink, clicker)
passive_income_button_1 = Button((600, 500), (50, 50), button_color_pink, clicker)

PASSIVEVENT = USEREVENT + 1
pygame.time.set_timer(PASSIVEVENT,1000)

clock = pygame.time.Clock()

running = True
while True:
    clicker.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == PASSIVEVENT:
            main_counter += input_passive_income
            print(f"main counter is {main_counter}")
        (mousex, mousey) = pygame.mouse.get_pos()
        mousepressdown = event.type == MOUSEBUTTONDOWN
        mousepressup = event.type == MOUSEBUTTONUP
        
        if main_button.is_clicked((mousex, mousey), mousepressdown):

            main_counter += click_worth
            score_display.text = "you clicked: " + str(main_counter)
            print("main_counter:", main_counter)
            print(f"your click worth is {click_worth}")
          
        if upgrade_button_1.is_clicked((mousex, mousey), mousepressdown):                     
            if main_counter >= next_upgrade_1:
                main_counter -= next_upgrade_1     
                upgrade_logic_1_sub_module += 1
                upgrade_logic_1 = 3 ** upgrade_logic_1_sub_module   
                next_upgrade_1 += upgrade_logic_1
                click_worth += 1               
            until_next_upgrade_1.text = f"{next_upgrade_1}"
            print(f"next_upgrade_1: {next_upgrade_1}")
            print(f"your click worth: {click_worth}")
            print("upgrade_logic_1e:", next_upgrade_1)
            print(f" base  is equal to {upgrade_logic_1_sub_module}")
       
        if upgrade_button_2.is_clicked((mousex, mousey), mousepressdown):            
            power_result = upgrade_logic_2.recursive_power(next_upgrade_2, upgrade_logic_2.exponent) 
            if main_counter >= next_upgrade_2:
                main_counter -= next_upgrade_2
                next_upgrade_2 += power_result  
                click_worth += 5
            until_next_upgrade_2.text = f"{next_upgrade_2}"
            print(f"next_upgrade_2: {next_upgrade_2}")
            print(f"your click worth: {click_worth}")
            print("upgrade_logic:", next_upgrade_2)

        if passive_income_button_1.is_clicked((mousex, mousey), mousepressdown):
            if main_counter >= next_upgrade_3:
                input_passive_income += 1
                next_upgrade_3 += 3 * 5 + 3 - 1 - 5 + 10
            until_passive_income_upgrade_1.text = f"{next_upgrade_3}"
            print(f"next_upgrade_3: {next_upgrade_3}")
            print(f"your click worth: {click_worth}")
            print(f"your passive income is {input_passive_income}")
               
        def animationhandler():   
            if main_button.is_clicked((mousex, mousey), mousepressdown):
                main_button.set_size((90, 90))
            if main_button.is_clicked((mousex, mousey), mousepressup):       
                main_button.set_size((100, 100))
            if upgrade_button_1.is_clicked((mousex, mousey), mousepressdown):
                upgrade_button_1.set_size((45, 45))
            if upgrade_button_1.is_clicked((mousex, mousey), mousepressup):
                upgrade_button_1.set_size((50, 50))
            if upgrade_button_2.is_clicked((mousex, mousey), mousepressdown):
                upgrade_button_2.set_size((45, 45))
            if upgrade_button_2.is_clicked((mousex, mousey), mousepressup):
                upgrade_button_2.set_size((50, 50))
            if passive_income_button_1.is_clicked((mousex, mousey), mousepressdown):
                passive_income_button_1.set_size((45, 45))
            if passive_income_button_1.is_clicked((mousex, mousey), mousepressup):
                passive_income_button_1.set_size((50, 50))

               
    # Draw the text on the screen
    score_display.textrender(clicker)
    until_next_upgrade_1.textrender(clicker)
    until_next_upgrade_2.textrender(clicker)
    until_passive_income_upgrade_1.textrender(clicker)
        
        
    #draw the button on the screen
    main_button.button_render()
    upgrade_button_1.button_render()
    upgrade_button_2.button_render()
    passive_income_button_1.button_render()
    
    #click amount display
    score_display.text = "you clicked: " + str(main_counter)
    click_amount_display = text((10, 500), "click worth: " + str(click_worth), font2)
    click_amount_display.textrender(clicker)
    
    passive_income_display = text((10, 550), f"you have: {input_passive_income} passive income", font2)
    passive_income_display.textrender(clicker)
    
    #animation function
    animationhandler()
    
    clock.tick(60)    
    pygame.display.flip()
