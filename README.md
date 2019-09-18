# Point Cloud

### tree.py

#### generate_point
dataset을 이용하여 point set을 생성, 원점을 센터로 만들어준 point set을 반환한다.

#### generate_grid
point set의 inner bounds space를 N^3 공간으로 grid화 하여 해당되는 point를 각 grid에 할당한다.

#### generate_grid_clustering
각 grid 별로 clustering 한다.

#### sorted_clustering
grid 내의 점들을 정렬하여 tree화 한다.

#### generate_tree
주어진 grid 의 점들을 바탕으로 binary tree를 만든다.


--- 

### assignment.py

#### assignment
Reference : assignment in Point cloud morphing paper

#### stretch
node 와 tree 가 할당되었을때 트리의 모든 노드를 해당 노드와 할당되게 늘려준다.

#### nodeToTree
tree 의 모든 요소를 node 에 할당

#### grid_assignment
source와 destination에 대하여 모든 grid 를 1:1 로 mapping 하여 assignment 를 진행.

#### removeNone
None 과 node 가 할당되는 경우 None 을 가장 인접한 node로 바꿔준다. (1:N mapping)

#### distance
L2 distance 