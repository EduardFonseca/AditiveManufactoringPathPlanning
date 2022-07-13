import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import scipy as sp
from stl import mesh

def stlPreparator(path, layerHeight = 0.16):
    '''
    Read, rotate and slice the STL file
    
    Parameters:
        path [string]: path to the stl file
        layerHeight [float]: layer height in mm
    
    Returns:
        slicedFile [array]: array of vertices in each layer
    '''
    # Read the STL file
    mesh_data = mesh.Mesh.from_file(path)

    # TODO: Rotate the STL file automatically
    # mesh.rotate([0,0,1],-90)
    # TODO: Slice the STL file

    # return slicedFile

def STL_ploter(file):
    # Create a new figure
    figure = plt.figure()
    axes = mplot3d.Axes3D(figure)

    # Plot the mesh
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(file.vectors))
    
    # Auto-scale to the mesh size
    scale = file.points.flatten('F')
    axes.auto_scale_xyz(scale, scale, scale)

    plt.show()


if __name__ == "__main__":
    mesh_file = r'stl\cube.stl'
    mesh_data = mesh.Mesh.from_file(mesh_file)
    STL_ploter(mesh_data)
    # plot v0
    # axes.scatter(mesh_data.v2[:, 0], mesh_data.v2[:, 1], mesh_data.v2[:, 2], c='r', marker='o')


