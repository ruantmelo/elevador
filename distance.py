def distance(graph, start, end):
    """
    Find the shortest path from start to end in graph.
    """
    # Create a queue of paths
    queue = [[start]]
    # Loop until we find the end
    while queue:
        # Get the first path from the queue
        path = queue.pop(0)
        # Get the last node from the path
        node = path[-1]
        # Check if we're at the end
        if node == end:
            return len(path) - 1
        # Loop over the neighbors
        for neighbor in graph[node]:
            # Check if the neighbor has not been visited
            if neighbor not in path:
                # Add the neighbor to the path
                new_path = path + [neighbor]
                # Add the new path to the queue
                queue.append(new_path)
    # If we get here, there's no path
    return None
