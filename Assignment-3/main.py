def dfs_with_limit(graph, source, goal, limit):
    # Stack stores: (current_node, path_history_list, current_depth)
    stack = [(source, [source], 0)]
    
    # Flag to check if we need to keep increasing the threshold later
    nodes_remaining_beyond_limit = False

    while stack:
        # 1. Pop the last item (LIFO)
        current_node, current_path, current_depth = stack.pop()

        # 2. Show the intermediate steps/path sequentially on every visit
        print(f"  -> Visiting: {current_node} | Path taken: {' -> '.join(current_path)}")

        # 3. Check for the goal
        if current_node == goal:
            print(f"\n✅ SUCCESS! Final Traversal Path: {' -> '.join(current_path)}")
            return True, False # Goal found, no need to check remaining nodes

        # 4. Explore neighbors if within the threshold limit
        if current_depth < limit:
            # We reverse the neighbors simply so the stack pops them in the order they were entered
            for neighbor in reversed(graph.get(current_node, [])):
                if neighbor not in current_path:
                    new_path = current_path + [neighbor]
                    stack.append((neighbor, new_path, current_depth + 1))
        else:
            # If we hit the limit ceiling, check if any unvisited neighbors exist deeper down
            for neighbor in graph.get(current_node, []):
                if neighbor not in current_path:
                    nodes_remaining_beyond_limit = True
                    break

    # If the stack empties and we didn't find the goal
    return False, nodes_remaining_beyond_limit


def iddfs(graph, source, goal):
    threshold = 0
    
    print("\n" + "="*50)
    print(f"--- Starting IDDFS: {source} -> {goal} ---")
    print("="*50)

    while True:
        print(f"\n=== Testing Threshold Limit: {threshold} ===")
        
        goal_found, nodes_remaining = dfs_with_limit(graph, source, goal, threshold)
        
        if goal_found:
            break # Stop the while loop, we won!
            
        if not nodes_remaining:
            # If no nodes exist beyond our limit, expanding the limit won't help.
            print(f"\n🚫 ERROR: Entire graph explored. No path exists between '{source}' and '{goal}'.")
            break
            
        # Increase the threshold for the next iteration
        threshold += 1


# ==========================================
# --- USER INPUT & GRAPH BUILDING AREA ---
# ==========================================
if __name__ == "__main__":
    graph = {}
    num_edges = int(input("How many total edges are in the graph? "))
    
    for i in range(num_edges):
        user_input = input(f"Enter edge {i+1} (format: Node1 Node2): ")
        u, v = user_input.split()
        
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
            
        # Creating an undirected graph (two-way connections)
        graph[u].append(v)
        graph[v].append(u)
    
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
    
    # Run the Iterative Deepening Search
    iddfs(graph, source_node, goal_node)