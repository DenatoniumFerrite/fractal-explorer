import numpy as np
import create_complex_plane as ccp
from PIL import Image as im
from widgets import *
from math import cos
import tkinter as tk
from pathlib import Path
import os

def is_in_mandelbrot(c, tot_iter):
    z = 0+0j
    if abs(c-0.2)<0.45-0.45*cos(np.angle(c-0.2)) or (c.real+1)**2+c.imag**2<0.04:
        return 0
    for x in range(tot_iter):
        z=z**2+c
        if z.real**2+z.imag**2>4:
            return round(255-x*(255/tot_iter))
    return 0

def is_in_julia(z, tot_iter, c):
    for x in range(tot_iter):
        z=z**2+c
        if z.real()**2+z.imag()**2>4:
            return round(255-x*(255/tot_iter))
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
    return output

def image_convert(array, mode="d"):
    if array.dtype=="uint8":
        img = im.fromarray(array, "L")
    if mode=="d":
        img.show()
    if mode=="s":
        def save():
            name = (entry.get() + ".png")
            path = (os.path.expanduser("~") + "/Desktop/" + name)
            os.system("touch " + path)
            img.save(fp=path)
            window.destroy()
        window = tk.Tk(screenName="Save image")
        label = tk.Label(text="Save to desktop as:", borderwidth=10)
        entry = tk.Entry()
        button = tk.Button(text="Save", command=save, borderwidth=10)
        label.pack()
        entry.pack()
        button.pack()
        window.mainloop()

    

# create_mandelbrot(0.000000025, -0.98966+0.25242j, -0.98939+0.25258j, iterations=300) looks nice
# create_mandelbrot(0.0000000025, -1.044695257-0.246678932j, -1.044693493-0.246677618j, 1500) like bro
