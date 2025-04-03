import streamlit as st
from travelling_salesman import bfs_tsp, dfs_tsp
from tic_tac_toe import play_tic_tac_toe
from water_jug_hill_climbing import water_jug_hill_climb
from puzzle_8_gbfs import solve_8_puzzle_gbfs
from a_star_algorithms import a_star_water_jug, a_star_8_puzzle


def main():
    st.title("Welcome to AI Algorithms Playground")

    st.sidebar.title("Select an Experiment to move forward")
    choice = st.sidebar.radio("Go to:", [
        "Travelling Salesman (DFS & BFS)",
        "Tic Tac Toe",
        "Water Jug (Hill Climbing)",
        "8 Puzzle (Greedy Best First Search)",
        "A* Algorithm (Water Jug & 8 Puzzle)"
    ])

    if choice == "Travelling Salesman (DFS & BFS)":
        st.subheader("Travelling Salesman Problem using DFS & BFS")
        dfs_tsp()
        bfs_tsp()

    elif choice == "Tic Tac Toe":
        st.subheader("Tic Tac Toe Game")
        play_tic_tac_toe()

    elif choice == "Water Jug (Hill Climbing)":
        st.subheader("Water Jug Problem using Hill Climbing")
        water_jug_hill_climb()

    elif choice == "8 Puzzle (Greedy Best First Search)":
        st.subheader("8 Puzzle Problem using Greedy Best First Search")
        solve_8_puzzle_gbfs()

    elif choice == "A* Algorithm (Water Jug & 8 Puzzle)":
        st.subheader("A* Algorithm for Water Jug and 8 Puzzle")
        st.write("Water Jug using A*")
        a_star_water_jug()
        st.write("8 Puzzle using A*")
        a_star_8_puzzle()


if __name__ == "__main__":
    main()
