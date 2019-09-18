# source & destination is both tree.
import math

element = [1, 2, 3]
test1src = {
    "element": None, #1
    "child": [{
        "element": None, #2
        "child": [{
            "element": None, #4
            "child": [{
                "element": 8, #8
                "child": [None] * 2
            }, {
                "element": 9, #9
                "child": [None] * 2
            }]
        }, {
            "element": None, #5
            "child": [{
                "element": 10, #10
                "child": [None] * 2
            }, {
                "element": 11, #11
                "child": [None] * 2
            }]
        }]
    }, {
        "element": None, #3
        "child": [{
            "element": 6, #6
            "child": [None] * 2
        }, {
            "element": None, #7
            "child": [{
                "element": 12, #12
                "child": [None] * 2
            }, {
                "element": 13, #13
                "child": [None] * 2
            }]
        }]
    }]
}

test1det = {
    "element": None, #1
    "child": [{
        "element": None, #2
        "child": [{
            "element": 4, #4
            "child": [None] * 2
        }, {
            "element": None, #5
            "child": [{
                "element": 8, #8
                "child": [None] * 2
            }, {
                "element": 9, #9
                "child": [None] * 2
            }]
        }]
    }, {
        "element": None, #3
        "child": [{
            "element": 6, #6
            "child": [None] * 2
        }, {
            "element": 7, #7
            "child": [None] * 2
        }]
    }]
}

test2src = {
    "element": None, #1
    "child": [{
        "element": None, #2
        "child": [{
            "element": None, #4
            "child": [{
                "element": [1, 2, 3], #7
                "child": [None] * 2
            }, {
                "element": [4, 5, 6], #8
                "child": [None] * 2
            }]
        }, {
            "element": None, #5
            "child": [{
                "element": [7, 8, 9], #9
                "child": [None] * 2
            }, None]
        }]
    },{
        "element": None, #3
        "child": [None, {
            "element": [10, 11, 12], #6
            "child": [None] * 2
        }]
    }]
}

test2det = {
    "element": None, #1
    "child": [{
        "element": None, #2
        "child": [{
            "element": [-1, -2, -3], #4
            "child": [None] * 2
        }, None]
    },{
        "element": None, #3
        "child": [{
            "element": [-4, -5, -6], #5
            "child": [None] * 2
        }, {
            "element": [-7, -8, -9], #6
            "child": [None] * 2
        }]
    }]
}


def assignment(source, destination, queue = {"src": [], "det": []}):
    if source is None or destination is None:
        queue["src"].append(source)
        queue["det"].append(destination)
    elif source["element"] is None and destination["element"] is None:
        assignment(source["child"][0], destination["child"][0], queue)
        assignment(source["child"][1], destination["child"][1], queue)
    else:
        queue["src"].append(source)
        queue["det"].append(destination)
    return queue

def stretch(queue):
    cluster1 = [] # source
    cluster2 = [] # destination

    source = queue["src"]
    destination = queue["det"]

    while source:
        srcElement = source.pop(0)
        detElement = destination.pop(0)
        if detElement is None:
            nodeToTree(cluster2, cluster1, detElement, srcElement)
        elif srcElement is None:
            nodeToTree(cluster1, cluster2, srcElement, detElement)
        elif srcElement["element"] is not None and detElement["element"] is not None:
            cluster1.append(srcElement)
            cluster2.append(detElement)
        elif srcElement["element"] is not None and detElement["element"] is None:
            nodeToTree(cluster1, cluster2, srcElement, detElement)
        elif srcElement["element"] is None and detElement["element"] is not None:
            nodeToTree(cluster2, cluster1, detElement, srcElement)
    return cluster1, cluster2
            
def nodeToTree(nodeCluster, treeCluster, node, tree):
    if tree["child"][0] is None and tree["child"][1] is None:
        nodeCluster.append(node)
        treeCluster.append(tree)
    if tree["child"][0] is not None:
        if tree["child"][0]["element"] is not None:
            nodeCluster.append(node)
            treeCluster.append(tree["child"][0])
        elif tree["child"][0]["element"] is None:
            nodeToTree(nodeCluster, treeCluster, node, tree["child"][0])
    if tree["child"][1] is not None:
        if tree["child"][1]["element"] is not None:
            nodeCluster.append(node)
            treeCluster.append(tree["child"][1])
        elif tree["child"][1]["element"] is None:
            nodeToTree(nodeCluster, treeCluster, node, tree["child"][1])

def printQueue(cluster1, cluster2):
    print(cluster1)
    print(cluster2)

def grid_assignment(source_grid, destination_grid, N = 3):
    source = []
    destination = []
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                queue = assignment(source_grid[i][j][k], destination_grid[i][j][k])
                cluster1, cluster2 = stretch(queue)
                source += cluster1
                destination += cluster2
    
    #removeNone(source, destination)

    return source, destination

def removeNone(source, destination):
    for i in range(len(source)):
        if source[i] is None:
            if i is 0:
                source[0] = source[1]
            elif i is len(source) - 1:
                source[i] = source[i - 1]
            elif distance(source[i - 1], destination[i]) < distance(source[i + 1], destination[i]):
                source[i] = source[i - 1]
            else:
                source[i] = source[i + 1]
        elif destination[i] is None:
            if i is 0:
                destination[0] = destination[1] 
            elif i is len(source) - 1 :
                destination[i] = source[i - 1]
            elif distance(source[i], destination[i - 1]) < distance(source[i], destination[i + 1]):
                destination[i] = destination[i - 1]
            else:
                destination[i] = destination[i + 1]
            
def distance(source, destination):
    return (source["element"][0] - destination["element"][0]) ** 2 + (source["element"][1] - destination["element"][1]) ** 2 + (source["element"][2] - destination["element"][2]) ** 2

queue = assignment(test2src, test2det)
cluster1, cluster2 = stretch(queue)
removeNone(cluster1, cluster2)
printQueue(cluster1, cluster2)
