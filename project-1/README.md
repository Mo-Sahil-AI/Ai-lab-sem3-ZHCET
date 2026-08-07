# Graph Traversal in Python: BFS & DFS

This project implements Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms in Python. It allows users to dynamically build a graph or tree via the command line and visualizes the step-by-step logic of how Stacks and Queues process the data.

## Features
* **Dynamic Graph Building:** Users can define the number of edges and input custom node connections to build an adjacency list dynamically.
* **Path Counting:** The data structure tracks and displays the number of paths between connected nodes.
* **Input Validation:** Includes error-handling to ensure the user selects a valid starting source node before traversal begins.
* **Step-by-Step Visualization:** Prints the exact, real-time state of the Stack/Queue and Visited lists at every step of the traversal.
* **Disconnected Graph Detection:** Strictly adheres to single-source traversal constraints while intelligently warning the user if any unreachable "islands" (disconnected nodes) exist in the graph.

## Files in this Repository
* `main.py`: The core Python script containing the graph builder and traversal logic.
* `instructions.md`: The original assignment instructions and constraints.
* `README.md`: Project documentation.

## How to Run
Execute the script in your terminal:
```bash
python main.py