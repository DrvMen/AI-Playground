import streamlit as st
import numpy as np
import pandas as pd
import heapq

# Utility function to calculate heuristic (Manhattan Distance)


def manhattan_distance(state, goal):
    distance = 0
    for i in range(9):  # Treat state as a flat list
        if state[i] != 0:
            target_idx = goal.index(state[i])
            x, y = divmod(i, 3)
            target_x, target_y = divmod(target_idx, 3)
            distance += abs(x - target_x) + abs(y - target_y)
    return distance

# 8-Puzzle Problem using Greedy Best First Search


class Puzzle8:
    def __init__(self, start_state, goal_state):
        self.start_state = tuple(start_state)  # Ensure immutable
        self.goal_state = tuple(goal_state)  # Ensure immutable
        self.empty_tile = 0
        self.visited = set()

    def get_possible_moves(self, state):
        moves = []
        state = list(state)  # Convert tuple back to list for manipulation
        idx = state.index(self.empty_tile)
        x, y = divmod(idx, 3)

        # Define possible directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = state[:]
                new_idx = nx * 3 + ny
                new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
                moves.append(tuple(new_state))  # Store as tuple to be hashable
        return moves

    def greedy_best_first_search(self):
        priority_queue = []
        heapq.heappush(priority_queue, (manhattan_distance(
            self.start_state, self.goal_state), self.start_state, []))

        while priority_queue:
            _, state, path = heapq.heappop(priority_queue)
            if state in self.visited:
                continue
            self.visited.add(state)
            path = path + [state]

            if state == self.goal_state:
                return path
            for move in self.get_possible_moves(state):
                heapq.heappush(priority_queue, (manhattan_distance(
                    move, self.goal_state), move, path))
        return None

# Streamlit UI for solving 8-Puzzle using GBFS


def solve_8_puzzle_gbfs():
    st.title("8-Puzzle Problem (Greedy Best First Search)")

    start_state = st.text_input(
        "Enter the start state (9 numbers, space separated)", "1 2 3 4 5 6 7 8 0")
    start_state = list(map(int, start_state.split()))
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    if len(start_state) != 9:
        st.write("Invalid input. Please enter exactly 9 numbers.")
        return

    puzzle = Puzzle8(start_state, goal_state)
    solution = puzzle.greedy_best_first_search()

    if solution:
        st.write("Steps to solve the puzzle:")
        for step in solution:
            # Convert the state to a DataFrame for better visualization
            df = pd.DataFrame(np.array(step).reshape(3, 3))
            st.table(df)
    else:
        st.write("No solution found.")


# Run the Streamlit app
if __name__ == "__main__":
    solve_8_puzzle_gbfs()
