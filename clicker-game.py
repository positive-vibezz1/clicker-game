from pygame import *
from pygame import font
from pygame import math
import pygame
import os
import sys


#display initiation aswell as fonnt initiation
pygame.display.init()
pygame.font.init()


#click button
click = 0
clickworth = 1

#upgrade button
nextupgradetwo = 18
nextupgrade = 9

#reduce counter logic
reducecounter = 0
bottomout = 0

#window properties
clicker = pygame.display.set_mode((800, 600))
pygame.display.set_caption("clicker game")
pygame.display.flip()

'''
clickicon = pygame.image.load('sponge bob.png')
pygame.image.save(clickicon, 'sponge bob.png')
pygame.display.set_icon(clickicon)
'''

#clicker button properties
clickebutton = pygame.draw.rect(clicker, "pink", pygame.Rect(325, 350, 60, 60))

upgradebutton = pygame.draw.rect(clicker, "pink", pygame.Rect(675, 130, 40, 40))

#upgradebutton = pygame.draw.rect(clicker, "pink", pygame.Rect(675, 360, 40, 40))


running = True




while True:
    for event in pygame.event.get():
        # Check for QUIT event 
     
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        #checks if the mouse posotion is over our click button, and if it is then it adds 1 to the total value
        leftclick = 1
        (x, y) = pygame.mouse.get_pos()


        mouseposition = pygame.mouse.get_pos()
        mousepress = MOUSEBUTTONDOWN


        #clicker button
        if x >= 325 and x <=383 and y >= 350 and event.type == mousepress and event.button == leftclick:
            click += clickworth
            #print(nextupgrade)
            #print('u clicked: ' + str(click))

        
        #upgradebuttonone
        if x >= 663 and x <= 733 and y >= 100 and event.type == mousepress and event.button == leftclick:
            if click > nextupgrade:
                clickworth += 1
                nextupgrade *= 3

        '''
        #upgradebuttontwo
        if x >= 663 and x <= 733 and y >= 352 and y <= 402 and event.type == mousepress and event.button == leftclick:
            print('i clicked this button')
            if click > nextupgradetwo:
                clickworth += 1
                nextupgrade *= 4
        '''
                

        #our number displays, how it displays aswell as color and everything which has to do with the total value
        #click display
        def clickbuttontoaddclick():
            global click
            global clickworth
            global nextupgrade
            #draws a black rectangle over our amount text
            if event.type == mousepress and event.button == leftclick:
                pygame.draw.rect(clicker, "black", pygame.Rect(70, 120, 350, 60))

            font = pygame.font.SysFont("Times New Roman", 35)
            numberdisplay = font.render('u clicked: ' + str(click), True, 'pink')
            clicker.blit(numberdisplay, (150 - numberdisplay.get_width() // 2, 150 - numberdisplay.get_height() // 2))


        #reduces counter until next upgrade letting u know how many more clicks 
        def untilnextupgrade(countdown):
            if event.type == mousepress and event.button == leftclick:
                pygame.draw.rect(clicker, "black", pygame.Rect(440, 200, 320, 90))

            if countdown >= click - 1:
                countdown -= click - 1

            else:
                countdown = 0



            font = pygame.font.SysFont("Times New Roman", 35)
            numberdisplay = font.render('next upgrade in: ' + str(countdown), True, 'pink')
            clicker.blit(numberdisplay,(584 - numberdisplay.get_width() // 2, 250 - numberdisplay.get_height() // 2))

            return countdown

            #print(reducecounter)
            #print(click)
            

        #upgrade display
        def clickbuttontoupgradeclick():

            #draws a black rectangle over our upgrade text
            if event.type == mousepress and event.button == leftclick:
                pygame.draw.rect(clicker, "black", pygame.Rect(420, 110, 250, 100))
       
            font = pygame.font.SysFont("Times New Roman", 35)
            numberdisplay = font.render('click worth: ' + str(clickworth), True, 'pink')
            clicker.blit(numberdisplay,(550 - numberdisplay.get_width() // 2, 150 - numberdisplay.get_height() // 2))

        '''
        def clickbuttontoupgradeclicktwo():
            print("hello world")
            if event.type == mousepress and event.button == leftclick:
                pygame.draw.rect(clicker, "black", pygame.Rect(440, 200, 320, 90))

            font = pygame.font.SysFont("Times New Roman", 35)
            numberdisplay = font.render('click worth: ' + str(clickworth), True, 'pink')
            clicker.blit(numberdisplay,(550 - numberdisplay.get_width() // 2, 250 - numberdisplay.get_height() // 2))
        '''



    untilnextupgrade(nextupgrade)
    clickbuttontoaddclick()
    clickbuttontoupgradeclick()

        
    pygame.display.update()

