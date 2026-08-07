# 1. Create an empty dictionary to hold the graph
graph = {}

# 2. Ask the user for the total number of connections (edges)
num_edges = int(input("How many total edges/paths are in the graph? "))

# 3. Loop to collect each edge
for i in range(num_edges):
    user_input = input(f"Enter edge {i+1} (format: Node1 Node2): ")
    u, v = user_input.split()
    
    # 4. Initialize Node1 in the graph if it doesn't exist
    if u not in graph:
        graph[u] = {} # Now using an empty dictionary instead of a list
        
    # 5. Initialize Node2 in the graph if it doesn't exist
    if v not in graph:
        graph[v] = {}
        
    # 6. Add or update the path count from u to v
    if v in graph[u]:
        graph[u][v] += 1  # A path already exists, add another one
    else:
        graph[u][v] = 1   # This is the first path discovered
        
    # 7. Add or update the path count from v to u (Two-way street)
    if u in graph[v]:
        graph[v][u] += 1
    else:
        graph[v][u] = 1

# 8. Display the graph so the number of paths can be clearly seen
print("\n--- Graph Map (Node: {Neighbor: Path_Count}) ---")
for node, connections in graph.items():
    print(f"{node} is connected to: {connections}")

# 1. Start an infinite loop that only breaks when valid input is given
while True:
    # 2. Ask the user for the source node
    source_node = input("\nEnter the source node to start traversal: ")
    
    # 3. Check if the node actually exists in our graph dictionary
    if source_node in graph:
        print(f"Success! Starting algorithms from node: {source_node}")
        break  # Exit the loop, the input is safe to use!
    else:
        # 4. If they type a typo, warn them and let the loop run again
        print(f"Error: '{source_node}' does not exist in the graph. Valid nodes are: {list(graph.keys())}")


def bfs_traversal(graph, source_node):
    print("\n" + "="*40)
    print("--- Starting BFS (Queue / FIFO) ---")
    print("="*40)
    
    # Initialize the Queue and Visited list with the source node
    queue = [source_node]
    visited = []
    
    step = 1
    while queue:
        print(f"\nStep {step}:")
        print(f"  Queue contents : {queue}")
        print(f"  Visited so far : {visited}")
        
        # Pop the FIRST element from the queue (FIFO behavior)
        current = queue.pop(0)
        visited.append(current)
        print(f"  -> Popped & processing node: {current}")
        
        # Checking current node's neighbors
        for neighbor in graph[current]:
            # If the neighbor hasn't been visited, mark it and add to queue
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                print(f"Found unvisited neighbor '{neighbor}'. Adding to Queue.")
                
        step += 1

    # Print the final path
    print("-" * 40)
    print(f"FINAL BFS PATH: {' -> '.join(visited)}")


def dfs_traversal(graph, source_node):
    print("\n" + "="*40)
    print("--- Starting DFS (Stack / LIFO) ---")
    print("="*40)
    
    # Initialize the Stack with the source node, but Visited starts empty
    stack = [source_node]
    visited = []
    
    step = 1
    while stack:
        print(f"\nStep {step}:")
        print(f"  Stack contents : {stack}")
        print(f"  Visited so far : {visited}")
        
        # Pop the LAST element from the stack (LIFO behavior)
        current = stack.pop()
        print(f"  -> Popped & processing node: {current}")
        visited.append(current)
        # Because stacks can accidentally store duplicates if a node is a neighbor 
        # to multiple nodes, we must check if it's visited AFTER popping
        # Get neighbors. We reverse them so the first neighbor is on top of the stack.
        neighbors = list(graph[current].keys())
        for neighbor in reversed(neighbors):
                if neighbor not in visited and neighbor not in stack:
                    stack.append(neighbor)
                    print(f"Pushing unvisited neighbor '{neighbor}' to Stack.")
        step += 1
 
    # Print the final path
    print("-" * 40)
    print(f"FINAL DFS PATH: {' -> '.join(visited)}")

    # At the very end, compare the visited list to the graph dictionary
    if len(visited) < len(graph):
        unvisited_nodes = set(graph.keys()) - set(visited)
        print(f"\n[!] Note: The graph is disconnected. The nodes {unvisited_nodes} could not be reached from source node '{source_node}'itself.")
