import itertools
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Example graph representation
GRAPH = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

# Function to draw the graph with current edges


def draw_graph(path=None):
    G = nx.Graph()

    # Add nodes and edges to the graph
    for node in GRAPH:
        for neighbor, cost in GRAPH[node].items():
            G.add_edge(node, neighbor, weight=cost)

    pos = nx.spring_layout(G)  # Layout for the graph visualization

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue',
            node_size=2000, font_size=12, font_weight='bold', edge_color='gray')

    # Highlight the path if provided
    if path:
        edges_in_path = [(path[i], path[i+1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(
            G, pos, edgelist=edges_in_path, edge_color='r', width=2)

    # Display the plot
    plt.title("Graph Visualization with Path (Red Edges)")
    st.pyplot(plt)

# BFS for TSP


def bfs_tsp():
    min_cost = float('inf')
    best_path = None
    start = 'A'

    queue = [(start, [start], 0)]

    while queue:
        node, path, cost = queue.pop(0)

        if len(path) == len(GRAPH):
            cost += GRAPH[path[-1]][start]
            if cost < min_cost:
                min_cost = cost
                best_path = path + [start]
            continue

        for neighbor in GRAPH[node]:
            if neighbor not in path:
                queue.append(
                    (neighbor, path + [neighbor], cost + GRAPH[node][neighbor]))

    draw_graph(best_path)  # Visualize the best path
    st.write(f"Best Path (BFS): {' -> '.join(best_path)} with cost {min_cost}")

# DFS for TSP


def dfs_tsp():
    min_cost = float('inf')
    best_path = None
    start = 'A'

    stack = [(start, [start], 0)]

    while stack:
        node, path, cost = stack.pop()

        if len(path) == len(GRAPH):
            cost += GRAPH[path[-1]][start]
            if cost < min_cost:
                min_cost = cost
                best_path = path + [start]
            continue

        for neighbor in GRAPH[node]:
            if neighbor not in path:
                stack.append(
                    (neighbor, path + [neighbor], cost + GRAPH[node][neighbor]))

    draw_graph(best_path)  # Visualize the best path
    st.write(f"Best Path (DFS): {' -> '.join(best_path)} with cost {min_cost}")

# Streamlit UI


def main():
    st.title("Travelling Salesman Problem (TSP) - BFS & DFS")

    st.sidebar.title("Choose Algorithm")
    choice = st.sidebar.radio(
        "Select an algorithm to solve TSP", ["BFS", "DFS"])

    if choice == "BFS":
        st.subheader("Travelling Salesman Problem using BFS")
        bfs_tsp()
    elif choice == "DFS":
        st.subheader("Travelling Salesman Problem using DFS")
        dfs_tsp()


if __name__ == "__main__":
    main()
