import numpy as np
import create_complex_plane as ccp
from PIL import Image as im
from widgets import *
from math import cos

def is_in_mandelbrot(c, tot_iter):
    zpos = 0
    if abs(c-0.2)<0.45-0.45*cos(np.angle(c-0.2)) or (c.real+1)**2+c.imag**2<0.04:
        return 0
    for x in range(tot_iter):
        zpos=zpos**2+c
        if abs(zpos) > 2:
            return round(255-x*(255/tot_iter))
    if abs(zpos) < 2:
        return 0

def is_in_julia(zpos, tot_iter, c):
    for x in range(tot_iter):
        zpos=zpos**2+c
        if abs(zpos) > 4:
            return round(255-x*(255/tot_iter))
    if abs(zpos) < 4:
        return 0

def create_mandelbrot(stepsize=0.001, minpoint=-2-1j, maxpoint=0.5+1j, iterations=100, is_julia=False, c=0):
    clock_start()
    grid = ccp.create_complex_plane(minpoint, maxpoint, stepsize)
    output = np.zeros(np.shape(grid), np.uint8)
    if is_julia is False:
        for x in range(len(grid)):
            progress_percent(x, len(grid))
            for y in range(len(grid[0])):
                try:
                    output[x, y]=is_in_mandelbrot(grid[x, y], iterations)
                except TypeError:
                    output[x, y]=0
    if is_julia is True:
        for x in range(len(grid)):
            progress_percent(x, len(grid))
            for y in range(len(grid[0])):
                try:
                    output[x, y]=is_in_julia(grid[x, y], iterations, c)
                except TypeError:
                    output[x, y]=0
    clock_end()
    img = im.fromarray(output, "L")
    img.show()

# create_mandelbrot(0.000000025, -0.98966+0.25242j, -0.98939+0.25258j, iterations=300) looks nice
# create_mandelbrot(0.0000000025, -1.044695257-0.246678932j, -1.044693493-0.246677618j, 1500) like bro
