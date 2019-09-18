import assignments as AS
import tree as T
import numpy as np
import pyvista as pv

from pyvista import examples
from operator import itemgetter


# Configuration
N = 2
GRID_SIZE = N * N * N

# Dataset
dataset_teapot = examples.download_teapot()
dataset_bunny = examples.download_bunny_coarse()

# Generate Points
teapot_points, teapot_bounds = T.generate_points(dataset_teapot)
bunny_points, bunny_bounds = T.generate_points(dataset_bunny)

# Generate Grid
teapot_grid, teapot_grid_bounds = T.generate_grid(teapot_points, teapot_bounds, N)
bunny_grid, bunny_grid_bounds = T.generate_grid(bunny_points, bunny_bounds, N)

# Generate Grid Clustering
T.geneate_grid_clustering(teapot_grid, bunny_grid, N)

# Grid Assignment
source, destination = AS.grid_assignment(teapot_grid, bunny_grid, N)

# Test
AS.printQueue(source, destination)