def bfs(shortCuts):
    max_size = len(shortCuts)
    mins = [float('inf')] * max_size 
    mins[0] = 0
    queue = [(0, 0)]
    
    while len(queue) != 0:
        current_index, current_energy = queue.pop(0)
        
        if current_index + 1 < max_size and current_energy + 1 < mins[current_index + 1]:
            mins[current_index + 1] = current_energy + 1
            queue.append((current_index + 1, current_energy + 1))
        
        shortcut_index = shortCuts[current_index] - 1
        if current_energy + 1 < mins[shortcut_index]:
            mins[shortcut_index] = current_energy + 1
            queue.append((shortcut_index, current_energy + 1))

    return mins

_ = input()
shortCuts = list(map(int, input().split()))
print(bfs(shortCuts))
