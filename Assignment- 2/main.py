def find_all_paths_and_least_cost(graph, source, goal):
    print("\n" + "="*50)
    print(f"--- Finding ALL Paths: {source} -> {goal} ---")
    print("="*50)
    
    # Stack stores: (current_node, path_so_far, cost_so_far)
    stack = [(source, [source], 0)]
    all_completed_paths = []
    
    while stack:
        # Pop the last item (LIFO)
        current_node, current_path, current_cost = stack.pop()
        
        # Check if we hit the goal
        if current_node == goal:
            print(f"✅ SUCCESS (Destination Reached): {' -> '.join(current_path)} (Cost: {current_cost})")
            all_completed_paths.append((current_path, current_cost))
            continue 

        # Explore neighbors
        is_dead_end = True 
        
        for neighbor, edge_cost in graph.get(current_node, []):
            if neighbor not in current_path:
                is_dead_end = False # Found a valid place to go
                
                new_path = current_path + [neighbor]
                new_cost = current_cost + edge_cost
                stack.append((neighbor, new_path, new_cost))
                
        # Check for Dead End
        if is_dead_end:
            print(f"🚫 DEAD END (Cannot Proceed): {' -> '.join(current_path)} (Cost: {current_cost})")

    # --- Phase 2: Declare the Winner ---
    print("\n" + "="*50)
    print("--- Final Analysis ---")
    
    if not all_completed_paths:
        print(f"No paths exist between '{source}' and '{goal}'.")
        return

    # Find the path with the minimum cost from our master list
    least_cost_path, lowest_cost = min(all_completed_paths, key=lambda x: x[1])
    
    print(f"Total successful paths found: {len(all_completed_paths)}")
    print(f"🏆 LEAST COST PATH: {' -> '.join(least_cost_path)} | Cost: {lowest_cost}")


# ==========================================
# --- USER INPUT & GRAPH BUILDING AREA ---
# ==========================================

graph = {}
num_edges = int(input("How many total edges/paths are in the graph? "))

for i in range(num_edges):
    user_input = input(f"Enter edge {i+1} (format: Node1 Node2 Cost): ")
    u, v, cost_string = user_input.split()
    cost = int(cost_string)
    
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
        
    # Append the tuple. This allows multiple paths between the same two nodes!
    graph[u].append((v, cost))
    graph[v].append((u, cost))

# --- UPDATED: Show the complete graph structure to the user ---
print("\n" + "="*40)
print("--- Complete Graph Map ---")
print("="*40)
for node, connections in graph.items():
    # Formatting it nicely so it's easy to read the tuples
    print(f"{node} connects to: {connections}")
print("="*40)

# Safely get the Source Node
while True:
    source_node = input("\nEnter the SOURCE node: ")
    if source_node in graph:
        break
    print(f"Error: '{source_node}' does not exist. Valid nodes are: {list(graph.keys())}")

# Safely get the Goal Node
while True:
    goal_node = input("Enter the GOAL node: ")
    if goal_node in graph:
        break
    print(f"Error: '{goal_node}' does not exist. Valid nodes are: {list(graph.keys())}")

# Run the algorithm
find_all_paths_and_least_cost(graph, source_node, goal_node)