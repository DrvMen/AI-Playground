# AI-Playground

🔹 Overview
This project provides an interactive GUI-based visualization for various search and problem-solving algorithms using Streamlit. The application visually demonstrates how different algorithms work with step-by-step outputs.

🔹 Implemented Algorithms
The following algorithms are included in this project:

A Algorithm* - Pathfinding algorithm for shortest path computation.

8-Puzzle Solver (Greedy Best First Search) - Solves the 8-puzzle problem using Manhattan Distance heuristic.

Tic-Tac-Toe - A simple two-player game implemented in Streamlit.

Travelling Salesman Problem (TSP) - Uses BFS and DFS to find optimal paths.

Water Jug Problem (Hill Climbing) - Solves the classic water jug problem using a heuristic approach.

🔹 Installation & Setup
To run the project locally, follow these steps:

1️⃣ Install Dependencies
Ensure you have Python installed, then run:

bash
Copy
Edit
pip install streamlit numpy pandas networkx matplotlib
2️⃣ Run the Application
bash
Copy
Edit
streamlit run app.py
This will launch the Streamlit app in your default web browser.

🔹 How It Works
Each algorithm has a dedicated UI in Streamlit where users can:
✔ Input initial problem parameters.
✔ Click "Start" or "Solve" to visualize algorithm steps.
✔ View results dynamically using tables, plots, and graphs.

🔹 Files & Code Structure
app.py - Main Streamlit application entry point.

a_star_algorithms.py - Implementation of the A* algorithm.

puzzle_8_gbfs.py - 8-Puzzle Solver using Greedy Best First Search.

tic_tac_toe.py - Interactive Tic-Tac-Toe game.

travelling_salesman.py - TSP solution using BFS & DFS.

water_jug_hill_climbing.py - Water Jug Problem solver using Hill Climbing.

🔹 Screenshots
You can add images here to showcase different visualizations in the GUI.

🔹 Future Enhancements
🔸 Add more algorithms like Dijkstra’s, Minimax, or Genetic Algorithm.
🔸 Improve UI with animations for better visualization.
🔸 Optimize performance for larger problem instances.

🔹 Contributors
Developed by Dhruv Menon 🎯
