import pygame
import sys

pygame.init()

# Window properties
size = 800, 600
clicker = pygame.display.set_mode(size)
pygame.display.set_caption("Clicker Game")

# Variables
click = 0
clickworth = 1
nextupgrade = 9

# Clock
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("Times New Roman", 35)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check for mouse click
    leftclick = 1
    (x, y) = pygame.mouse.get_pos()
    mousepress = pygame.mouse.get_pressed()

    # Clicker button
    clickebutton = pygame.Rect(325, 350, 60, 60)
    pygame.draw.rect(clicker, "pink", clickebutton)

    # Upgrade button
    upgradebutton = pygame.Rect(675, 130, 40, 40)
    pygame.draw.rect(clicker, "pink", upgradebutton)

    # Click logic
    if clickebutton.collidepoint(x, y) and mousepress[0]:
        click += clickworth

    # Upgrade logic
    if upgradebutton.collidepoint(x, y) and mousepress[0] and click > nextupgrade:
        clickworth += 1
        nextupgrade *= 3

    # Draw displays
    click_display = font.render('u clicked: ' + str(click), True, 'pink')
    clicker.blit(click_display, (150 - click_display.get_width() // 2, 150 - click_display.get_height() // 2))

    upgrade_display = font.render('click worth: ' + str(clickworth), True, 'pink')
    clicker.blit(upgrade_display, (550 - upgrade_display.get_width() // 2, 150 - upgrade_display.get_height() // 2))

    countdown_display = font.render('next upgrade in: ' + str(nextupgrade - click), True, 'pink')
    clicker.blit(countdown_display, (584 - countdown_display.get_width() // 2, 250 - countdown_display.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)
