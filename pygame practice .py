# pygame Practice, O'Berry Matthew, 11/29/21 8:37, v0.2

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
text = basicFont.render('hello,world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowsurface.get_rect().centerx
textRect.centery = windowsurface.get_rect().centerx
