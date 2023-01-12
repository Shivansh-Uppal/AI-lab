# Water jug problem
from collections import deque

# Jug capacities
jug1 =int(input("Enter the capacity (in gallons) for jug 1: "))
jug2 = int(input("Enter the capacity (in gallons) for jug 2: "))

# Target amount of water
target =int(input("Enter the amount of water to be obtained (in gallons): "))

# Initial state
init_state = (0, 0)

# Visited states
visited = set()

# Queue for BFS
queue = deque([init_state])
visited.add(init_state)

# Function to check if a state is valid
def is_valid(state):
    if state[0] > jug1 or state[1] > jug2 or state[0] < 0 or state[1] < 0:
        return False
    return True

# Function to check if a state is goal
def is_goal(state):
    if (state[0] == target and state[1] == 0) or (state[0] == 0 and state[1] == target):
        return True
    return False

def rule(state):
    new_states = []
    # Rule 1: Fill jug 1 (x,y) -> (jug1,y)
    new_state = (jug1, state[1])
    if new_state not in visited and is_valid(new_state):
        print("Rule 1: Fill jug 1")
        new_states.append(new_state)
        visited.add(new_state)
    # Rule 2: Fill jug 2 (x,y) -> (x,jug2)
    new_state = (state[0], jug2)
    if new_state not in visited and is_valid(new_state):
        print("Rule 2: Fill jug 2")
        new_states.append(new_state)
        visited.add(new_state)
    # Rule 3: Pour some water out of the jug 1 (x,y) -> (x-d,y) if x>0
    new_state = (state[0]-min(state[0],jug2-state[1]), state[1]+min(state[0],jug2-state[1]))
    if new_state not in visited and is_valid(new_state):
        print("Rule 3: Pour some water out of the jug 1")
        new_states.append(new_state)
        visited.add(new_state)
    # Rule 4: Pour some water out of the jug 2 (x,y) -> (x,y-d) if y>0
    new_state = (state[0]+min(state[1],jug1-state[0]), state[1]-min(state[1],jug1-state[0]))
    if new_state not in visited and is_valid(new_state):
        print("Rule 4: Pour some water out of the jug 2")
        new_states.append(new_state)
        visited.add(new_state)
    # Rule 5: Empty jug 1 (x,y) -> (0,y)
    new_state = (0, state[1])
    if new_state not in visited and is_valid(new_state):
        print("Rule 5: Empty jug 1")
        new_states.append(new_state)
        visited.add(new_state)
    # Rule 6: Empty jug 2 (x,y) -> (x,0)
    new_state = (state[0], 0)
    if new_state not in visited and is_valid(new_state):
        print("Rule 6: Empty jug 2")
        new_states.append(new_state)
        visited.add(new_state)
    # Rule 7: Pour water from jug 2 into jug 1 until the jug 1 is full (x,y) -> (jug1,y-(jug1-x)) if x+y>=jug1,y>0
    new_state = (jug1, state[1]-min(state[1],jug1-state[0]))
    if new_state not in visited and is_valid(new_state):
        print("Rule 7: Pour water from jug 2 into jug 1 until the jug 1 is full")
        new_states.append(new_state)
        visited.add(new_state)
    # Rule 8: Pour water from jug 1 into jug 2 until the jug 2 is full (x,y) -> (x-(jug2-y),jug2) if x+y>=jug2,x>0
    new_state = (state[0]-min(state[0],jug2-state[1]), jug2)
    if new_state not in visited and is_valid(new_state):
        print("Rule 8: Pour water from jug 1 into jug 2 until the jug 2 is full")
        new_states.append(new_state)
        visited.add(new_state)
    # Rule 9: Pour all water from the jug1 into the jug2 (x,y) -> (0,x+y) if x+y<=jug2,x>0
    new_state = (0, state[0]+state[1])
    if new_state not in visited and is_valid(new_state):
        print("Rule 9: Pour all water from the jug1 into the jug2")
        new_states.append(new_state)
        visited.add(new_state)
    # Rule 10: Pour all water from the jug2 into the jug1 (x,y) -> (x+y,0) if x+y<=jug1,y>0
    new_state = (state[0]+state[1], 0)
    if new_state not in visited and is_valid(new_state):
        print("Rule 10: Pour all water from the jug2 into the jug1")
        new_states.append(new_state)
        visited.add(new_state)
    return new_states

while queue:
    state = queue.popleft()
    if is_goal(state):
        print("Found goal state:", state)
        break
    new_states = rule(state)
    for new_state in new_states:
        queue.append(new_state)
        print(new_state)
