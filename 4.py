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

# Function to implement rules
def rule(state):
    new_states = []
    # Rule 1: Fill jug 1
    #1
    new_state = (jug1, state[1])
    if new_state not in visited and is_valid(new_state):
        print("Rule 1: Fill jug 1\n")
        new_states.append(new_state)
        visited.add(new_state)
    # Rule 2: Fill jug 2
    #2
    new_state = (state[0], jug2)
    if new_state not in visited and is_valid(new_state):
        print("Rule 2: Fill jug 2\n")
        new_states.append(new_state)
        visited.add(new_state)
    # Rule 3: Empty jug 1
    #3
    new_state = (0, state[1])
    if new_state not in visited and is_valid(new_state):
        print("Rule 3: Empty jug 1\n")
        new_states.append(new_state)
        visited.add(new_state)
    # Rule 4: Empty jug 2
    #4
    new_state = (state[0], 0)
    if new_state not in visited and is_valid(new_state):
        print("Rule 4: Empty jug 2\n")
        new_states.append(new_state)
        visited.add(new_state)
    # Rule 5: Pour water from jug 1 to jug 2
    #5
    new_state = (state[0] - min(state[0], jug2 - state[1]), state[1] + min(state[0], jug2 - state[1]))
    if new_state not in visited and is_valid(new_state):
        print("Rule 5: Pour water from jug 1 to jug 2\n")
        new_states.append(new_state)
        visited.add(new_state)
    # Rule 6: Pour water from jug 2 to jug 1
    #6
    new_state = (state[0] + min(state[1], jug1 - state[0]), state[1] - min(state[1], jug1 - state[0]))
    if new_state not in visited and is_valid(new_state):
        print("Rule 6: Pour water from jug 2 to jug 1\n")
        new_states.append(new_state)
        visited.add(new_state)
    # Rule 7: Pour water from jug 1 to jug 2 until jug 1 is empty
    #7
    new_state = (0, state[1] + state[0])
    if new_state not in visited and is_valid(new_state):
          print("Rule 7: Pour water from jug 1 to jug 2 until jug 1 is empty\n")
          new_states.append(new_state)
          visited.add(new_state)
    # Rule 8: Pour water from jug 2 to jug 1 until jug 2 is empty
    #8
    new_state = (state[0] + state[1], 0)
    if new_state not in visited and is_valid(new_state):
           print("Rule 8: Pour water from jug 2 to jug 1 until jug 2 is empty\n")
           new_states.append(new_state)
           visited.add(new_state)
    # Rule 9: Pour water from jug 1 to jug 2 until jug 2 is full
    #9
    new_state = (state[0] - (jug2 - state[1]), jug2)
    if new_state not in visited and is_valid(new_state):
          print("Rule 9: Pour water from jug 1 to jug 2 until jug 2 is full\n")
          new_states.append(new_state)
          visited.add(new_state)
    # Rule 10: Pour water from jug 2 to jug 1 until jug 1 is full
    #10
    new_state = (jug1, state[1] - (jug1 - state[0]))
    if new_state not in visited and is_valid(new_state):
         print("Rule 10: Pour water from jug 2 to jug 1 until jug 1 is full\n")
         new_states.append(new_state)
         visited.add(new_state)
    # Rule 11: Pour enough water from jug 1 to jug 2 to make the amount of water in jug 2 equal to the target
    #11
    new_state = (state[0] - (target - state[1]), target)
    if new_state not in visited and is_valid(new_state):
           print("Rule 11: Pour enough water from jug 1 to jug 2 to make the amount of water in jug 2 equal to the target\n")
           new_states.append(new_state)
           visited.add(new_state)
    # Rule 12: Pour enough water from jug 2 to jug 1 to make the amount of water in jug 1 equal to the target
    #12
    new_state = (target, state[1] - (target - state[0]))
    if new_state not in visited and is_valid(new_state):
        print("Rule 12: Pour enough water from jug 2 to jug 1 to make the amount of water in jug 1 equal to the target\n")
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

#else if in python syntax: if condition: statement elif condition: statement else: statement