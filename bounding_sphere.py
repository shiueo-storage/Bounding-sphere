import glob
import os
import random
import time

import pygame
from pygame.locals import *
import sys
from utils import global_path

pygame.init()
global_path.set_proj_abs_path(os.path.abspath(__file__))
flags = DOUBLEBUF
screen = pygame.display.set_mode((600, 600), flags)
screen_x, screen_y = screen.get_size()
pygame.display.set_caption("Bounding Sphere")
clock = pygame.time.Clock()

mainLoop = True
while mainLoop:
    events = pygame.event.get()
    if events:
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                mainLoop = False
    pygame.display.flip()

pygame.quit()
sys.exit()