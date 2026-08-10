# Graph Traversal: BFS & DFS with Step-by-Step Visualization

A Python program that builds an undirected graph from user input and traverses it using both **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**, printing every intermediate step so the underlying queue/stack behavior is visible.

## Features

- **Interactive graph input** — build any graph by entering the number of edges and each connection.
- **Custom source node selection** — with input validation (re-prompts on invalid/typo'd node names).
- **BFS using an explicit queue** (FIFO, Python list with `pop(0)`).
- **DFS using an explicit stack** (LIFO, Python list with `pop()`).
- **Step-by-step trace** — at every iteration, the current queue/stack and visited list are printed before the next node is processed.
- **Final traversal path** printed for both algorithms.
- **Disconnected graph detection** — warns if any nodes were unreachable from the chosen source.

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

```bash
python main.py
```

## Usage Walkthrough

### 1. Build the Graph

You'll first be asked how many edges the graph has, then asked to enter each one:

```
How many total edges/paths are in the graph? 3
Enter edge 1 (format: Node1 Node2): A B
Enter edge 2 (format: Node1 Node2): B C
Enter edge 3 (format: Node1 Node2): A C
```

The graph is stored internally as an **adjacency dictionary of dictionaries**:

```python
graph = {
    "A": {"B": 1, "C": 1},
    "B": {"A": 1, "C": 1},
    "C": {"B": 1, "A": 1}
}
```

- Each node maps to its neighbors.
- Each neighbor's value is a **count**, tracking how many times that edge was entered (supports parallel/duplicate edges between the same pair of nodes).
- Edges are treated as **undirected** — entering `A B` connects `A → B` and `B → A`.

The program then prints the full adjacency map:

```
--- Graph Map (Node: {Neighbor: Path_Count}) ---
A is connected to: {'B': 1, 'C': 1}
B is connected to: {'A': 1, 'C': 1}
C is connected to: {'B': 1, 'A': 1}
```

### 2. Choose a Source Node

```
Enter the source node to start traversal: A
Success! Starting algorithms from node: A
```

If you enter a node that doesn't exist in the graph, you'll see an error and be re-prompted:

```
Error: 'Z' does not exist in the graph. Valid nodes are: ['A', 'B', 'C']
```

### 3. BFS Traversal (Queue)

`bfs_traversal(graph, source_node)` explores the graph level by level:

- Starts with `queue = [source_node]` and an empty `visited` list.
- On each step, prints the current queue and visited list, then **pops from the front** (`queue.pop(0)`) to process the next node.
- Any unvisited neighbor not already queued is appended to the back of the queue.
- Continues until the queue is empty, then prints the final visited order as the BFS path.

### 4. DFS Traversal (Stack)

`dfs_traversal(graph, source_node)` explores as deep as possible before backtracking:

- Starts with `stack = [source_node]` and an empty `visited` list.
- On each step, prints the current stack and visited list, then **pops from the top** (`stack.pop()`) to process the next node.
- Neighbors are pushed in reverse order so that the first neighbor ends up on top of the stack (visited first).
- Continues until the stack is empty, then prints the final visited order as the DFS path.

### 5. Disconnected Graphs

After each traversal, the program compares the number of visited nodes to the total node count. If some nodes were never reached, it reports them:

```
[!] Note: The graph is disconnected. The nodes {'D'} could not be reached from source node 'A'.
```

## Example Session

```
How many total edges/paths are in the graph? 4
Enter edge 1 (format: Node1 Node2): A B
Enter edge 2 (format: Node1 Node2): A C
Enter edge 3 (format: Node1 Node2): B D
Enter edge 4 (format: Node1 Node2): C D

--- Graph Map (Node: {Neighbor: Path_Count}) ---
A is connected to: {'B': 1, 'C': 1}
B is connected to: {'A': 1, 'D': 1}
C is connected to: {'A': 1, 'D': 1}
D is connected to: {'B': 1, 'C': 1}

Enter the source node to start traversal: A
Success! Starting algorithms from node: A

========================================
--- Starting BFS (Queue / FIFO) ---
========================================

Step 1:
  Queue contents : ['A']
  Visited so far : []
  -> Popped & processing node: A
Found unvisited neighbor 'B'. Adding to Queue.
Found unvisited neighbor 'C'. Adding to Queue.

Step 2:
  Queue contents : ['B', 'C']
  Visited so far : ['A']
  -> Popped & processing node: B
Found unvisited neighbor 'D'. Adding to Queue.

Step 3:
  Queue contents : ['C', 'D']
  Visited so far : ['A', 'B']
  -> Popped & processing node: C

Step 4:
  Queue contents : ['D']
  Visited so far : ['A', 'B', 'C']
  -> Popped & processing node: D
----------------------------------------
FINAL BFS PATH: A -> B -> C -> D
```

*(DFS output follows the same style, using the stack instead of the queue.)*

## Project Structure

```
.
├── main.py         # Graph builder + BFS/DFS traversal logic
├── instructions.md # Assignment requirements
└── README.md        # This file
```
