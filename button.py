from pygame import *
from pygame import font
from pygame import math
import pygame



class Button:
    def __init__(self, B_position, B_size, the_screen):
        self.B_position = B_position
        self.B_size = B_size
        self.the_screen = the_screen
        self.rect = Rect(self.B_position[0], self.B_position[1], self.B_size[0], self.B_size[1])

    def button_render(self):
        pygame.draw.rect(self.the_screen, self.rect)
        
    def is_clicked(self, mouse_pos, mouse_button):
        leftclick = 1
        return self.rect.collidepoint(mouse_pos) and mouse_button == leftclick
    
    def set_size(self, size):
        self.B_size = size
        self.rect.size = size
        return self.B_size, self.rect.size

    def main_cookie(self, imagepath, surface):
        image = pygame.image.load(imagepath)
        scaledimage = pygame.transform.scale(image, self.B_size)
        surface.blit(scaledimage, self.B_position)