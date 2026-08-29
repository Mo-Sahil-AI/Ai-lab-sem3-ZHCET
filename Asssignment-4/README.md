# Best First Search vs. Beam Search Implementation

## 📌 Project Overview
This Python project implements and compares two informed search algorithms: **Best First Search (Greedy)** and **Beam Search**. It dynamically accepts user input to build a graph (or tree), takes heuristic values for each node, and outputs a step-by-step trace of how each algorithm navigates the state space to find a goal.

This project was built to explicitly demonstrate the behavioral and memory differences between a global heuristic search and a memory-constrained local search.

## 🧠 Algorithm Breakdown

### 1. Best First Search (Greedy)
* **Mechanic:** Uses a global **Priority Queue** (`heapq`). It evaluates all known, unvisited nodes and always expands the one with the lowest absolute heuristic score.
* **Memory:** High. It hoards every node it discovers in memory.
* **Behavior:** It can easily "jump backward" to an earlier branch if its current path hits a dead end or bad heuristic values. It will eventually find the goal if one exists.

### 2. Beam Search
* **Mechanic:** Operates strictly level-by-level. It expands the current candidates, sorts the resulting neighbors by heuristic score, and executes a **Beam Slice**—keeping only the top `N` candidates (where `N` is the Beam Width) and permanently deleting the rest.
* **Memory:** Extremely low and strictly capped based on the defined beam width. 
* **Behavior:** It cannot jump backward. Because it permanently discards nodes that look temporarily bad, it is incomplete and can fail to find a reachable goal if the optimal path is deleted early on.

## ⚙️ Features
* **Dynamic Graph Building:** Users can toggle whether the input graph is **Directed** (one-way, standard for state-space AI trees) or **Undirected** (two-way, standard for physical maps).
* **Step-by-Step Tracing:** Prints the exact node evaluation sequence, current memory state, and path history at every step.
* **Performance Summary:** Automatically calculates and displays the final **Path Length** and **Total Nodes Evaluated** for direct efficiency comparison between the two algorithms.

## 🚀 How to Run
Run the script using Python 3:
```bash
python main.py


### 1. The Input & Setup Algorithm

The input phase is responsible for translating the user's terminal commands into mathematical data structures that the algorithms can navigate.

* **Graph Representation (Adjacency List):** The code uses a Python dictionary to represent the graph. In an adjacency list, each node is a "key," and its "value" is a list of all nodes it directly connects to (e.g., `{'A': ['B', 'C']}`). This is vastly more memory-efficient than a 2D matrix, especially for sparsely connected graphs.
* **Directed vs. Undirected Logic:**
* If the user selects a **Directed Graph**, the algorithm reads an edge from `u` to `v` and executes `graph[u].append(v)`. This creates a strictly one-way path.
* If the user selects an **Undirected Graph**, the algorithm executes both `graph[u].append(v)` and `graph[v].append(u)`, allowing traversal in both directions.


* **The Heuristic Map:** The algorithm collects every unique node entered by the user using a mathematical `set()` (which automatically prevents duplicates). It then prompts the user for a numerical value for each node and maps them in a separate dictionary (e.g., `heuristics = {'S': 10, 'A': 2, 'G': 0}`). This dictionary acts as the "radar" the algorithms use to make decisions.

---

### 2. Best First Search (Greedy Best-First Search)

Best First Search is an informed search algorithm that selects the next path to explore based strictly on which node has the lowest heuristic score out of *all* available options currently known to the algorithm.

* **Core Data Structure:** It relies on a **Priority Queue** (implemented via Python's `heapq` module as a Min-Heap). A Min-Heap automatically re-sorts its internal data so that the element with the lowest numerical value is always at index 0.
* **Execution Flow:**
1. **Initialization:** The Source node is pushed into the Priority Queue along with its heuristic value.
2. **Selection:** The algorithm pops the node with the lowest heuristic value from the global queue.
3. **Goal Check:** If the popped node is the goal, the search terminates.
4. **Expansion:** If not, the algorithm marks the node as `visited` (to prevent infinite loops) and looks at its neighbors.
5. **Queueing:** Every unvisited neighbor is pushed into the Priority Queue. The queue instantly re-sorts itself, guaranteeing the next loop iteration will evaluate the absolute best option available anywhere on the map.


* **Properties:**
* **Space Complexity:** $O(b^m)$ (where $b$ is the branching factor and $m$ is the maximum depth). It stores every generated node in memory.
* **Time Complexity:** $O(b^m)$ in the worst case, though a good heuristic dramatically reduces this.
* **Completeness:** It is **Complete** (it will eventually find the goal if one exists) as long as it keeps track of visited nodes to avoid cyclic loops.
* **Optimality:** It is **Not Optimal**. Because it ignores the actual cost of edges traversed, it can find a longer, more expensive path simply because the heuristic looked favorable at the time.



---

### 3. Beam Search

Beam Search is a highly memory-optimized adaptation of Breadth-First Search (BFS). Instead of evaluating options globally, it searches strictly level-by-level (depth 1, then depth 2, etc.), forcibly limiting how many nodes it remembers at each level.

* **Core Data Structure:** It uses standard arrays/lists. The main array is called the **Beam**, and its maximum size is strictly governed by an integer called the `beam_width` (denoted as $W$).
* **Execution Flow:**
1. **Initialization:** The Source node is placed into the Beam array.
2. **Level Expansion:** The algorithm iterates through *every* node currently surviving in the Beam and generates all of their valid neighbors.
3. **Aggregation:** All of these new neighbors are dumped into a temporary list called `next_level_candidates`.
4. **Sorting & Pruning (The Beam Slice):** The `next_level_candidates` list is sorted mathematically by heuristic scores. The algorithm then slices this list, keeping only the top $W$ candidates.
5. **Overwrite:** The algorithm permanently overwrites the old Beam array with these top $W$ candidates. All other discovered nodes are instantly deleted from memory. The loop repeats for the next level.


* **Properties:**
* **Space Complexity:** $O(W \cdot m)$ (where $W$ is beam width and $m$ is depth). Because it deletes unselected nodes at every level, its memory footprint remains incredibly small and stable, never exceeding the defined width.
* **Time Complexity:** $O(W \cdot b \cdot m)$. It only ever evaluates the neighbors of the $W$ nodes that survived the slice.
* **Completeness:** It is **Incomplete**. If the only valid path to the goal relies on a node that has a temporarily poor heuristic score, Beam Search will delete it during the pruning phase and fail to find the goal.
* **Optimality:** It is **Not Optimal**. It suffers from the same greedy heuristic bias as Best First Search, compounded by the fact that it permanently throws away potential alternative routes.