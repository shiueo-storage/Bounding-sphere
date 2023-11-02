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
screen = pygame.display.set_mode((700, 700), flags)
screen_x, screen_y = screen.get_size()
pygame.display.set_caption("Bounding Circle")
clock = pygame.time.Clock()

N = 120

POINT_RADIUS = 3
points = []
FONT = pygame.font.Font(None, 60)


class Point:
    def __init__(self, X=0.5, Y=0.5):
        self.X = X
        self.Y = Y


for _ in range(N):
    points.append(Point(X=screen_x // 4 + random.uniform(0, 1) * (screen_x * 2 // 4),
                        Y=screen_y // 4 + random.uniform(0, 1) * (screen_y * 2 // 4)))


def Welzl(point_set):
    pass


mainLoop = True
while mainLoop:
    N_INDICATOR = FONT.render(f"N={N}", False, (255, 255, 255))
    screen.blit(N_INDICATOR, (10, 10))
    events = pygame.event.get()
    if events:
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                mainLoop = False

    for point in points:
        pygame.draw.circle(screen, (255, 255, 255), (point.X, point.Y), POINT_RADIUS)

    dt = clock.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()
