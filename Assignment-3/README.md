# Iterative Deepening Depth-First Search (IDDFS)

This project implements the **Iterative Deepening Depth-First Search (IDDFS)** algorithm in Python. It allows users to dynamically build an undirected graph via the command line and actively visualize the algorithm's step-by-step search process.

## Algorithm Overview

IDDFS is a clever hybrid graph traversal algorithm that combines the best characteristics of two standard searches:
1. **The Shortest-Path Guarantee of BFS:** Like Breadth-First Search (BFS), it explores the graph level-by-level. This ensures that the first time it finds the goal, it is mathematically guaranteed to be the shortest path (fewest edges).
2. **The Memory Efficiency of DFS:** Like Depth-First Search (DFS), it only stores the single path currently being evaluated in memory (using a Stack). This avoids the massive memory bloat that often causes BFS to crash on extremely large graphs.

## How It Works: The 3 Core Mechanics

This script breaks the algorithm down into three interacting parts:

### 1. The Iterative Threshold (The Outer Loop)
The algorithm does not attempt to search the entire graph at once. Instead, it places a strict "depth limit" (or threshold) on the search. 
* It starts with a limit of `0`.
* If the target is not found within `0` steps, it wipes the slate clean, increases the limit to `1`, and restarts the search from the beginning.
* It loops continually, exploring exactly one level deeper on each iteration.

### 2. The Depth-Limited Search (The Inner Engine)
Inside each iteration, a standard DFS runs, but with a strict constraint: **it cannot explore past the current threshold.** 
* As it visits nodes, it tracks the `current_depth` of the path. 
* If `current_depth` equals the threshold limit, the algorithm treats that node as a temporary dead end. It refuses to add its neighbors to the stack, forcing the DFS to backtrack and explore other valid paths within the allowed limit.

### 3. The Infinite-Loop Safety Net
To prevent the algorithm from increasing the threshold forever if a destination is unreachable (e.g., in a disconnected graph), the engine uses a flag called `nodes_remaining_beyond_limit`. 
* When the DFS hits the depth ceiling, it peeks at the unvisited neighbors. If there are valid nodes just out of reach, it flags that expanding the limit on the next iteration is worth it. 
* If the DFS finishes exploring and this flag remains `False`, the algorithm mathematically knows the entire graph has been mapped, the goal does not exist, and it safely shuts down the program.

## How to Run
Execute the script in your terminal:
```bash
python main.py