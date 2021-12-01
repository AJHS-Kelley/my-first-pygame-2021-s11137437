# pygame Practice, O'Berry Matthew, 12/1/21 8:19, v0.3

import pygame, sys
from pygame.locals import *

# start pygame
pygame.init()

# creat game window
windowsurface = pygame.display.set_mode((500, 400),0, 32)
pygame.display.set_caption("Hello, World!")

# set color values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setup Fonts 
BasicFont = pygame.font.sysfont(None, 48)

# Setup Text
text = BasicFont.render('hello,world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowsurface.get_rect().centerx
textRect.centery = windowsurface.get_rect().centerx

# draw a backgrown onto window surface.
windowsurface.fill(WHITE)

# draw a green polygon the surface 
pygame.draw.polygon(windowsurface, Green, ((146, 0), (291, 186), (236,277), (56,277), (0,196))

# draw bluw line on the windowsurface 
pygame.draw.polygn(windowsurface,Blue, (60,60), (120,60), 4)
pygame.draw.polygn(windowsurface,Blue, (120,60), (60,120))
pygame.draw.polygn(windowsurface,Blue, (60,120), (120,120),4)