import pygame as pg
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"   
import math
from random import randint

os.environ["SDL_VIDEO_CENTERED"] = '1'
width, height = 1920, 1080
size = (width,height)
red, black = (200, 200, 200), (0,0,0)
pg.init()
pg.display.set_caption('Lorenz Attractor')
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
# Pygame Clock
fps = 160

sigma = 10
rho = 28
beta = 8/3

x, y, z = 0.01, 0, 0
scale = 15

run = True
while run:
    #screen.fill(black)
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()

    time = 0.01
    dx = (sigma * (y-x)) * time
    dy = (x * (rho - z) - y) * time
    dz = (x * y - beta * z) * time

    x = x + dx

    y = y + dy

    z = dz + z

    pg.draw.circle(screen, (255,0,0), (int(x * scale) + width//2, int(y * scale) + height//2), 1)

    pg.display.update()

pg.quit()


