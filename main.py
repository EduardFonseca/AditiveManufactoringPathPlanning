import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def createGrid(size,distance):
    '''
    Create a grid to alocate certain surface before aplying the pixel method
    
    Parameters:
        size [int]: size of the square grid
        distance [int]: distance between nodes in the grid
    '''
    # canvas = np.mat([[(x%distance == 0 and y%distance == 0) for x in range(size)] for y in range(size)])
    canvas = np.mat([[((size)**2-((x+1)+10*(y))) for x in range(size)] for y in range(size)]) #so funciona para matriz ate 10x10 pensar em uma forma de generalizar isso melhor
    
    return canvas

if __name__ == "__main__":
    pass