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

font_path = os.path.join(base_path, font_path)


#display initiation aswell as fonnt initiation
pygame.display.init()
pygame.font.init()
font1 = pygame.font.Font("Montserrat-Medium.ttf", 36)
font2 = pygame.font.Font("Montserrat-Medium.ttf", 28)

class clickergame:
    def __init__(self, position, text, font):
        self.position = position
        self.text = text
        self.font = font

    def clickamount(self, surface):
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        surface.blit(text_surface, self.position)


#window properties
size = 800, 600
clicker = pygame.display.set_mode((size))
surface = pygame.Surface(size)
pygame.display.set_caption("clicker game")
pygame.display.flip()





# Create a NumberDisplay object
score_display = clickergame((10, 10), "you clicked: ", font1)
until_next_upgrade = clickergame((500, 200), "next upgrade: ", font2)

clock = pygame.time.Clock()

running = True
while True:
    clicker.fill((0, 0, 0))

    for event in pygame.event.get():
        # Check for QUIT event 

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Draw the score on the screen
        score_display.clickamount(clicker)
        until_next_upgrade.clickamount(clicker)

        clock.tick(60)   
        pygame.display.flip()
