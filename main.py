"""
This module is the entry point for the application.
"""

from src.display_maze import draw_maze
from src.graph_generation import generate_maze, _generate_maze_kruskal

if __name__ == "__main__":
    print("Hello ACO world!")
    rows, cols = 30, 30
    mst = generate_maze(rows, cols)
    # mst = _generate_maze_kruskal(rows, cols)
    draw_maze(mst, rows, cols, 50)
