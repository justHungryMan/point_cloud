import itertools
import math
from random import *
from tqdm import tqdm
import numpy as np
import sys
from operator import itemgetter



N = 4
EPSILON = sys.float_info.epsilon

#a = [[-6.772171368040148, 3.098186881994504], [-1.015157048167616, 0.9770798741858915], [-0.38145326793389955, 7.190889223809808], [4.097874586341421, 5.61204317597225], [4.252019029739728, 8.176340881976259], [4.824121836576495, 6.843110566759066], [4.920106550992996, -1.457297689898427], [4.926588124825223, -9.43856674908825], [5.165375161277963, 8.917174689870539], [5.178001279084432, -8.715059917890539]]
#b = [[-8.511766992371367, 0.5822082797271122], [-4.867715188789128, 5.334296558302313], [-2.0908517321324505, -5.045556792483186], [1.4469717294339883, -6.558630128959171], [3.8527510519820325, 0.06859265595500474], [4.416209872289755, -9.770144371495014], [5.169177133100508, 9.527711314043248], [6.577845516830926, -1.5330301486081694], [6.739524021155013, 0.17348379982137452], [9.9562681620889, 7.677228569878874]]


'''
for i in range(N):
    temp1 = uniform(-10, 10)
    temp2 = uniform(-10, 10)
    a.append([temp1, temp2])
    temp1 = uniform(-10, 10)
    temp2 = uniform(-10, 10)
    b.append([temp1, temp2])
'''

a = [[-3.2, 1.3], [2.5, 3.6], [-3.1, 2.6], [7.7, -1.2]]


a = sorted(a)
print(a)
b = [[1.1,3.0], [5.2,-2.1], [4.1,1.3], [-5.1, 2.3]]

# Step 0 : make hungarian matrix
print("Step 0")
hungarian_matrix = np.ndarray((N,N), dtype = list).tolist()
for a_idx, a_ele in enumerate(a):
    for b_idx, b_ele in enumerate(b):
        dist = 0
        
        for i in range(len(a_ele)):
            dist += (a_ele[i] - b_ele[i]) ** 2
        hungarian_matrix[a_idx][b_idx] = dist

print(hungarian_matrix)


# Step 1 : substract row minimum
print("Step 1")
hungarian_matrix = hungarian_matrix - np.min(hungarian_matrix, axis = 1).reshape(N, -1)
print(hungarian_matrix)

# Step 2 : substract column minimum
print("Step 2")
hungarian_matrix = hungarian_matrix - np.min(hungarian_matrix, axis = 0)
print(hungarian_matrix)

# Step 3 : find optimal solution
zero_element_matrix = np.zeros((N, N))
# 1 is zero else 0

zero_line = []
for i in range(N):
    column_cnt = 0

    for j in range(N):
        if hungarian_matrix[i][j] < EPSILON:
            column_cnt += 1
            zero_element_matrix[i][j] = 1

    zero_line.append((column_cnt, "column", i))
        
# |
for i in range(N):        
    row_cnt = 0
    for j in range(N):
        if hungarian_matrix[j][i] < EPSILON:
            row_cnt += 1
    zero_line.append((row_cnt, "row", i))
# -
zero_line = sorted(zero_line, key = itemgetter(0), reverse = True)
print(zero_line)
sum_row_column = 0
for ele in range(len(zero_line)):
    if ele[1] is "column" and (zero_element_matrix[ele[2]] == 0).sum is not 0:
        for i in range(N):
            zero_element_matrix[ele[2]][i] = -1
    elif ele[1] is "row" and (zero_element_matrix.T[ele[2]] == 0).sum is not 0:
        for i in range(N):
            zero_element_matrix[i][ele[2]] = -1
    sum_row_column += 1

    if (zero_element_matrix == 0).sum() is 0:
        break

if sum_row_column is N:
    #go to Step 6
    temp = []
else:
    #go to Step 4
    for i in range(N):
        for j in range(N):


            
        

    
'''
permutation = itertools.permutations(b)

min_distance = math.inf
ans = []
cnt = 0
for i in permutation:
    dist = 0
    for idx, ele in enumerate(i):
        dist += math.sqrt((a[idx][0] - ele[0]) ** 2 + (a[idx][1] - ele[1]) ** 2)

    if dist < min_distance:
        min_distance = dist
        ans = i        
    cnt += 1 
print("---------")
print(cnt)
print(min_distance)
print(ans)


b = list(reversed(b))

dist = 0
for idx, ele in enumerate(b):
    dist += math.sqrt((a[idx][0] - ele[0]) ** 2 + (a[idx][1] - ele[1]) ** 2)
print("sorted result")
print("a :", a)
print("b :", b)
print(dist)
'''