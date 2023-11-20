from pygame import *
from pygame import font
from pygame import math
import pygame
import os
import sys

font_path = "Montserrat-Medium.ttf"

if getattr(sys, 'frozen', False):
    # If the script is run as a bundled executable
    base_path = sys._MEIPASS
else:
    
    # If the script is run as a regular Python script
    base_path = os.path.abspath(os.path.dirname(__file__))
#where our font is stored locally? idk?
font_path = os.path.join(base_path, font_path)


#display initiation aswell as fonnt initiation
pygame.display.init()
pygame.font.init()
font1 = pygame.font.Font("Montserrat-Medium.ttf", 36)
font2 = pygame.font.Font("Montserrat-Medium.ttf", 28)

#colours
button_color_pink = (255, 192, 203)
button_color_black = (0, 0, 0)
button_color_white = (255, 255, 255)
button_color_red = (255, 0, 0)


class text:
    def __init__(self, position, text, font):
        self.position = position
        self.text = text
        self.font = font

    def textrender(self, surface):
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        surface.blit(text_surface, self.position)

class Button:
    def __init__(self, B_position, B_size, color, the_screen):
        self.B_position = B_position
        self.B_size = B_size
        self.color = color
        self.the_screen = the_screen
        self.rect = Rect(self.B_position[0], self.B_position[1], self.B_size[0], self.B_size[1])

    def button_render(self):
        pygame.draw.rect(self.the_screen, self.color, self.rect) 

       
#window properties
size = 800, 600
clicker = pygame.display.set_mode((size))
surface = pygame.Surface(size)
pygame.display.set_caption("clicker game")
pygame.display.flip()


# Create the text object
score_display = text((10, 10), "you clicked: ", font1)
until_next_upgrade = text((500, 200), "next upgrade: ", font2)

# create a button object
main_button = Button((100, 100), (50, 50), button_color_pink, clicker)

# creates the rects
#doesthiswork = button((200, 200), (60, 60))

clock = pygame.time.Clock()

running = True

while True:
    clicker.fill((0, 0, 0))

    for event in pygame.event.get():
        # Check for QUIT event 

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Draw the text on the screen
        score_display.textrender(clicker)
        until_next_upgrade.textrender(clicker)
        
        #draw the button on the screen
        main_button.button_render()
        

        clock.tick(60 )    
        pygame.display.flip()

