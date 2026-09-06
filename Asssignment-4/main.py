import heapq

def best_first_search(graph, heuristics, source, goal):
    """
    Executes a Greedy Best First Search.
    Uses a priority queue to always expand the node with the lowest heuristic score globally.
    """
    print("\n" + "="*50)
    print(f"--- Starting Best First Search (Greedy) ---")
    print("="*50)
    
    # Priority Queue stores: (heuristic_value, current_node, path_so_far)
    pq = [(heuristics[source], source, [source])]
    visited = set()
    step = 1
    nodes_evaluated = 0
    
    while pq:
        # Pop the node with the lowest heuristic value
        current_h, current_node, path = heapq.heappop(pq)
        nodes_evaluated += 1
        
        print(f"Step {step}: Evaluated '{current_node}' (h={current_h}) | Path: {' -> '.join(path)}")
        
        if current_node == goal:
            print(f"\n  ✅ GOAL REACHED!")
            print(f"🏆 Final Path: {' -> '.join(path)}")
            
            # Performance Summary
            print("-" * 35)
            print("📊 BEST FIRST SEARCH PERFORMANCE:")
            print(f"   • Path Length (Steps): {len(path) - 1}")
            print(f"   • Total Nodes Evaluated: {nodes_evaluated}")
            print("-" * 35 + "\n")
            return
            
        if current_node not in visited:
            visited.add(current_node)
            
            # Explore neighbors
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    heapq.heappush(pq, (heuristics[neighbor], neighbor, new_path))
        step += 1
        
    print(f"\n🚫 ERROR: Goal '{goal}' is unreachable.")


def beam_search(graph, heuristics, source, goal, beam_width):
    """
    Executes a Beam Search.
    Searches level-by-level, keeping only the top 'beam_width' candidates to save memory.
    """
    print("\n" + "="*50)
    print(f"--- Starting Beam Search (Width = {beam_width}) ---")
    print("="*50)
    
    # Beam stores a list of tuples: (heuristic_value, current_node, path_so_far)
    beam = [(heuristics[source], source, [source])]
    step = 1
    nodes_evaluated = 0
    
    while beam:
        print(f"\nStep {step} | Current Beam Candidates: {[n[1] for n in beam]}")
        next_level_candidates = []
        
        # 1. Expand all nodes currently surviving in the beam
        for current_h, current_node, path in beam:
            nodes_evaluated += 1
            print(f"  -> Expanding: '{current_node}'")
            
            if current_node == goal:
                print(f"\n  ✅ GOAL REACHED!")
                print(f"🏆 Final Path: {' -> '.join(path)}")
                
                # Performance Summary
                print("-" * 35)
                print("📊 BEAM SEARCH PERFORMANCE:")
                print(f"   • Path Length (Steps): {len(path) - 1}")
                print(f"   • Total Nodes Evaluated: {nodes_evaluated}")
                print("-" * 35 + "\n")
                return
                
            # Generate all possible next moves for this node
            neighbours= graph.get(current_node, []).reverse()
            while(neighbours) :
                neighbor=neighbours.pop()
                if neighbor not in path: # Prevent immediate backtracking
                    new_path = path + [neighbor]
                    next_level_candidates.append((heuristics[neighbor], neighbor, new_path))
                    
        # 2. Sort all generated candidates globally by their heuristic value (lowest is best)
        next_level_candidates.sort(key=lambda x: x[0])
        
        # 3. The Beam Slice: Keep ONLY the top 'beam_width' candidates
        beam = next_level_candidates[:beam_width]
        
        if not beam:
            break # Dead end reached
            
        print(f"  ✂️  Beam sliced. Keeping top {beam_width}: {[n[1] for n in beam]}")
        step += 1
        
    print(f"\n🚫 ERROR: Goal '{goal}' is unreachable with a beam width of {beam_width}.")


# ==========================================
# --- USER INPUT & SETUP AREA ---
# ==========================================
if __name__ == "__main__":
    graph = {}
    nodes_set = set()
    
    num_edges = int(input("How many edges are in the graph? "))
    
    # Check for Directed vs Undirected
    graph_type = input("Is this a Directed graph? (y/n): ").strip().lower()
    is_directed = (graph_type == 'y')
    
    print("\nEnter edges (format: Node1 Node2):")
    for i in range(num_edges):
        u, v = input(f"  Edge {i+1}: ").split()
        
        # Ensure nodes exist in dictionary
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
            
        # Always add the forward path
        graph[u].append(v)
        
        # If undirected (two-way), add the reverse path automatically
        if not is_directed:
            graph[v].append(u)
            
        nodes_set.update([u, v])
        
    print("\n--- Enter Heuristic Values (h-values) ---")
    print("*(Lower numbers mean the node is estimated to be closer to the goal)*")
    heuristics = {}
    for node in nodes_set:
        heuristics[node] = int(input(f"  Heuristic for Node '{node}': "))
        
    # Safely get the Source Node
    while True:
        source_node = input("\nEnter the SOURCE node: ")
        if source_node in nodes_set:
            break
        print(f"Error: '{source_node}' does not exist. Valid nodes are: {list(nodes_set)}")
        
    # Safely get the Goal Node
    while True:
        goal_node = input("Enter the GOAL node: ")
        if goal_node in nodes_set:
            break
        print(f"Error: '{goal_node}' does not exist. Valid nodes are: {list(nodes_set)}")
        
    beam_w = int(input("Enter the Beam Width limit (e.g., 2): "))
    
    # Run algorithms back-to-back for comparison
    best_first_search(graph, heuristics, source_node, goal_node)
    beam_search(graph, heuristics, source_node, goal_node, beam_w)