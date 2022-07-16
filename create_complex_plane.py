import numpy as np

def create_complex_plane(minimum, maximum, stepsize):
    plane = [[]]
    numrows = int((maximum.imag - minimum.imag) / stepsize)
    numcols = int((maximum.real - minimum.real) / stepsize)
    for x in range(numcols+1):
        plane[0].append(minimum + x * stepsize)
    for x in range(1, numrows+1):
        plane.insert(0, [])
        for y in plane[-1]:
            plane[0].append(y+1j*x*stepsize)
    return np.array(plane, dtype=object)
