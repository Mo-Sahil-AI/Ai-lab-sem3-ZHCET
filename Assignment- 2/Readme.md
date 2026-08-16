# Weighted Graph Pathfinding: All Paths & Least Cost

This project implements an exhaustive pathfinding algorithm in Python. It allows users to dynamically build a weighted graph (including multigraphs with parallel edges) via the command line. Using a Depth-First Search (DFS) backtracking approach, it explores and documents every possible route from a source to a target destination, ultimately calculating the Least Cost Path.

## Features
* **Dynamic Weighted Graphs:** Users can define edges and assign numerical costs (weights) to each path.
* **Multigraph Support:** The adjacency list uses Tuples, allowing multiple parallel paths with different costs between the same two nodes.
* **Exhaustive Backtracking:** Uses a Stack (LIFO) to traverse the graph, actively preventing infinite loops while ensuring 100% of valid paths are explored.
* **Terminal Visualization:** 
  * Prints a complete map of the parsed graph.
  * Explicitly logs every terminal route, classifying them as either a `✅ SUCCESS` or a `🚫 DEAD END`.
* **Least Cost Calculation:** Automatically compares all successful routes and declares the optimal (cheapest) path.
* **Input Validation:** Prevents crashes by verifying that the user's selected Source and Goal nodes actually exist in the parsed graph.

## Files in this Repository
* `main.py`: The core Python script containing the graph builder, validation loops, and the exhaustive traversal algorithm.
* `Instructions.md`: The assignment instructions, constraints, or setup parameters for this project.
* `README.md`: Project documentation.

## How to Run
Execute the script in your terminal:
```bash
python main.py

Example Terminal Output

How many total edges/paths are in the graph? 4
Enter edge 1 (format: Node1 Node2 Cost): A B 10
Enter edge 2 (format: Node1 Node2 Cost): A C 5
Enter edge 3 (format: Node1 Node2 Cost): B D 12
Enter edge 4 (format: Node1 Node2 Cost): C D 15

========================================
--- Complete Graph Map ---
========================================
A connects to: [('B', 10), ('C', 5)]
B connects to: [('A', 10), ('D', 12)]
C connects to: [('A', 5), ('D', 15)]
D connects to: [('B', 12), ('C', 15)]
========================================

Enter the SOURCE node: A
Enter the GOAL node: D

==================================================
--- Finding ALL Paths: A -> D ---
==================================================
✅ SUCCESS (Destination Reached): A -> C -> D (Cost: 20)
✅ SUCCESS (Destination Reached): A -> B -> D (Cost: 22)

==================================================
--- Final Analysis ---
Total successful paths found: 2
🏆 LEAST COST PATH: A -> C -> D | Cost: 20