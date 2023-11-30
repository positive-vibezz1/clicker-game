from pygame import *
from pygame import font
from pygame import math
import pygame



class Button:
    def __init__(self, B_position, B_size, color, the_screen):
        self.B_position = B_position
        self.B_size = B_size
        self.color = color
        self.the_screen = the_screen
        self.rect = Rect(self.B_position[0], self.B_position[1], self.B_size[0], self.B_size[1])

    def button_render(self):
        pygame.draw.rect(self.the_screen, self.color, self.rect)
        
    def is_clicked(self, mouse_pos, mouse_button):
        leftclick = 1
        return self.rect.collidepoint(mouse_pos) and mouse_button == leftclick
