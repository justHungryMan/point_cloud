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

#test
#dataset_teapot.plot(cpos=[-1, 2, -5], show_edges=True)
print(type(dataset_teapot.points))

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


# TEST
FRAME = 6000
filename = "test.mp4"


sourceList = []
for element in source:
    sourceList.append(element["element"])
source_dataset = pv.PolyData(np.array(sourceList))
#source_dataset.plot(show_edges = True)

destinationList = []
for element in destination:
    destinationList.append(element["element"])
destination_dataset = pv.PolyData(np.array(destinationList))
#destination_dataset.plot(show_edges = True)

plotter = pv.Plotter()
plotter.open_movie(filename)
plotter.add_mesh(source_dataset, color='red')

plotter.show(auto_close = False)
plotter.write_frame()

for i in range(FRAME):
    source_dataset.points = destination_dataset.points * i / FRAME + source_dataset.points * (FRAME - i) / FRAME
    plotter.write_frame()

# Test
AS.printQueue(source, destination)