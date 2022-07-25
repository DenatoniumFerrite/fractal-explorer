from fractal_gen import *
from PIL import Image

mandel = create_mandelbrot(0.01)
image_convert(mandel, mode="s")
