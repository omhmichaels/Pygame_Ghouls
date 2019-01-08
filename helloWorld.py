"""
#
# S0mHmxxGh0ulz
# 
# Author: l33tH@x0rxxGh0u1
#
"""


import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Somhm xx Ghouls")
while True: # Main Game Loop
    for event in pygame.event.get():
        pygame.quit()
        sys.exit()
    pygame.display.update()

