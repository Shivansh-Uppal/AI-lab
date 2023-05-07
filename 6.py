#write a program to implement 8-puzzle problem using A* search algorithm

#initial state
#f(n) = g(n) + h(n)

#f(n)=7
# 2 8 3
# 1 6 4
# 7   5

#f(n)=3
# 2 8 3
# 1   4
# 7 6 5

#f(n)=3
# 2   3
# 1 8 4
# 7 6 5

#f(n)=2
#   2 3
# 1 8 4
# 7 6 5

#f(n)=1
# 1 2 3
#   8 4
# 7 6 5

# 1 2 3
# 8   4
# 7 6 5

#final state
# 1 2 3
# 8   4
# 7 6 5

import heapq
import copy

start= [[2,8,3],[1,6,4],[7,0,5]]
goal = [[1,2,3],[8,0,4],[7,6,5]]

def heuristic(state):
    # calculate the number of misplaced tiles
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != (i*3 + j + 1) % 9:
                h += 1
    return h

def find_zero(state):
    # find the position of the empty tile (represented by 0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)
    return None

def move_up(state, i, j):
    # move the empty tile up
    new_state = copy.deepcopy(state)
    new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
    return new_state

def move_down(state, i, j):
    # move the empty tile down
    new_state = copy.deepcopy(state)
    new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
    return new_state

def move_left(state, i, j):
    # move the empty tile left
    new_state = copy.deepcopy(state)
    new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
    return new_state

def move_right(state, i, j):
    # move the empty tile right
    new_state = copy.deepcopy(state)
    new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
    return new_state

def get_neighbors(state):
    # return the possible new states from the current state
    i, j = find_zero(state)
    neighbors = []
    if i > 0:
        neighbors.append(move_up(state, i, j))
    if i < 2:
        neighbors.append(move_down(state, i, j))
    if j > 0:
        neighbors.append(move_left(state, i, j))
    if j < 2:
        neighbors.append(move_right(state, i, j))
    return neighbors



def a_star_search(start, goal):
    heap = []
    heapq.heappush(heap, (0, start, 0, [start], [0]))
    visited = set()
    while heap:
        f, state, depth, path, f_values = heapq.heappop(heap)
        if state == goal:
            return path, f_values
        if tuple(map(tuple, state)) in visited:
            continue
        visited.add(tuple(map(tuple, state)))
        for neighbor in get_neighbors(state):
            g = depth + 1
            f = g + heuristic(neighbor)
            heapq.heappush(heap, (f, neighbor, g, path + [neighbor], f_values + [f]))

    return -1

path,f_values = a_star_search(start, goal)
if path == -1:
    print("No solution found")
else:
    for i, state in enumerate(path):
        for row in state:
            print(row)
        print("f value:", f_values[i])
        print()
