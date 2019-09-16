import numpy as np
import pyvista as pv
from pyvista import examples
from operator import itemgetter

#mesh = examples.download_teapot()
#mesh.plot(cpos=[-1, 2, -5], show_edges=True)

# Configuration
N = 3
GRID_SIZE = N * N * N

# Define some helpers - ignore these and use your own data!
dataset = examples.download_teapot()
bounds = dataset.bounds # x, y, z
center = dataset.center

def generate_points(dataset = examples.download_teapot(), subset=1):
    """A helper to make a 3D NumPy array of points (n_points by 3)"""
    ids = np.random.randint(low=0, high=dataset.n_points-1,
                            size=int(dataset.n_points * subset))
    return dataset.points[ids]


points = generate_points(dataset)
# Print firts 5 rows to prove its a numpy array (n_points by 3)
# Columns are (X Y Z)

# Center align
center = np.array(center).reshape(-1, 3)
points = points - center

# bounds translation
bounds[0] = bounds[0] - center[0][0]
bounds[1] = bounds[1] - center[0][0]
bounds[2] = bounds[2] - center[0][1]
bounds[3] = bounds[3] - center[0][1]
bounds[4] = bounds[4] - center[0][2]
bounds[5] = bounds[5] - center[0][2]

# 함수화 작업 필요함.
grid = np.ndarray((N,N,N), dtype = dict).tolist()
for point in points:
    for i in range(N): # x
        xAxis = (bounds[1] - bounds[0]) / N * (i + 1) + bounds[0]
        for j in range(N): # y
            yAxis = (bounds[3] - bounds[2]) / N * (j + 1) + bounds[2]
            for k in range(N): # z
                zAxis = (bounds[5] - bounds[4]) / N * (k + 1) + bounds[4]
                if point[0] >= xAxis - (bounds[1] - bounds[0]) / N and point[0] < xAxis and point[1] >= yAxis - (bounds[3] - bounds[2]) / N and point[1] < yAxis and point[2] >= zAxis - (bounds[5] - bounds[4]) / N and point[2] < zAxis:
                    if grid[i][j][k] is None:
                        grid[i][j][k] = {
                            "element": [],
                            "child": []
                        }
                    grid[i][j][k]["element"].append(point)


'''
points = sorted(points, key = itemgetter(0, 1, 2))
tree = {
    "element": points,
    "child": [None] * 2
}


def orthogonalClustering(tree, bounds, xAxis, yAxis, zAxis):
    tree["child"][0] = {
        "elements": [],
        "child": [None] * 2
    }
    tree["child"][1] = {
        "elements": [],
        "child": [None] * 2
    }
    elements = tree["elements"]
    children = tree["child"]

    if xAxis is True:
        children[0] = elements[: len(elements) / 2]
        children[1] = elements[len(elements / 2) :]
        
        



point_cloud = pv.PolyData(points)
print(point_cloud)

point_cloud.plot(eye_dome_lighting=True)
'''