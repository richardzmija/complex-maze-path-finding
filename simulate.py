#!/usr/bin/env python
"""
This module is the entry point for the application.
"""

from src.path_finding import AntColonyOptimization
from src.evaluation import compare_with_dijkstra
from src.graph_generation import generate_maze
from src.graph_utils import convert_grid_to_graph, node_tuple_to_int
from networkx import write_gexf  # type: ignore


if __name__ == "__main__":
    ROWS = 10
    COLS = 10
    CELL_SIZE = 40
    ITERATIONS = 3

    maze = generate_maze(ROWS, COLS)
    graph = convert_grid_to_graph(maze)
    write_gexf(maze, "data/maze.gexf")
    write_gexf(graph, "data/graph.gexf")

    aco = AntColonyOptimization(
        graph,
        n_ants=100,
        n_best=3,
        n_iterations=ITERATIONS,
        filename="data/aco_state.jsonl",
        decay=0.5,
        alpha=1,
        beta=1,
    )

    upper_right_corner = node_tuple_to_int((0, COLS - 1), COLS)
    lower_left_corner = node_tuple_to_int((ROWS - 1, 0), COLS)

    aco_path, dijkstra_path = compare_with_dijkstra(
        graph, lower_left_corner, upper_right_corner, aco
    )