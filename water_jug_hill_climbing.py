import streamlit as st
import matplotlib.pyplot as plt


class WaterJug:
    def __init__(self, capacity_x, capacity_y, target):
        self.capacity_x = capacity_x
        self.capacity_y = capacity_y
        self.target = target
        self.current_x = 0
        self.current_y = 0

    def is_goal_state(self):
        return self.current_x == self.target or self.current_y == self.target

    def get_possible_moves(self):
        moves = [
            (self.capacity_x, self.current_y),  # Fill Jug X
            (self.current_x, self.capacity_y),  # Fill Jug Y
            (0, self.current_y),                # Empty Jug X
            (self.current_x, 0),                # Empty Jug Y
            # Pour from Jug X to Jug Y
            (self.current_x - min(self.current_x, self.capacity_y - self.current_y),
             self.current_y + min(self.current_x, self.capacity_y - self.current_y)),
            # Pour from Jug Y to Jug X
            (self.current_x + min(self.current_y, self.capacity_x - self.current_x),
             self.current_y - min(self.current_y, self.capacity_x - self.current_x))
        ]
        return moves

    def heuristic(self, state):
        x, y = state
        return abs(self.target - x) + abs(self.target - y)

    def hill_climbing(self):
        visited = set()
        current_state = (self.current_x, self.current_y)
        path = [current_state]

        while not self.is_goal_state():
            visited.add(current_state)
            possible_moves = self.get_possible_moves()
            next_move = None
            min_heuristic = float('inf')
            for move in possible_moves:
                if move not in visited:
                    h = self.heuristic(move)
                    if h < min_heuristic:
                        min_heuristic = h
                        next_move = move
            if next_move is None:
                return None
            self.current_x, self.current_y = next_move
            current_state = next_move
            path.append(current_state)
            if self.is_goal_state():
                return path
        return None


def draw_jugs(current_x, current_y, capacity_x, capacity_y):
    fig, ax = plt.subplots(figsize=(4, 6))
    ax.bar(["Jug X", "Jug Y"], [current_x, current_y],
           color=['blue', 'red'], alpha=0.6)
    ax.set_ylim(0, max(capacity_x, capacity_y))
    ax.set_ylabel("Water Level")
    ax.set_title("Water Jug Levels")
    st.pyplot(fig)


def water_jug_hill_climb():
    st.title("Water Jug Problem (Hill Climbing)")
    st.sidebar.header("Input Parameters")
    capacity_x = st.sidebar.number_input(
        "Capacity of Jug X", min_value=1, value=4)
    capacity_y = st.sidebar.number_input(
        "Capacity of Jug Y", min_value=1, value=3)
    target = st.sidebar.number_input("Target Amount", min_value=1, value=2)

    if 'step' not in st.session_state:
        st.session_state.step = 0
        st.session_state.path = []

    if st.button("Start" if st.session_state.step == 0 else "Next Step"):
        if st.session_state.step == 0:
            problem = WaterJug(capacity_x, capacity_y, target)
            path = problem.hill_climbing()
            if path:
                st.session_state.path = path
                st.session_state.step = 1
            else:
                st.error("No solution found")
        else:
            st.session_state.step += 1
            if st.session_state.step > len(st.session_state.path):
                st.success("Goal reached!")
                st.session_state.step = 0

    if st.session_state.step > 0 and st.session_state.step <= len(st.session_state.path):
        current_x, current_y = st.session_state.path[st.session_state.step - 1]
        draw_jugs(current_x, current_y, capacity_x, capacity_y)
        st.write(
            f"Step {st.session_state.step}: Jug X = {current_x}, Jug Y = {current_y}")


if __name__ == "__main__":
    water_jug_hill_climb()
