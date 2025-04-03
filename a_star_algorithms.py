import heapq
import streamlit as st
import numpy as np

# A* algorithm utility function for Water Jug Problem


def a_star_water_jug(capacity_x, capacity_y, target):
    # Define the state as a tuple of (x, y) where x is the amount of water in Jug X and y in Jug Y
    start_state = (0, 0)
    goal_state = target

    def heuristic(state):
        return abs(state[0] - goal_state) + abs(state[1] - goal_state)

    def get_possible_moves(state):
        x, y = state
        moves = []
        # Fill Jug X
        moves.append((capacity_x, y))
        # Fill Jug Y
        moves.append((x, capacity_y))
        # Empty Jug X
        moves.append((0, y))
        # Empty Jug Y
        moves.append((x, 0))
        # Pour from Jug X to Jug Y
        pour_x_to_y = min(x, capacity_y - y)
        moves.append((x - pour_x_to_y, y + pour_x_to_y))
        # Pour from Jug Y to Jug X
        pour_y_to_x = min(y, capacity_x - x)
        moves.append((x + pour_y_to_x, y - pour_y_to_x))
        return moves

    open_list = []
    heapq.heappush(open_list, (heuristic(start_state), start_state, []))
    visited = set()

    while open_list:
        _, state, path = heapq.heappop(open_list)
        if state in visited:
            continue
        visited.add(state)
        path.append(state)

        if state[0] == goal_state or state[1] == goal_state:
            return path
        for move in get_possible_moves(state):
            heapq.heappush(open_list, (heuristic(move), move, path.copy()))
    return None

# A* algorithm utility function for 8-Puzzle Problem


def manhattan_distance(state, goal):
    print(f"State is: {state}")
    distance = 0
    for i in range(3):
        for j in range(3):
            current_value = state[i][j]
            if current_value != 0:
                target_x, target_y = divmod(goal.index(current_value), 3)
                distance += abs(i - target_x) + abs(j - target_y)
    return distance


def a_star_8_puzzle(start_state, goal_state):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(
        start_state, goal_state), start_state, []))
    visited = set()

    while open_list:
        _, state, path = heapq.heappop(open_list)
        if tuple(state) in visited:
            continue
        visited.add(tuple(state))
        path = path + [state]

        if state == goal_state:
            return path
        for move in get_possible_moves(state):
            heapq.heappush(
                open_list, (manhattan_distance(move, goal_state), move, path))
    return None

# Streamlit UI for A* Algorithm (Water Jug & 8-Puzzle)


def a_star_water_jug():
    st.title("A* Algorithm for Water Jug Problem")

    capacity_x = st.sidebar.number_input(
        "Capacity of Jug X", min_value=1, value=4)
    capacity_y = st.sidebar.number_input(
        "Capacity of Jug Y", min_value=1, value=3)
    target = st.sidebar.number_input("Target Amount", min_value=1, value=2)

    path = a_star_water_jug(capacity_x, capacity_y, target)

    if path:
        st.write("Path to reach the goal:")
        for step in path:
            st.write(step)
    else:
        st.write("No solution found.")


def a_star_8_puzzle():
    st.title("A* Algorithm for 8-Puzzle Problem")

    start_state = st.text_input(
        "Enter the start state (9 numbers, space separated)", "1 2 3 4 5 6 7 8 0")
    start_state = list(map(int, start_state.split()))
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    if len(start_state) != 9:
        st.write("Invalid input. Please enter exactly 9 numbers.")
        return

    path = a_star_8_puzzle(start_state, goal_state)

    if path:
        st.write("Steps to solve the puzzle:")
        for step in path:
            st.write(np.array(step).reshape(3, 3))
    else:
        st.write("No solution found.")
